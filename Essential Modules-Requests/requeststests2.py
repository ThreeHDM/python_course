import requests
#   Pillow is an image processing library
from PIL import Image
#   A class that helps use the byte data
from io import BytesIO

r = requests.get("https://i.pinimg.com/originals/b6/11/9f/b6119f219b33cc8624077d05bd3145a2.jpg")

print("Status code", r.status_code)

#   Create an image from the binary data returned. Instead of using r.text we use r.content which is binary data
#   BytesIO --> converts it into an image we can use
image = Image.open(BytesIO(r.content))

#   Print data about the image
print(image.size, image.format, image.mode)

#   Create the path where we save the image and we assign it the format
path = "./image." + image.format

try:
    image.save(path, image.format)
#   if there were an IO error
except IOError:
    print("Cannot save image.")
