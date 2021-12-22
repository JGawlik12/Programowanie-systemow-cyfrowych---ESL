from myhdl import block

@block
def top(...):
    ...
    instance_1 = module_1(...)
    instance_2 = module_2(...)
    ...
    instance_n = module_n(...)
    ...
    return instance_1, instance_2, ... , instance_n

