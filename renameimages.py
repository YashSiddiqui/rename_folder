import os

os.getcwd()
collection = ""   #add your file directory
for i, filename in enumerate(os.listdir(collection)):
    os.rename( "add your file directory" + "/" + filename,  "add your file directory" + "/" + "name?" + str(i) + ".file type")