from xml.etree.ElementTree import Element,XML
from typing_extensions import *
from os.path import isfile,dirname

try:
    from . import error
    from .widget import *
except ImportError:
    import error
    from widget import *

TRUE = "true"

Elements = List[Element]
strs = List[str]

class LoadedElements:
    def __init__(self) -> None:
        self.widgets:strs = []
        self.frames:strs = []
        self.mainwindow:str = ''
        self.subwindows:strs = []

class Xml:
    def __init__(self) -> None:
        self.frames:Elements = []
        self.mainwindow:Element
        self.subwindows:Elements = []
        self.widgets:Elements = []

def _find_elem(root:Element,name:str,all:bool):
    result = None
    if all:
        result = root.findall(name)
    else:
        result = root.find(name)
    if not result:
        raise error.ele_notfound(name)
    return result

# 不是不会写find，只是懒得挨个查空……
def xml_find(root:Element,name:str) -> Element:
    return _find_elem(root,name,False)

def xml_findall(root:Element,name:str) -> Elements:
    return _find_elem(root,name,True)

class Application:
    #region 绑定用的修饰器
    def bind_command(self,id:str):
        "给函数绑定command"
        def decorator(func):
            self.commands[id] = func
            return func
        return decorator
    
    def bind_event(self,id:str):
        "给函数绑定事件"
        def decorator(func):
            self.events[id] = func
            return func
        return decorator
    #endregion

    def __init__(self,appxml:str) -> None:
        global Image
        self.dir = dirname(appxml)
        self.events = {}
        self.commands = {}
        self.binds = {}
        with open(appxml,'r',encoding='utf-8') as f:
            self.appxml = XML(f)
        self.load = LoadedElements()
        self.xml = Xml()
        # 加载application xml
        app = self.appxml.find("Application")
        if not app:
            raise error.ele_notfound("Application")
        
        self.config = app.attrib
        self.dirname = True
        # 解析参数
        if 'enable-pil' in self.config:
            if self.config['enable-pil'] == TRUE:
                from PIL import Image
            else:
                try:
                    del Image
                except NameError:
                    pass
                Image = None
        if 'enable-dirname' in self.config:
            self.dirname = (self.config['enable-dirname'] == TRUE)
        # 获取Element内指向xml文件的src参数
        def get_srcattr(ele:str) -> List[str]:
            lst = []
            name = 'src'
            for e in app.findall(ele):
                if name in e.attrib:
                    lst.append(e.attrib[name].replace('?dir',self.dir) if self.dirname else e.attrib[name])
                else:
                    raise error.attr_notfound(name)
            return lst
        mainwindow = xml_find(app,"MainWindow")
        if 'src' not in mainwindow.attrib:
            raise error.attr_notfound("src")
        self.load.mainwindow = mainwindow.attrib['src'].replace('?dir',self.dir) if self.dirname else mainwindow.attrib['src']
        self.load.subwindows = get_srcattr("SubWindow")
        self.load.widgets = get_srcattr("Widget")
        self.load.frames = get_srcattr("Frame")
        # 加载xml
        with open(self.load.mainwindow,'r',encoding='utf-8') as f:
            self.xml.mainwindow = XML(f)
        for fp in self.load.subwindows:
            with open(fp,'r',encoding='utf-8') as f:
                self.xml.subwindows.append(XML(f))
        for fp in self.load.frames:
            with open(fp,'r',encoding='utf-8') as f:
                self.xml.frames.append(XML(f))
        for fp in self.load.widgets:
            with open(fp,'r',encoding='utf-8') as f:
                self.xml.widgets.append(XML(f))

    def parse_control(self,control_element:Element):
        ... # TODO 递归解析控件（困难）

    def parse_mainwindow(self):
        mw = xml_find(self.xml.mainwindow,'MainWindow')
        width = 0
        height = 0
        x = 0
        y = 0
        x_place = 0
        y_place = 0
        center = ''
        attr = mw.attrib
        ... # TODO 创建主窗体

