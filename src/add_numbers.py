# Modulo para sumar enteros
import ctypes as C  # Poner este import acá me permite generar un código externo con esta función e importarlo 
math = C.CDLL('./libmathmine.so')

def add_int_ref_python(a,b):
    a_c = C.c_int(a)                   
    b_c = C.c_int(b)                  
    res_c = C.c_int()
    math.add_int_ref(C.byref(a_c),C.byref(b_c),C.byref(res_c))
    return res_c.value

#Modulo para sumar floats
def add_float_ref_python(a,b):
    a_c = C.c_float(a)                   
    b_c = C.c_float(b)                  
    res_c = C.c_float()
    math.add_float_ref(C.byref(a_c),C.byref(b_c),C.byref(res_c))
    return res_c.value
