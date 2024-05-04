# TkXML

## 设计器
TkXML-Designer

## 依赖项
pillow

typing_extensions

## XML根元素规范
<details>

* `Application`：<br>
    TkXML应用程序窗体主文件。子元素只能是自闭合元素，都使用`src`属性指定路径。`src`属性中`?div`会被换成`dirname(Application.xml)`
    * Element `MainWindow`：主窗体，只允许有一个，且必须有一个。不止一个时只加载最前面的
    * Element `Toplevel`：子窗体
    * Element `Frame`：框架/页面文件(其实是Canvas)
    * Element `Widget`：自定义控件
* `MainWindow`：主窗体文件，允许子控件（子元素）
* `Frame`：框架/页面文件，允许子控件
* `SubWindow`：子窗体文件
* `Widget`：自定义控件文件
* `Config`：配置信息
</details>

## 基本控件
<details>

### 部分参数说明
<details>

#### center
控件/窗体中心点位置<br>
`L`:左，`R`:右，`T`:顶，`B`:底，存在两个相对的方位参数时取其中心。默认为`LP`。<br>
`LR` = `T`，`TB` = `L`，`LRTB` = 中心
#### width, height, x, y
末尾有`%`时使用百分比，单位1为父控件/主屏幕
#### font
只允许使用系统上已安装的字体，无法使用外部文件
#### 指定文件路径的参数
支持开头`?dir`替换
#### 布尔类型的参数
xml内使用`true`字符串代替python的`True`，使用`false`字符串代替python的`False`。<br>
无法解析为布尔类型的字符串默认当`false`处理
#### 颜色参数
使用hex颜色字符串`#000000`
#### master
父窗体参数自动赋值
</details>

### 头部控件
<details>

#### MainWindow
主窗体（Tk）
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* style:int 窗体样式 `0`.默认，`1`.只有一个关闭键，`2`.没有标题栏
* title:str 标题栏
* icon:str 图标路径
* resize:bool 允许改变大小
* toplevel:bool 置于顶层
* alpha:float 透明度，最大100，最小0
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* hide:bool 隐藏窗体
* status:str 状态
* minisize:bool 允许最小化
* maxsize:bool 允许最大化
* fix_noicon:bool 无图标时尝试恢复在任务栏的图标

#### SubWindow
子窗体
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* style:int 窗体样式 `0`.默认，`1`.只有一个关闭键，`2`.没有标题栏
* title:str 标题栏
* icon:str 图标路径
* resize:bool 允许改变大小
* toplevel:bool 置于顶层
* alpha:float 透明度，最大100，最小0
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* hide:bool 隐藏窗体
* status:str 状态
* minisize:bool 允许最小化
* maxsize:bool 允许最大化
* fix_noicon:bool 无图标时尝试恢复在任务栏的图标
* id:str id
</details>

### 中部控件
<details>

#### Frame
页面/框架（实际上这是Canvas）
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id

#### ScrollFrame
滚动页面
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* place:int 默认位置
* scroll_speed:int 滚动速度
</details>

### 尾部控件
<details>

#### Button
按键
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* text:str 按键文本
* command:str 点击时触发的事件

#### RadioButton
单选框
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* command:str 点击时触发的事件

#### CheckButton
复选框
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id

#### Switch
开关
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id

#### Entry
输入框
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* prompt:str 输入提示文本
* prompt_fg:str 提示文本颜色
* disabled_prompt_fg:str 禁用时的提示文本颜色

#### Label
文本
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* text:str 文本

#### Combobox
选择器
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* prompt:str 选择提示文本
* prompt_fg:str 提示文本颜色
* disabled_prompt_fg:str 禁用时的提示文本颜色

#### ListBox
列表
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* index:int 当前索引
* scroll_speed:int 滚动速度

#### ProgressBar
进度条
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* value:int 当前值
* max_value: 最大值

#### Scale
拖拽条
* width:int 窗体宽度
* height:int 窗体高度
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* value:int 当前值
* max_value: 最大值
</details>

### 预制窗体
<details>

#### Palette
调色板
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* value:str 当前选择颜色
* ok_command:str 确认键按下事件
* cancel_command:str 取消事件 关闭键也视为取消
* destroy_button:bool 有关闭键

#### CalendarClock
日历和钟
* center:str 中心点位置
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* datetime_value:str 当前选择的时间和日期
* ok_command:str 确认键按下事件
* cancel_command:str 取消事件 关闭键也视为取消
* destroy_button:bool 有关闭键

#### Tooltip
提示文本窗体
* x:int X轴位置
* y:int Y轴位置
* bg:str 背景颜色
* fg:str 字体颜色
* font:str 字体名字
* disabled_bg:str 禁用时的背景颜色
* disabled_fg:str 禁用时的字体颜色
* status:str 状态
* id:str id
* text:str 提示文本
</details>

### 控件配置
<details>

```xml
<!--为指定的元素添加图片 只允许有一个-->
<Image target="" id="" src="" svg_color="" svg_path="" svg_size=""/>
<!--为指定的元素绑定事件 允许同时绑定多个-->
<Bind target="" event="" command="" id=""/>
<!--为指定的元素添加提示文本 只允许有一个-->
<Prompt target="" id="" text=""/>
<!--为指定的元素添加文本，可追加 mode: Literal['w', 'a']-->
<AddText target="" index="" color="" text="" mode="a"/>
<!--父类为Canvas时在Canvas上创建图形-->
<Draw type="" id="">
    <Param name="" type=""/>
</Draw>
```
</details>
</details>

## 开源协议
MIT License