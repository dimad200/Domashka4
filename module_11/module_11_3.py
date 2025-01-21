import inspect
from pprint import pprint


# Напишу тестовый класс
class Test_class():
    def __init__(self,name, value_1,value_2):
        self.name=name
        self.value_1=value_1
        self.value_2 = value_2

    def matematika(self):
        a=(self.value_1 + self.value_2) / 2
        return f"Среднее значение объекта '{self.name}' равно: {a} "



def introspection_info(obj):
    info = {}
    info["type"] = type(obj)
    module=[]
    att=[]
    method=[]
    try:
        obj_type = type(obj).__name_
    except:
        obj_type = type(obj)

    attributes=[attr_name for attr_name in dir(obj) if not callable(getattr(obj,attr_name)) and not inspect.ismodule(getattr(obj,attr_name))]
    methods=[ attr_name for attr_name in dir(obj) if callable(getattr(obj,attr_name))]
    # module=[attr_name for attr_name in dir(obj) if not attr_name.startswith("__") and inspect.ismodule(getattr(obj,attr_name))]
    module = [attr_name for attr_name in dir(obj) if inspect.ismodule(getattr(obj, attr_name))]

    info["attributes"]=attributes
    info["method"] = methods
    info["module"]=module

    return info

a=Test_class("первый",3,9)
print(a.matematika())

pprint(introspection_info(a))

pprint(introspection_info("a"))

pprint(introspection_info(inspect))