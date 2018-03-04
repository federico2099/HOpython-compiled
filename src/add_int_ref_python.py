def add_int_ref_python(a,b):
    import ctypes as C  # Poner este import acá me permite generar un código externo con esta función e importarlo 
    math = C.CDLL('./libmathmine.so') #desde distintos programas que lo necesiten como una librería y que el 
    a_c = C.c_int(a)                  #usuario llame a esa librería sin saber que tiene adentro. Funcionaría como 
    b_c = C.c_int(b)                  #una caja negra.
    res_c = C.c_int()
    math.add_int_ref(C.byref(a_c),C.byref(b_c),C.byref(res_c))
    return res_c.value
