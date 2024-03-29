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

from AssetList import ActiveAsset, ActiveMarket

#TODO make it easier to pick file name and location etc
def writeToCSV(data, name, filetype, project_path):
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
    
    project_path
        File path to active project directory.
    
    """
    #TODO add option to select if overwrite file. Currently it will just overwrite.
    # if not file_exists("SaveData"):
    #     os.mkdir(os.getcwd()+"/SaveData")
    #save to SaveData Directory
    if not file_exists(project_path + "GRID_DATA"):
        os.mkdir(project_path + "/GRID_DATA")
    save_path = project_path + "/GRID_DATA/"
    #TODO use os.path.join to fix the ugly backslashes maybe???
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
        folder = r"/ENERGY_SYSTEM/ASSETS/"
    elif type == "Market":
        folder = r"/ENERGY_SYSTEM/MARKET/"
    elif type == "Network":
        folder = r"/ENERGY_SYSTEM/NETWORK/"
    else:
        pass
    
    path = project+folder+name+".open"
    print("Path is: " + path)
    #Way of getting object name from the object class?
    f = open(path, "wb")
    pickle.dump(object, f)
    f.close()
    
    return

def loadObject(filename, filepath, object_type): #filepath without the file name
    """Loads and deserialises an object with the given filename
    
    Args:
        filename (string): The name of the file to be imported.
        
        filepath (string): The path to the current directory. (NOTE: DOES NOT INCLUDE FILENAME)
        
        object_type (string): The basic type of object to be loaded (Asset, Market, Network).
        
    """
    if object_type == "Asset":
        #ASSETS
        f=open(filepath + filename,'rb') #opening the file to read the data in the binary form
        object = pickle.load(f)
        object_name = filename[:-5] # gets rid of .open extension
        print(type(object).__name__)

        ActiveAsset(object_name, type(object).__name__, object)
    
    elif object_type == "Market":
        #MARKETS
        f=open(filepath + filename,'rb') #opening the file to read the data in the binary form
        object = pickle.load(f)
        object_name = filename[:-5] # gets rid of .open extension
        ActiveMarket(object_name, object)
    
    return
# Eventually there will be an import data function here...

#TESTING - Works!!!!!!!!

#building assets
# bldg_i = ActiveAsset("Building 1", "Building")
# bldg_i.asset.Tmax = 18*np.ones(T_ems)
# bldg_i.asset.Tmin = 16*np.ones(T_ems)
# bldg_i.asset.Hmax = 90
# bldg_i.asset.Cmax = 200
# bldg_i.asset.deltat
# bldg_i.asset.T0 = 17
# bldg_i.asset.C = 500
# bldg_i.asset.R = 0.0337
# bldg_i.asset.CoP_heating = 3
# bldg_i.asset.CoP_cooling = 1
# # bldg_i.asset.Ta = None #CHOOSE WITHIN CASE
# # bldg_i.asset.bus_id  = None #CHOOSE WITHIN CASE
# bldg_i.asset.dt = dt
# bldg_i.asset.T = T
# bldg_i.asset.dt_ems = dt_ems
# bldg_i.asset.T_ems = T_ems

# print(ActiveAsset.active_assets)

# path = os.getcwd() + "/UserData/test/ENERGY_SYSTEM/ASSETS/"
# name = "Building 1.open"
# loadObject(name, path, "Asset")

# print(ActiveAsset.active_assets)

# print(ActiveAsset.active_assets[0].asset.Tmax)