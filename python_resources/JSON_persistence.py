#   JSON needs a package
#   pip3 install simplejson

import simplejson as json
#   We also import the os class to get aditional file data
import os

#   We check if the file exists and if it is greater than 0
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    # leemos el archivo
    old_file = open("./ages.json", "r+")
    # leemos el archivo y lo almacenamos como un objeto de python
    data = json.loads(old_file.read())
    print("Current age is ", data["age"], " -- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name" : "Juan", "age" : 31}
    print("No file found, setting default age to", data["age"])


#   Esta linea hace que pise el archivo. De lo contrario la información se agrega (append)
old_file.seek(0)
#   Escribimos el archivo pero antes debemos convertirla en un objeto json nuevamente
old_file.write(json.dumps(data))

