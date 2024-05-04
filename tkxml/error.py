class TkXmlError(Exception):pass
class ElementNotFoundError(TkXmlError):pass
class AttribNotFoundError(TkXmlError):pass

def ele_notfound(name:str):
    return ElementNotFoundError('Element "%s" not found'%name)

def attr_notfound(name:str):
    return AttribNotFoundError('Attrib "%s" not found'%name)