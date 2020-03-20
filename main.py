print("Hello World")

# Concatenar strings con números
print("This costs " + str(4) + " Dollars")

# Convertir en array un string
print("Hello:Nick:World".split(":"))


print("Hello:Nick:World".split(":")[1])  # Acceder al indice del array

# Comparacion de valores booleanos
print(5 == 5)  # true
print(5 is 5)  # true
print(5 is not 5)  # true
print("This" is "This")  # true
print("True" is True)  # false - because it evaluates the type too

# Lists (Arrays)
['Movies', 'Games', 'Python']
['Movies', 6, 'Python']

# Dictionaries (son tipo JSON, key value format)
{"name": "Nick", "age": 27, "hobby": "code"}

# Variables
greeting = "Hello World"
greeting = greeting.split(" ")[0]  # separa el string en el valor que asignemos, lo convierte en array para que nos devuelva lo que le asignemos
number = 1
secondnumber = 2
print( number * secondnumber + secondnumber * number)

# funciones básicas (built-in)///////////////////////////////////

print("Imprime")
str(5)  # convierte en string
str("True")
int("4")  # convierte en int
float("5.4")  # convierte en float
bool("True") # convierte en booleandos

len("Hello") # determina el length de strings y arrays
len([1, 2, 3, 4])
len(["Hello", "John"])

sorted([16, 3, 8, 6, 9, 133, 435, 21, 823, 45]) # ordena numericamente

sorted(["B", "R", "a", "N"]) # ordena alfabeticamente (primero numeros luego capital letters y luego lowercase)





