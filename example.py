import os


path_file = os.path.realpath(__file__)
#this will give the path with the file name, ie, C:\Directory\Directory1\.....\example.py

path_file = path_file[:-10]

#removing "example.py" from the path string. -10 because example.py has 10 chars.

#====================IMPORTANT=======================
# If you change the name of the file remember to update the number.

print (path_file)
