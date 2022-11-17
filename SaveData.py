"""OPENGUI SaveData module

The SaveData module contains all of the methods of data storage and manipulation for OPENGUI.
In this module there are methods to write and read from csv/txt files.

"""

import csv
import Popups
from os.path import exists as file_exists
# from os.path import join
# from os import mkdir
import os
import pickle

#TODO make it easier to pick file name and location etc
def writeToCSV(data, name, filetype):
    """Writes data from the data grid to a csv/txt file.
    
    Currently takes the data from the data grid and stores it line by line into a csv or txt file.
    The filetype is chosen by the user from a dialogue box option.
    No returns, however the output data is written to a file that is saved in the local directory.
    
    Parameters
    ----------
    data
        The data array taken from the data grid (line by line with existing text).
    
    name
        The filename (taken from the dialogue box user input).
    
    filetype
        The file type to be saved as (currently either csv or txt).
    
    """
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
    """Reads data from a csv/txt file to the data grid.
    
    Currently takes the data from a csv or txt file (or any file containing text) and stores it line by line into the data grid.
    Newline is considered a line of data, so every newline will write the following data in the next row etc.
    
    Parameters
    ----------
    filename
        The chosen filename to read the data from.
    
    Returns
    -------
    returndata
        List of data taken from the file.
        
    """
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

def saveObject(object, name, project, type):
    """Serializes an instantiated object into a .open file

    Args:
        object (class): The instantiated object to be serialised and saved.
        
        name (string): The name of the object.
        
        project (string): The path to the active project.
        
        type (string): The type of object to be saved (Asset, Market, Network).
        
    """
    
    if type == "Asset":
        folder = r"\ENERGY_SYSTEM\ASSETS"
    elif type == "Market":
        folder = r"\ENERGY_SYSTEM\MARKET"
    elif type == "Network":
        folder = r"\ENERGY_SYSTEM\NETWORK"
    else:
        pass
    
    #Way of getting object name from the object class?
    f = open(project+folder+name+".open", "wb")
    pickle.dump(object, f)
    f.close()
    
    return

def loadObject(filename):
    """Loads and deserialises an object with the given filename
    
    Args:
        filename (string): The name of the file to be imported.
        
    """
    return
# Eventually there will be an import data function here...
