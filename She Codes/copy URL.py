#random image name
from random import randint
import requests

File_Name = randint(1, 1000)
Image_Name = str(File_Name) + ".jpg"
#save image url
url = 'http://www.fodors.com/wp-content/uploads/2018/03/Ultimate-Things-To-Do-Bahamas-Hero.jpg'
r = requests.get(url)
with open(Image_Name, 'wb') as outfile:
    outfile.write(r.content)
#headers.items()
#headers["content-type"]