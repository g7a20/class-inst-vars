import types
def class_inst_vars(cls):
    inst_vars = []
    for func in dir(cls):
        if isinstance(func, types.MethodType):
            inst_vars.extend(func.__code__.co_varnames)
    return inst_vars
