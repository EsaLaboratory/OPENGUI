import pickle
import System.Assets as ass

asset1 = ass.Asset(0, 1, 2)

# STORING ASSET
# print(asset1.__dict__)

# f = open("asset1.open", "wb")
# pickle.dump(asset1, f)
# f.close()

f=open('asset1.open','rb') #opening the file to read the data in the binary form
print(pickle.load(f))