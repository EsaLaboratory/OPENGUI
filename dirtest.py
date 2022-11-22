import os
import pickle

path = os.getcwd() + "/UserData/test/ENERGY_SYSTEM/ASSETS/"
projects = os.listdir(path)

for project in projects:
    print(project)
    print(project[:-5]) # without .open extension
    print(path+project)
    f=open(path + project,'rb') #opening the file to read the data in the binary form
    print(pickle.load(f))

