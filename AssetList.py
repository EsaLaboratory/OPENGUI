"""OPENGUI AssetList Module

The AssetList module contains all of the methods that manipulate the active asset list and the parameters of each asset."""
#TODO FINISH DOCUMENTATION
from unittest.util import strclass
import wx
import wx.propgrid as pg
import System.Assets as ass
import System.Markets as mar
import SaveData as sv

# TEMPORARY
import numpy as np
import ast

asset_dict = {
    "Asset" : ass.Asset.__init__.__code__.co_varnames,
    "Building" : ass.BuildingAsset.__init__.__code__.co_varnames,
    "Storage" : ass.StorageAsset.__init__.__code__.co_varnames,
    "NonDispatch" : ass.NondispatchableAsset.__init__.__code__.co_varnames,
    "Asset (3 phase)" : ass.Asset_3ph.__init__.__code__.co_varnames,
    "Storage (3 phase)" : ass.StorageAsset_3ph.__init__.__code__.co_varnames,
    "NonDispatch (3 phase)" : ass.NondispatchableAsset_3ph.__init__.__code__.co_varnames,
    "Market" : mar.Market.__init__.__code__.co_varnames
}

# for now just manually import default values...
#Note the first item bust be none since it is zipped with "self"
asset_defaults = {
    "Asset" : ass.Asset(1,1/60,60/24,1), #1440 below was 2
    "Building" : ass.BuildingAsset(18,16,90,200,17,500,0.0337,3,1,0,1,1/60,1440,0.25,0.166667),
    "Storage" :  ass.StorageAsset([0],[0],[0],[0],0.0,0.0,0.0,0.0,0,0.0,0),
    "NonDispatch" : ass.NondispatchableAsset(0.0,0.0,0.0,0.0,0),
    "Asset (3 phase)" : ass.Asset_3ph(0.0,[0],0.0,0),
    "Storage (3 phase)" : ass.StorageAsset_3ph([0],[0],[0],[0],0.0,0.0,0.0,[0],0.0,0,0.0,0), #Maybe have a selector for wye, delta, 3phase connexions?
    "NonDispatch (3 phase)" : ass.NondispatchableAsset_3ph(0.0,0.0,0.0,[0],0.0,0),
    "Market" : mar.Market(1, 0.04, 0.07, 0.10, 500, -500, 0.25, 96, None, None, 0.6, 0.4, 0.005, None, 0.13) #TODO prices import and export aren't just numbers...
} #This might not be the best way to do it, usually the numbers are found by formulas or smth...


def translate(value, default):
    if type(default) is int:
        return int(value)
    elif type(default) is float:
        return float(value)
    elif type(default) is str:
        return value
    elif type(default) is list:
        print(ast.literal_eval(value))
        return ast.literal_eval(value)
    elif type(default) is np.ndarray:
        return np.array(ast.literal_eval(value)) # I think this works!
    #TODO maybe add more



class ActiveAsset(ass.BuildingAsset, ass.StorageAsset, ass.NondispatchableAsset, ass.StorageAsset_3ph, ass.NondispatchableAsset_3ph):
    
    active_assets = []
    
    def pickAsset(asset_type):
        return asset_defaults[asset_type]
    
    # def update(self, )

    def __init__(self, name, asset_type):
        self.name = name
        self.asset_type = asset_type
        self.asset = ActiveAsset.pickAsset(asset_type)
        
        ActiveAsset.active_assets.append(self)
    
class ActiveMarket(mar.Market):
    active_markets = []
    
    def __init__(self, name):
        self.name = name
        self.market = asset_defaults["Market"]
        ActiveMarket.active_markets.append(self)

def updateParam(label, value, item, asset_type): 
    if asset_type == "Network":
        pass
    elif asset_type == "Market":
        for param, default in ActiveMarket.active_markets[item].market.__dict__.items():
            if param == "self":
                continue
            if str(param) == label:
                translate(value, default)
                code = f"ActiveMarket.active_markets[item].market.{param} = value"
                exec(code) #FIXME this is so hideous I hate it but it works for now
                break
    else:
        for param, default in ActiveAsset.active_assets[item].asset.__dict__.items():
            if param == "self":
                continue
            if str(param) == label:
                translate(value, default)
                # if type(default) is list:
                #TODO add all data types
                code = f"ActiveAsset.active_assets[item].asset.{param} = value"
                exec(code) #FIXME this is so hideous I hate it but it works for now
                break
    for param, default in ActiveMarket.active_markets[item].market.__dict__.items():
        print(param, default)

