import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def do_math():
    global run  # We give access to the global variable
    global previous

    equation = ""

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, Human")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)  # We add regex to validate the input

        if previous == 0:
            previous = eval(equation)  # evaluates the string
        else:
            previous = eval(str(previous) + equation)


while run:
    do_math()
