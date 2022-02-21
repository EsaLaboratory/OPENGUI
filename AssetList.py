import wx
import wx.propgrid as pg
import System.Assets as ass

def populateAssetList( self , active ):
    print(self.m_ActiveAssetList.InReportView())
    self.m_ActiveAssetList.ClearAll()
    self.m_ActiveAssetList.InsertColumn(0, "Asset Name", wx.LIST_FORMAT_LEFT, wx.LIST_AUTOSIZE)
    self.m_ActiveAssetList.InsertColumn(1, "Asset Type", wx.LIST_FORMAT_RIGHT, wx.LIST_AUTOSIZE)
    if active == "Market":
        index = self.m_ActiveAssetList.InsertItem( 0, "Market" )
        self.m_ActiveAssetList.SetItem( index, 1, "Market" )
    if active == "Network":
        index = self.m_ActiveAssetList.InsertItem( 0, "Network" )
        self.m_ActiveAssetList.SetItem( index, 1, "Network" )
    if active == "Assets":
        assets = [("Building 1","Building"), ("Asset 2","Asset")]
        for asset_name, asset_type in assets:
            index = self.m_ActiveAssetList.InsertItem( 0, asset_name )
            self.m_ActiveAssetList.SetItem( index, 1, asset_type )

asset_dict = {
    "Asset" : ass.Asset.__init__.__code__.co_varnames,
    "Building" : ass.BuildingAsset.__init__.__code__.co_varnames,
    "Storage" : ass.StorageAsset.__init__.__code__.co_varnames,
    "NonDispatch" : ass.NondispatchableAsset.__init__.__code__.co_varnames,
    "Asset (3 phase)" : ass.Asset_3ph.__init__.__code__.co_varnames,
    "Storage (3 phase)" : ass.StorageAsset_3ph.__init__.__code__.co_varnames,
    "NonDispatch (3 phase)" : ass.NondispatchableAsset_3ph.__init__.__code__.co_varnames
}

# print(asset_dict["Asset"])

def populateParameterList( self, asset_type ):
    self.m_propertyGrid.Clear()
    params = asset_dict[asset_type]
    for param in params:
        self.m_propertyGrid.Append( pg.StringProperty( param, param ))
    print(params)
    
# self.m_propertyGridItem3 = self.m_propertyGrid.Append( pg.StringProperty( u"Name3", u"Name3" ) )