def populateAssetList( self , active, column ):
    """_summary_

    Args:
        active (_type_): _description_
        column (_type_): _description_
        font (_type_): _description_
    """
    
    self.m_ActiveAssetList.ClearAll()
    self.m_ActiveAssetList.InsertColumn(0, "Object Name", wx.LIST_FORMAT_LEFT, column)
    self.m_ActiveAssetList.InsertColumn(1, "Object Type", wx.LIST_FORMAT_RIGHT, column)
    listfont = self.m_ActiveAssetList.GetFont()
    headfont = listfont.MakeBold()
    headAttr = wx.ItemAttr((0,0,0), (240,240,240), headfont)
    self.m_ActiveAssetList.SetHeaderAttr(headAttr)
    if active == "Market":
        for market in ActiveMarket.active_markets:
            index = self.m_ActiveAssetList.InsertItem( self.m_ActiveAssetList.GetItemCount(), market.name )
            self.m_ActiveAssetList.SetItem( index, 1, "Market" )
    if active == "Network":
        index = self.m_ActiveAssetList.InsertItem( 0, "Network" )
        self.m_ActiveAssetList.SetItem( index, 1, "Network" )
    if active == "Assets":
        for asset in ActiveAsset.active_assets:
            index = self.m_ActiveAssetList.InsertItem( self.m_ActiveAssetList.GetItemCount(), asset.name )
            self.m_ActiveAssetList.SetItem( index, 1, asset.asset_type )




def populateParameterList( self, item, active ): # pass the market as ITEM when Market active
    self.m_propertyGrid.Clear()
    if active == "Market":
        #FIXME
        for param, default in ActiveMarket.active_markets[item].market.__dict__.items():
            if param == "self":
                continue
            if type(default) is np.ndarray: # Just to make it a bit more readable
                default = list(default)
            self.m_propertyGrid.Append( pg.StringProperty( param, param, str(default) )) #third param is default value
    elif active == "Network":
        #TODO Network implementation
        pass
    else: # ALL ASSETS
        for param, default in ActiveAsset.active_assets[item].asset.__dict__.items():
            if param == "self":
                continue
            if type(default) is np.ndarray: # Just to make it a bit more readable
                default = list(default)
            #TODO add a way of adding a multiple entry one for the array type data
            self.m_propertyGrid.Append( pg.StringProperty( param, param, str(default) )) #third param is default value
    
    

# TESTING ---------------------------------------------------------    
    
# # TESTING: best method is to replace the class instance
# #"Asset (3 phase)" : ass.Asset_3ph(0.0,[0],0.0,0), 
# newasset = ActiveAsset("Wow", "Asset (3 phase)")
# for attr, value in newasset.asset.__dict__.items():
#     print(attr, value)
    
# newasset.asset = ass.Asset_3ph(7.4,[0],0.0,0)
    
# for attr, value in newasset.asset.__dict__.items():
#     print(attr, value)

# x = ActiveMarket("Market1")
# print(x.name)
# print(ActiveMarket.active_markets[0].market.__dict__.items())

x = ActiveMarket("Market1")

# #storage assets
#None

dt = 1/60 #1 minute time intervals
T = int(24/dt) #Number of intervals
dt_ems = 15/60 #30 minute EMS time intervals
T_ems = int(T*dt/dt_ems) #Number of EMS intervals

#building assets
bldg_i = ActiveAsset("Building 1", "Building")
bldg_i.asset.Tmax = 18*np.ones(T_ems)
bldg_i.asset.Tmin = 16*np.ones(T_ems)
bldg_i.asset.Hmax = 90
bldg_i.asset.Cmax = 200
bldg_i.asset.deltat
bldg_i.asset.T0 = 17
bldg_i.asset.C = 500
bldg_i.asset.R = 0.0337
bldg_i.asset.CoP_heating = 3
bldg_i.asset.CoP_cooling = 1
# bldg_i.asset.Ta = None #CHOOSE WITHIN CASE
# bldg_i.asset.bus_id  = None #CHOOSE WITHIN CASE
bldg_i.asset.dt = dt
bldg_i.asset.T = T
bldg_i.asset.dt_ems = dt_ems
bldg_i.asset.T_ems = T_ems


#nondispatch assets
bus3_gen = ActiveAsset("PV Gen Bus3", "NonDispatch")
bus3_gen.asset.dt = dt
bus3_gen.asset.T = T
# bus3_gen.asset
# bus3_gen.asset
# bus3_gen.asset

bus3_load = ActiveAsset("Load Bus3", "NonDispatch")
bus3_load.asset.dt = dt
bus3_load.asset.T = T
# bus3_load.asset
# bus3_load.asset
# bus3_load.asset

# print(bus3_gen.asset.Pnet)