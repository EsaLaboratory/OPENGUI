import System.Assets as ass
import System.Markets as mar
import SaveData as sv
import os
from AssetList import ActiveAsset

print(ActiveAsset.active_assets)

asset = ass.BuildingAsset(18,16,90,200,17,500,0.0337,3,1,0,1,1/60,1440,0.25,0.166667)
asset1 = ass.Asset(1,1/60,60/24,1) #1440 below was 2
asset2 = ass.NondispatchableAsset(0.0,0.0,0.0,0.0,0)
market = mar.Market(1, 0.04, 0.07, 0.10, 500, -500, 0.25, 96, None, None, 0.6, 0.4, 0.005, None, 0.13)

path = os.getcwd() + "/UserData/test/"

sv.saveObject(asset, "Building_test", path, "Asset")
sv.saveObject(asset1, "Asset_test", path, "Asset")
sv.saveObject(asset2, "NonDispatch_test", path, "Asset")
sv.saveObject(market, "Market_test", path, "Market")

# sv.loadObject("Building_test.open", path, "Asset")

print(ActiveAsset.active_assets)

# print(ActiveAsset.active_assets[0].asset.Tmax) # This returns the correct value

# print(ActiveAsset.active_assets[0].asset.__dict__.items())