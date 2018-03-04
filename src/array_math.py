import ctypes as C
math = C.CDLL('./libmathmine.so')

def add_int_array_python(a_list,b_list):
    n = len(a_list)
    in1 = (C.c_int * n) (*a_list) 
    in2 = (C.c_int * n) (*b_list)
    out_list = []
    out = (C.c_int * n) (*out_list)
    math.add_int_array(C.byref(in1),C.byref(in2),C.byref(out),C.c_int(n))
    return out[:] # Asi tengo que pedirle para que me devuelva la lista como resultado y no el puntero

def dot_product_python(a_list,b_list):
    n = len(a_list)
    in1 = (C.c_float * n) (*a_list) 
    in2 = (C.c_float * n) (*b_list)
    math.dot_product.restype = C.c_float
    res_dot_prod = math.dot_product(in1,in2,n)
    return res_dot_prod
