import csv
import Popups
from os.path import exists as file_exists
# from os.path import join
# from os import mkdir
import os

def writeToCSV(data, name, filetype):
    #TODO add option to select if overwrite file. Currently it will just overwrite.
    if not file_exists("SaveData"):
        os.mkdir(os.getcwd()+"/SaveData")
    #save to SaveData Directory
    save_path = "SaveData/"
    filename = os.path.join(save_path, name + filetype)
    if filetype == ".txt":
        with open(filename, 'w') as f:
            for row in data:
                for elem in row:
                    f.write(str(elem))
                f.write("\n")
    else:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

def readFromCSV(filename):
    try:
        # csvfile = open(filename + '.csv', newline='', encoding='utf-8-sig')
        csvfile = open(filename, newline='', encoding='utf-8-sig')
    except OSError:
        error_popup = Popups.GenericError("File not found!")
        error_popup.ShowModal()
        return
    
    with csvfile:
        try:
            filereader = csv.reader(csvfile)
            returndata = list(filereader)
            # print(returndata)
        except UnicodeDecodeError:
            error_popup = Popups.GenericError("Filetype not supported!")
            error_popup.ShowModal()
            return
    return returndata

# Eventually there will be an import data function here...
