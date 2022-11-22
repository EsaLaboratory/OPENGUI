import System.Assets as ass
import SaveData as sv
import os
from AssetList import ActiveAsset

print(ActiveAsset.active_assets)

asset = ass.BuildingAsset(18,16,90,200,17,500,0.0337,3,1,0,1,1/60,1440,0.25,0.166667)

path = os.getcwd() + "/UserData/test/ENERGY_SYSTEM/ASSETS/"

# sv.saveObject(asset, "Building_test", path, "Asset")

sv.loadObject("Building_test.open", path, "Asset")

print(ActiveAsset.active_assets)

print(ActiveAsset.active_assets[0].asset.Tmax) # This returns the correct value

print(ActiveAsset.active_assets[0].asset.__dict__.items())