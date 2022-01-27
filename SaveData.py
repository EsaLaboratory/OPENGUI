import csv
from os.path import exists as file_exists

def writeToCSV(data, name):
    i = 0
    while file_exists(name + ".csv"):
        i += 1
        name = name + str(i)
    with open(name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def readFromCSV(filename):
    with open(filename + '.csv', newline='', encoding='utf-8-sig') as csvfile:
        filereader = csv.reader(csvfile)
        returndata = list(filereader)
        # print(returndata)
    return returndata

# print(readFromCSV("data"))
