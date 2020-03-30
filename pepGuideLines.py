# Imports
# se hacen en líneas separadas

import os
import sys

# si importamos múltiples clases de un módulo se usa coma
# from myModule include foo, bar, foobar
# entre los imports y el resto del código debe haber dos blank lines


def my_function(one, two,
                three, four, # para la indentación se utilizan 4 espacios
                five, six): # para mantener a la funcion legible podemos partir los params en varias lineas bien indentadas
    print("Hello World") #entre una función y otra debe haber dos blank lines


def second_function():
    print("second function")


my_list = [1, 2,
           3, 4,
           5, 6]

# El if siempre indentado no va en una sola linea (mal: if check is True: print("This is true"))
check = True
if check is True:
    print("This is true")

# llamar a múltiples funciones separado con semicolon está mal
# function(); function2(); etc..
# se deben llamar en lineas diferentes

function()
function2()
function3()



