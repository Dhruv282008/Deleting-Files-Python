import os
import shutil
import time
path = input("Enter the folder to be deleted : ")

path = path + '/'

days = 30
#30 x 24 x 60 x 60

seconds = time.time() - (days * 24 * 60 * 60)

exists = os.path.exists(path) 


if (exists):
    listofFiles = os.walk(path)

while seconds:
    os.remove(path)