# Funciones definidas por el usuario ///////////////////////////////////////////////////
# definimos una funcion con def y el name. Según las pep guidelines se usa snake_case


def my_function():
    print("This is my function")
    print("A second string ")


# lo que esté indentado será parte de la función, cuando quiero que no sea parte termino la indentación

# Llamo a la funcion
my_function()


# Agregando argumentos a una función

def my_second_function(str1, str2):
    print(str1)
    print(str2)


my_second_function("string 1", "string 2")


# Default params

def print_something(name="Default Name", age="Default Age"):
    # print("My name is " + name + " and my age is " + str(age))
    # En vez de concatenar podemos separar con coma. Imprime una cosa a la vez
    print("My name is", name, "and my age is", age)


print_something("Juan", 27)
print_something()

# Keyword Arguments///////////////////////////
# None es el equivalente a null
print_something(None, 27)

# Puedo pasar los keyword arguments para pasar parametros como yo quiera y en el orden que quiera
print_something(age=27)  # omito el primer argumento y paso el segundo
print_something(age=27, name="Pepe")  # paso los args en difrente orden


# Número variable/flexible de argumentos///////////////////////

def print_people(
        *people):  # el asterisco le dice que se le pasará un array de todos los argumentos que se le pasen, se crea un array con esos args
    for person in people:  # para recorrer el array usamos un bucle for
        print("This person is", person)


print_people("Persona1", "Persona2", "Persona3")


# Return Values From Functions
def do_math(num1, num2):
    return num1 + num2


math1 = do_math(3, 4)
math2 = do_math(11, 34)

print("The first sum is ", math1, "and the second sum is", math2)


# conditional statements

check = "Hamburger"

if check == False:
    print("it is false")
elif check == "Hamburger":
    print("Que rico")
elif check == "John":
    print("Master")
else:
    print("It's True")



