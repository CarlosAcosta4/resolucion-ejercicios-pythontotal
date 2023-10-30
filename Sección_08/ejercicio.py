import os
os.system("cls")

"""#--Decoradores--
#---------------

def mayuscula (texto) :
    print(texto.upper())

mi_funcion = mayuscula
mi_funcion("python")

#---------------

def mayuscula (texto):
    print (texto.upper ())

def minuscula (texto) :
    print (texto. lower ())

def una_funcion (funcion) :
    return funcion

una_funcion(mayuscula("probando" ))

#---------------
def cambiar_letras (tipo):
    def mayuscula (texto):
        print(texto.upper ())

    def minuscula (texto):
        print(texto.lower )

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion  = cambiar_letras("may")
operacion("palabra")

#---------------

def decorar_saludo(funcion):
    def otra_funcion (palabra):
        print('hola')
        funcion(palabra)
        print ('adios')
    return otra_funcion

@decorar_saludo
def mayusculas (texto) :
    print (texto.upper())

def minusculas (texto) :
    print (texto.lower ())

mayusculas("Python")

#--------------

def decorar_saludo(funcion):
    def otra_funcion (palabra):
        print('hola')
        funcion(palabra)
        print ('adios')
    return otra_funcion


def mayusculas (texto) :
    print (texto.upper())

def minusculas (texto) :
    print (texto.lower ())

mayusculas_decorada = decorar_saludo(mayuscula)
mayusculas_decorada("fede")

#---------------
"""


