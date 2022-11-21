import os

path = os.getcwd() + "/UserData/"
projects = os.listdir(path)

for project in projects:
    print(project)