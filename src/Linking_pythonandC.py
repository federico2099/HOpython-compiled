
# coding: utf-8

# In[1]:

import ctypes as C
math = C.CDLL('./libmathmine.so')


# In[ ]:

# Llama a la función add_int


# In[8]:

# Llamo a la función de c add_int
math.add_int(2,4)
# Me devuelve el resultado ya que tiene el return inluido


# In[ ]:

# Llama a la función float_int


# In[6]:

# Defino que los argumentos de entrada sean tipo float de C y luego que el resultado tambien lo sea
math.add_float.argtypes = [C.c_float,C.c_float] # Notar que tengo que anteponer el C. antes de c_float
math.add_float.restype = C.c_float       # ya que se trata de ctypes y lo tengo que aclarar explicitamente 
#Ahora puedo llamar a la librería desde Python de manera normal sin saber que está ejecutando código en C
math.add_float(2,4)


# In[10]:

'''

Llama a la función que suma enteros por referencia es decir, pasando como argumento la posición de memoria 
donde se encuentran los valores de cada variable

''' 


# In[9]:

'''
Escribimos un wrapper, es decir una función externa, transparente a Python (escrita en Python), 
que a su vez contendrá a otra función, es decir la librería en C. Este tipo de funciones wrappers
permite acomodar todo el entorno de variables de forma amena y organizada y permite que el usuario
llame a una función de Pÿthon (el wrapper) como una caja negra, es decir, no hace falta que el usuario
sepa que ocurre dentro del wrapper. De esta manera el usuario llamará a una función que suma dos enteros 
o floats sin saber que esa función wrapper llamará a una función escrita en C a través de una librería que es
llamada desde Python
'''


# In[ ]:

#Para sumar enteros


# In[10]:

def add_int_ref_python(a,b):
    import ctypes as C  # Poner este import acá me permite generar un código externo con esta función e importarlo 
    math = C.CDLL('./libmathmine.so') #desde distintos programas que lo necesiten como una librería y que el 
    a_c = C.c_int(a)                  #usuario llame a esa librería sin saber que tiene adentro. Funcionaría como 
    b_c = C.c_int(b)                  #una caja negra.
    res_c = C.c_int()
    math.add_int_ref(C.byref(a_c),C.byref(b_c),C.byref(res_c))
    return res_c.value


# In[11]:

add_int_ref_python(2,4)


# In[ ]:

#Para sumar floats


# In[6]:

def add_float_ref_python(a,b):
    import ctypes as C  # Poner este import acá me permite generar un código externo con esta función e importarlo 
    math = C.CDLL('./libmathmine.so') #desde distintos programas que lo necesiten como una librería y que el 
    a_c = C.c_float(a)                  #usuario llame a esa librería sin saber que tiene adentro. Funcionaría como 
    b_c = C.c_float(b)                  #una caja negra.
    res_c = C.c_float()
    math.add_float_ref(C.byref(a_c),C.byref(b_c),C.byref(res_c))
    return res_c.value


# In[8]:

add_float_ref_python(2.1,4.1)


# In[12]:

'''Ahora voy a hacer las mismas dos cuentas anteriores (suna int/float by ref) pero definiendo los wrappers
como librerías, poniéndolas en otro código e importándolas desde acá'''


# In[39]:

'''
Con esta sentencia puedo importar desde el código add_int_ref_python.py el módulo que desee (en este caso
tengo solo 1) y con el "as" le redefino el nombre dentro del programa que lo invoca 
'''
from add_int_ref_python import add_int_ref_python as sumaent  
sumaent(22,42)


# In[33]:

'''
Con esta sentencia puedo importar desde el código add_ref_ref_python.py el módulo que desee (en este caso
tengo solo 1) y con el "as" le redefino el nombre dentro del programa que lo invoca 
'''
from add_float_ref_python import* # El mismo código de recióen está guardado en add_float_ref_python.py
add_float_ref_python(2.1,4.1)


# In[34]:

'''
De esta manera puedo tener solo un código escrito por fuera de este programa que tenga ambos módulos e importar
uno u otro del mismo código según lo que quiera. A continuación va eso. Desde el código externo add_numbers.py 
importo el módulo para sumar floats o ints
'''


# In[3]:

from add_numbers import add_int_ref_python as sumaent  


# In[4]:

sumaent(4,4)


# In[5]:

from add_numbers import add_float_ref_python as sumafloat  


# In[7]:

sumafloat(34.,31.) #Acá no se por qué no anda


# In[ ]:

#Arrays


# In[2]:

a_list = [1,2,3,4]
b_list = [4,3,2,1]


# In[3]:

n = len(a_list)
in1 = (C.c_int * n) (*a_list) 
in2 = (C.c_int * n) (*b_list)
'''
El (*a/b_list) es una sintaxis acotada para acceder alos elementos de una lista. El Ctypes (C.c_int * n_b) 
"pide acceder a los elementos de la lista para asignar y alocatear in1 como un array de 4 elementos. La manera
"no eficiente" de hacer esto sería:

in1 = (C.c_int * 4) [1,2,3,4] 
in2 = (C.c_int * 4) [4,3,2,1]

Esto es poco eficiente porque si quiero definir un wrapper como en el caso anterior, al hacerlo de forma eficiente
yo paso una lista a cualquiera y el wrapper ser encargará de interpretarla y allocatearla
'''


# In[4]:

out_list = []
out = (C.c_int * n) (*out_list)


# In[6]:

#math.add_float.argtypes = [C.c_float,C.c_float]
math.add_int_array(C.byref(in1),C.byref(in2),C.byref(out),C.c_int(n))
print(*out) #out está definido como posición de memoria y así lo devuelve la fucion de C, entonces con el *
            #lo desreferencio


# In[7]:

# Ahora hago lo mismo pero definiendo un wrapper


# In[8]:

def add_int_array_python(a_list,b_list):
    n = len(a_list)
    in1 = (C.c_int * n) (*a_list) 
    in2 = (C.c_int * n) (*b_list)
#    if n_a > n_b:
#        n_out = n_a #Esto esta puesto al pedo porque no tiene sentido de acuerdo a la def de adicion de vec
#    else:           #Podria usar directamente o n_a o n_b
#        n_out = n_b
    out_list = []
    out = (C.c_int * n) (*out_list)
    math.add_int_array(C.byref(in1),C.byref(in2),C.byref(out),C.c_int(n))
    return out[:] # Asi tengo que pedirle para que me devuelva la lista como resultado y no el puntero


# In[9]:

a = [1,2,3,4]
b = [1,2,3,4]
result_add = add_int_array_python(a,b)


# In[10]:

print(result_add)


# In[11]:

# Dot Product


# In[12]:

def dot_product_python(a_list,b_list):
    n = len(a_list)
    in1 = (C.c_float * n) (*a_list) 
    in2 = (C.c_float * n) (*b_list)
    math.dot_product.restype = C.c_float
    res_dot_prod = math.dot_product(in1,in2,n)
    return res_dot_prod


# In[13]:

result_dot_prod = dot_product_python(a,b)


# In[14]:

print(result_dot_prod)


# In[15]:

# Ahora defino un código externo que se llama arrays_math.py y llamo a los modulos para hacer las cuentas


# In[16]:

from array_math import add_int_array_python as suma_arrays
from array_math import dot_product_python as dot_prod


# In[17]:

a_new = [10,10,10]
b_new = [1,1,1]
result_suma_arrays = suma_arrays(a_new,b_new)


# In[18]:

print(result_suma_arrays)


# In[19]:

result_dot_product = dot_prod(a_new,b_new)
print(result_dot_product)


# In[ ]:



