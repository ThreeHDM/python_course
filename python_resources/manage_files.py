# Reading and writing files

#   open takes a path as first parameter and the second is the action we want to perform. w+ means write
newfile = open("newfile.txt", "w+")

string = "This is the content that will be written to the text file"

newfile.write(string)