import inspect, requests, tkinter

from PIL.DdsImagePlugin import module
from Scripts.bottle import request


def introspection_info(obj):
    info = {}
    info["type"] = type(obj)
    module=[]
    print(dir(obj))
    print()
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        # print(attr_name, type(attr))
        if inspect.ismodule(attr):
            otvet="\u001b[0;32m ДА \u001b[0m"
            module.append(attr_name)
        else:
            otvet="\u001b[0;31m Нет \u001b[0m"
        print(f"{attr_name} это модуль : {otvet} ")
        # print(inspect.getmembers(obj))
    return info, module


print(introspection_info(requests))
print(inspect.ismodule(requests))
