import csv
from distutils.log import error
import Popups
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
    try:
        csvfile = open(filename + '.csv', newline='', encoding='utf-8-sig')
    except OSError:
        error_popup = Popups.GenericError("File not found!")
        error_popup.ShowModal()
        return
    with csvfile:
        filereader = csv.reader(csvfile)
        returndata = list(filereader)
        # print(returndata)
    return returndata

# Eventually there will be an import data function here...
