# -*- coding: utf-8 -*-
"""OPENGUI CurrentFullCanvas module

The CurrentFullCanvas module is the main file for OPENGUI.
From here, the gui window runs, and all of the subsidary modules are called from this module.

"""
###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
###########################################################################
#TODO change names of modules (gui_main etc...)
import sys, os
from SaveData import readFromCSV, writeToCSV, saveObject, loadObject
import wx
import wx.xrc
import wx.grid
import wx.propgrid as pg
from wx import html2
from webbrowser import open as link

#Dialogues
import Dialogues
import Popups
import AssetList
# import curves

# #OPEN

#Local Directory 
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script

#TODO add titles to the panels
#TODO have a better way of storing data. Currently there isn't a clean way of data permanence.
###########################################################################
## Class frameMain
###########################################################################
class frameMain ( wx.Frame ):
    """Main frame of the canvas. Container for all subframes.

    """

    def __init__( self, parent ):
        """Constructor"""
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OPEN_GUI", pos = wx.DefaultPosition, size = wx.Size( 1555,897 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

        bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

        bSizerActiveArea = wx.BoxSizer( wx.HORIZONTAL )
        
        #active project
        #TODO this should load the previous project by default
        self.active_project_name = ""
        self.active_project_path = ""
        
        #Title font for panel titles
        self.m_titleFont = wx.Font(wx.FontInfo(10).Bold())

#--LEFT--############################################################################################################################################################################################
        bSizerLeft = wx.BoxSizer( wx.VERTICAL )

        self.m_panelUserLibrary = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelUserLibrary = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainUserLibrary = wx.BoxSizer( wx.VERTICAL )

        # USER LIBRARY

        #User Library Panel Title
        self.m_userLibraryTitle = wx.StaticText( self.m_panelUserLibrary, wx.ID_ANY, u"USER LIBRARY", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE_HORIZONTAL, wx.StaticTextNameStr )
        self.m_userLibraryTitle.SetFont(self.m_titleFont)
        bSizerPanelMainUserLibrary.Add( self.m_userLibraryTitle, 0, wx.EXPAND, 0 )

        #Here I am using os.getcwd() to get the current directory
        # self.directory = os.getcwd()
        self.m_dirPicker = wx.DirPickerCtrl( self.m_panelUserLibrary, wx.ID_ANY, self.active_project_path, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizerPanelMainUserLibrary.Add( self.m_dirPicker, 0, 0, 1 )

        self.m_userLibrary = wx.GenericDirCtrl( self.m_panelUserLibrary, wx.ID_ANY, self.active_project_path, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )
        self.m_userLibrary.ShowHidden( False )
        
        bSizerPanelMainUserLibrary.Add( self.m_userLibrary, 1, wx.EXPAND, 1 )


        bSizerMainPanelUserLibrary.Add( bSizerPanelMainUserLibrary, 1, wx.EXPAND, 0 )


        self.m_panelUserLibrary.SetSizer( bSizerMainPanelUserLibrary )
        self.m_panelUserLibrary.Layout()
        bSizerMainPanelUserLibrary.Fit( self.m_panelUserLibrary )
        bSizerLeft.Add( self.m_panelUserLibrary, 1, wx.ALL|wx.EXPAND, 0 )

        
        # ENERGY SYSTEM TREE
        
        self.m_panelEnergySystemTree = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelEnergySystemTree = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainEnergySystemTree = wx.BoxSizer( wx.VERTICAL )
        
        # Energy System Tree Panel Title
        self.m_panelEnergySystemTreeTitle = wx.StaticText( self.m_panelEnergySystemTree, wx.ID_ANY, u"ENERGY SYSTEM TREE", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE_HORIZONTAL, wx.StaticTextNameStr )
        self.m_panelEnergySystemTreeTitle.SetFont(self.m_titleFont)
        bSizerPanelMainEnergySystemTree.Add( self.m_panelEnergySystemTreeTitle, 0, wx.EXPAND, 0 )
        
        self.m_treeCtrl = wx.TreeCtrl( self.m_panelEnergySystemTree, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        self.m_EnergySystemRoot = self.m_treeCtrl.AddRoot(u"Energy System",-1,-1, None)
        self.m_AssetsBranch = self.m_treeCtrl.AppendItem(self.m_EnergySystemRoot, u"Assets", -1, -1, None)
        self.m_MarketBranch = self.m_treeCtrl.AppendItem(self.m_EnergySystemRoot, u"Market", -1, -1, None)
        self.m_NetworkBranch = self.m_treeCtrl.AppendItem(self.m_EnergySystemRoot, u"Network", -1, -1, None)
        self.m_treeCtrl.ExpandAll()
        bSizerPanelMainEnergySystemTree.Add( self.m_treeCtrl, 1, wx.EXPAND, 0 )


        bSizerMainPanelEnergySystemTree.Add( bSizerPanelMainEnergySystemTree, 1, wx.EXPAND, 0 )


        self.m_panelEnergySystemTree.SetSizer( bSizerMainPanelEnergySystemTree )
        self.m_panelEnergySystemTree.Layout()
        bSizerMainPanelEnergySystemTree.Fit( self.m_panelEnergySystemTree )
        bSizerLeft.Add( self.m_panelEnergySystemTree, 1, wx.EXPAND |wx.ALL, 0 )


        bSizerActiveArea.Add( bSizerLeft, 0, wx.EXPAND, 0 )

#--Centre--#########################################################################################################################################################################################
        bSizerCentral = wx.BoxSizer( wx.VERTICAL )

        self.m_notebookCentral = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # MODELS PANEL
        self.m_panelModels = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerModels = wx.BoxSizer( wx.HORIZONTAL )
        #FIXME #TESTING
        self.bSizerAssetModels = wx.BoxSizer( wx.VERTICAL )
        self.bSizerBuildingModels = wx.BoxSizer( wx.VERTICAL )
        self.bSizerNonDispatchModels = wx.BoxSizer( wx.VERTICAL )
        #TODO add all asset types?
        ##
        bSizerModels.Add(self.bSizerAssetModels)
        bSizerModels.Add(self.bSizerBuildingModels)
        bSizerModels.Add(self.bSizerNonDispatchModels)
        
        self.m_panelModels.SetSizer( bSizerModels )
        self.m_panelModels.Layout()
        bSizerModels.Fit( self.m_panelModels )
        self.m_notebookCentral.AddPage( self.m_panelModels, u"MODELS", False ) # Was true
        
        # PF PANEL
        self.m_panelPF = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerPF = wx.BoxSizer( wx.VERTICAL )
        self.m_panelPF.SetSizer( bSizerPF )
        self.m_panelPF.Layout()
        bSizerPF.Fit( self.m_panelPF )
        self.m_notebookCentral.AddPage( self.m_panelPF, u"PF", False )
        
        # CURVES PANEL
        # self.m_panelCurves = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panelCurves = wx.ScrolledWindow( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_panelCurves.SetAutoLayout(1)
        self.m_panelCurves.SetScrollRate(10,10)
        bSizerCurves = wx.BoxSizer( wx.VERTICAL )

        self.m_curves = wx.BoxSizer(wx.VERTICAL)
        ##TESTING--------------------
        # from numpy import arange, sin, pi
        # t = arange(0.0, 3.0, 0.01)
        # s = sin(2 * pi * t)
        # curves.newgraph(self.m_panelCurves, t, s)
        # curves.newgraph(self.m_panelCurves, t, s)
        ########---------------------      
        bSizerCurves.Add(self.m_curves, 1, wx.ALIGN_CENTER, 0)  
        self.m_panelCurves.SetSizer( bSizerCurves )

        self.m_panelCurves.Layout()
        bSizerCurves.Fit( self.m_panelCurves )
        self.m_notebookCentral.AddPage( self.m_panelCurves, u"CURVES", False )
        #TODO https://stackoverflow.com/questions/10737459/embedding-a-matplotlib-figure-inside-a-wxpython-panel
        

        #DATA PANEL
        self.m_panelDATA = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerData = wx.BoxSizer( wx.VERTICAL )
        
        bSizerDataButtons = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_buttonClearAll = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Clear All", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonClearAll, 0, wx.ALL, 5 )
        
        self.m_buttonAddRow = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Row", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddRow, 0, wx.ALL, 5 )

        self.m_buttonAddColumn = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Column", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddColumn, 0, wx.ALL, 5 )
        bSizerData.Add( bSizerDataButtons, 0, wx.ALIGN_RIGHT, 0 )

        self.m_gridData = wx.grid.Grid( self.m_panelDATA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        #Grid Variables
        Default_Rows = 100
        Default_Columns = 30

        # Grid
        self.m_gridData.CreateGrid( Default_Rows, Default_Columns )
        self.m_gridData.EnableEditing( True )
        self.m_gridData.EnableGridLines( True )
        self.m_gridData.EnableDragGridSize( False )
        self.m_gridData.SetMargins( 0, 0 )

        # Columns
        self.m_gridData.EnableDragColMove( False )
        self.m_gridData.EnableDragColSize( True )
        self.m_gridData.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_gridData.EnableDragRowSize( True )
        self.m_gridData.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_gridData.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizerData.Add( self.m_gridData, 1, wx.EXPAND, 0 )
        
        self.m_panelDATA.SetSizer( bSizerData )
        self.m_panelDATA.Layout()
        bSizerData.Fit( self.m_panelDATA )
        self.m_notebookCentral.AddPage( self.m_panelDATA, u"DATA", False )

        bSizerCentral.Add( self.m_notebookCentral, 1, wx.EXPAND |wx.ALL, 0 )


        bSizerActiveArea.Add( bSizerCentral, 1, wx.EXPAND, 0 )
        
        #declare active file for csv imports
        self.active_file = "data.csv"

#--RIGHT--###########################################################################################################################################################################################
        bSizerRight = wx.BoxSizer( wx.VERTICAL )
        
        # OBJECT PARAMETERS
        
        self.m_panelObjectParameters = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelObjectParameters = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainObjectParameters = wx.BoxSizer( wx.VERTICAL )
        
        # Asset Parameters Panel Title
        self.m_panelObjectParametersTitle = wx.StaticText( self.m_panelObjectParameters, wx.ID_ANY, u"OBJECT PARAMETERS", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE_HORIZONTAL, wx.StaticTextNameStr )
        self.m_panelObjectParametersTitle.SetFont(self.m_titleFont)
        bSizerPanelMainObjectParameters.Add( self.m_panelObjectParametersTitle, 0, wx.EXPAND, 0 )

        self.m_propertyGrid = pg.PropertyGrid(self.m_panelObjectParameters, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE)
        self.m_propertyGrid.SetMinSize( wx.Size( 200,-1 ) )

        bSizerPanelMainObjectParameters.Add( self.m_propertyGrid, 1, wx.EXPAND, 0 )


        bSizerMainPanelObjectParameters.Add( bSizerPanelMainObjectParameters, 1, wx.EXPAND, 0 )


        self.m_panelObjectParameters.SetSizer( bSizerMainPanelObjectParameters )
        self.m_panelObjectParameters.Layout()
        bSizerMainPanelObjectParameters.Fit( self.m_panelObjectParameters )
        bSizerRight.Add( self.m_panelObjectParameters, 1, wx.EXPAND, 0 )

        # ACTIVE ASSET LIST
        self.m_panelActiveAssetList = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelActiveAssetList = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainActiveAssetList = wx.BoxSizer( wx.VERTICAL )

        # Active Assets Panel Title
        self.m_panelActiveAssetListTitle = wx.StaticText( self.m_panelActiveAssetList, wx.ID_ANY, u"ACTIVE OBJECTS", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE_HORIZONTAL, wx.StaticTextNameStr )
        self.m_panelActiveAssetListTitle.SetFont(self.m_titleFont)
        bSizerPanelMainActiveAssetList.Add( self.m_panelActiveAssetListTitle, 0, wx.EXPAND, 0 )

        self.m_ActiveAssetList = wx.ListCtrl( self.m_panelActiveAssetList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT | wx.BORDER_NONE | wx.LC_EDIT_LABELS )
        bSizerPanelMainActiveAssetList.Add( self.m_ActiveAssetList, 1, wx.EXPAND, 0 )


        bSizerMainPanelActiveAssetList.Add( bSizerPanelMainActiveAssetList, 1, wx.EXPAND, 0 )


        self.m_panelActiveAssetList.SetSizer( bSizerMainPanelActiveAssetList )
        self.m_panelActiveAssetList.Layout()
        bSizerMainPanelActiveAssetList.Fit( self.m_panelActiveAssetList )
        bSizerRight.Add( self.m_panelActiveAssetList, 1, wx.EXPAND, 0 )


        bSizerActiveArea.Add( bSizerRight, 0, wx.EXPAND, 0 )


        bSizerMainFrame.Add( bSizerActiveArea, 1, wx.EXPAND, 5 )


        bSizerFrameMain.Add( bSizerMainFrame, 1, wx.ALL|wx.EXPAND, 0 )


        self.SetSizer( bSizerFrameMain )
        self.Layout()
        
#--StatusBar--###########################################################################################################################################################################################
        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )
        self.m_statusBar.SetFieldsCount(2)
        self.m_statusBar.SetStatusText("Active Project: "+self.active_project_name+" | Located at: "+self.active_project_path, 0)
        self.m_statusBar.SetStatusText("OPEN GUI Alpha v0.01", 1)
        
#--MENU--###########################################################################################################################################################################################
        self.m_menuBar = wx.MenuBar( 0 )
    #File ---------------------------------
        #TODO make these "New -> Something" create a file in the UserData folder
        self.m_menuFile = wx.Menu()
        
        self.m_subMenuNew = wx.Menu()
        self.m_MenuItemProject = wx.MenuItem( self.m_subMenuNew, wx.ID_ANY, u"Project", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuNew.Append( self.m_MenuItemProject )
        self.m_MenuItemAsset = wx.MenuItem( self.m_subMenuNew, wx.ID_ANY, u"Asset", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuNew.Append( self.m_MenuItemAsset )
        self.m_MenuItemMarket = wx.MenuItem( self.m_subMenuNew, wx.ID_ANY, u"Market", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuNew.Append( self.m_MenuItemMarket )
        
        self.m_menuFile.AppendSubMenu( self.m_subMenuNew, u"New" )

        self.m_menuQuit = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menuFile.Append( self.m_menuQuit )

        self.m_menuBar.Append( self.m_menuFile, u"File" )

    #Data ---------------------------------------------------
        self.m_menuData = wx.Menu()
        
        self.m_subMenuSave = wx.Menu()
        self.m_MenuItemProjectData = wx.MenuItem( self.m_subMenuSave, wx.ID_ANY, u"Save Project Data", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuSave.Append( self.m_MenuItemProjectData )
        self.m_DataSave = wx.MenuItem( self.m_subMenuSave, wx.ID_ANY, u"Save Grid Data", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuSave.Append( self.m_DataSave )
        self.m_menuData.AppendSubMenu( self.m_subMenuSave, u"Save" )

        self.m_subMenuLoad = wx.Menu()
        self.m_MenuItemLoadProject = wx.MenuItem( self.m_subMenuLoad, wx.ID_ANY, u"Load Project", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuLoad.Append( self.m_MenuItemLoadProject )
        self.m_DataLoad = wx.MenuItem( self.m_subMenuLoad, wx.ID_ANY, u"Load Selected File", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuLoad.Append( self.m_DataLoad )
        self.m_menuData.AppendSubMenu( self.m_subMenuLoad, u"Load" )
        
        
        #TODO FINISH SETTING UP SUBMENUS FOR LOADING AND SAVING DATA

        # self.m_DataImport = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL )
        # self.m_menuData.Append( self.m_DataImport )

        # self.m_DataExport = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL )
        # self.m_menuData.Append( self.m_DataExport )

        self.m_menuBar.Append( self.m_menuData, u"Data" )

    #Run --------------------------------------------------------
        self.m_menuRun = wx.Menu()
        self.m_subMenuSimulation = wx.Menu()
        self.m_menuItemOPENTest = wx.MenuItem( self.m_subMenuSimulation, wx.ID_ANY, u"OPEN Test", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuSimulation.Append( self.m_menuItemOPENTest )

        self.m_menuRun.AppendSubMenu( self.m_subMenuSimulation, u"Run Simulation" )

        self.m_menuBar.Append( self.m_menuRun, u"Run")

    #Help -------------------------------------------------------
        self.m_menuHelp = wx.Menu()
        self.m_videoTutorials = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"Video Tutorials (Opens in Default Browser)", "https://gregorjmathieson.github.io/OPEN_GUI_Devlog/webhelp.html", wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_videoTutorials )
        
        self.m_OPENDocs = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"OPEN Documentation", "https://open-platform-for-energy-networks.readthedocs.io/en/latest/api_reference.html", wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_OPENDocs )
        
        self.m_reportIssue = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"Report an Issue (Opens in Default Browser)", "https://github.com/gregorjmathieson/OPENGUI/issues/new", wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_reportIssue )

        self.m_menuBar.Append( self.m_menuHelp, u"Help")


        self.SetMenuBar( self.m_menuBar )


        self.Centre( wx.BOTH )
        #TODO have a show info event for the asset list


#--EVENTS--###########################################################################################################################################################################################

        #TODO correctly make events for saving and loading data. Note save project data should save EVERY OBJECT in .open files.
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.m_dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.changeActiveDirectory, )
        self.m_userLibrary.Bind( wx.EVT_DIRCTRL_FILEACTIVATED, self.loadData )
        self.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.branchSelect, self.m_treeCtrl )
        # self.m_notebookCentral.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.updateCurves )
        self.m_buttonClearAll.Bind( wx.EVT_BUTTON, self.clearGrid )
        self.m_buttonAddRow.Bind( wx.EVT_BUTTON, self.addRow )
        self.m_buttonAddColumn.Bind( wx.EVT_BUTTON, self.addColumn )
        self.Bind( pg.EVT_PG_CHANGED, self.updateParams, id = self.m_propertyGrid.GetId() )
        self.m_ActiveAssetList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.listItemSelected )
        self.Bind( wx.EVT_MENU, self.createNewProject, id = self.m_MenuItemProject.GetId() )
        self.Bind( wx.EVT_MENU, self.createNewAsset, id = self.m_MenuItemAsset.GetId() )
        self.Bind( wx.EVT_MENU, self.createNewMarket, id = self.m_MenuItemMarket.GetId() )
        self.Bind( wx.EVT_MENU, self.shutDown, id = self.m_menuQuit.GetId() )
        self.Bind( wx.EVT_MENU, self.loadData, id = self.m_DataLoad.GetId() )
        self.Bind( wx.EVT_MENU, self.loadProject, id = self.m_MenuItemLoadProject.GetId() )
        self.Bind( wx.EVT_MENU, self.saveProject, id = self.m_MenuItemProjectData.GetId() )
        self.Bind( wx.EVT_MENU, self.saveData, id = self.m_DataSave.GetId() )
        # self.Bind( wx.EVT_MENU, self.loadData, id = self.m_DataLoad.GetId() )
        # self.Bind( wx.EVT_MENU, self.importData, id = self.m_DataImport.GetId() )
        # self.Bind( wx.EVT_MENU, self.exportData, id = self.m_DataExport.GetId() )
        self.Bind( wx.EVT_MENU, self.runOPENTest, id = self.m_menuItemOPENTest.GetId() )
        self.Bind( wx.EVT_MENU, self.videoTutorials, id = self.m_videoTutorials.GetId() )
        self.Bind( wx.EVT_MENU, self.OPENDocs, id = self.m_OPENDocs.GetId() )
        self.Bind( wx.EVT_MENU, self.reportIssue, id = self.m_reportIssue.GetId() )

    def __del__( self ):
        pass
    
    def on_close(self, event):
        """Closes the application

        """
        self.Destroy()
        sys.exit(0)

    # Virtual event handlers, override them in your derived class
    def changeActiveDirectory( self, event ):
        """Changes the active directory of the file tree.
        
        Opens the file explorer dialogue on the user's computer and copies that
        path to the path of the file tree.

        """
        
        print(self.directory)
        new_directory = self.m_dirPicker.GetPath()
        self.directory = new_directory
        self.m_userLibrary.SetPath(new_directory)
        self.m_userLibrary.Layout()
        self.m_userLibrary.FitInside()
        print(self.directory)
        event.Skip()
        
    def changeActiveProject (self, event ):
        """Changes the Active Project.

        """
        #FIXME MAKE SURE THIS WORKS PROPERLY
        
        self.active_file = self.m_userLibrary.GetFilePath() #selected in ctrl
        self.m_statusBar.SetStatusText(self.active_file)
        event.Skip()
    
    def branchSelect( self, event ):
        """Populates the Asset table with the assets of the selected branch.
        
        The actively selected branch of the energy system tree will have its
        active assets displayed on the active asset list.

        """
        active = self.m_treeCtrl.GetItemText(event.GetItem())
        column = self.m_ActiveAssetList.GetSize()[0] /2 - 2
        print(f"Clicked on: {active}")
        AssetList.populateAssetList(self, active, column)
        self.m_propertyGrid.Clear()
        event.Skip()
    
    def refreshModels( self ):
        pass
        # theBitmap = wx.Bitmap("power-plant.png")
        # bitmap = wx.StaticBitmap(self, -1, bitmap=theBitmap, pos=wx.DefaultPosition, size=(20,20))
        # self.bSizerAssetModels.Clear()
        # self.bSizerBuildingModels.Clear()
        # self.bSizerNonDispatchModels.Clear()
        # for asset in AssetList.ActiveAsset.active_assets:
        #     print("hey")
        #     if asset.asset_type == "Asset":
        #         self.bSizerAssetModels.Add(bitmap, 1, wx.EXPAND, 0)
        #         # self.m_panelModels.Layout()
        #         # self.m_panelModels.FitInside()
        #     elif asset.asset_type == "Building":
        #         print("here1")
        #         self.bSizerBuildingModels.Add(bitmap, 1, wx.EXPAND, 0)
        #         # self.m_panelModels.Layout()
        #         # self.m_panelModels.FitInside()
        #     elif asset.asset_type == "NonDispatch":
        #         print("here2")
        #         self.bSizerNonDispatchModels.Add(bitmap, 1, wx.EXPAND, 0)
        #         # self.m_panelModels.Layout()
        #         # self.m_panelModels.FitInside()
        #     else:
        #         pass

    def clearGrid( self, event ):
        """The data grid will be cleared of all text.

        """
        
        self.m_gridData.ClearGrid()
        event.Skip()
    
    def addRow( self, event ):
        """A row will be added to the data grid.

        """
        
        self.m_gridData.AppendRows()
        event.Skip()

    def addColumn( self, event ):
        """A column will be added to the data grid.

        """
        
        self.m_gridData.AppendCols()
        event.Skip()
        
    def updateParams(self, event):
        """The parameters of an asset will be updated.
        
        Whenever any parameter of an asset is edited in the active asset
        parameter list, the values will be refreshed and stored within 
        the local memory.

        """
        
        prop = event.GetProperty()
        label = prop.GetLabel()
        value = prop.GetValue()
        item = self.m_ActiveAssetList.GetFocusedItem() #active asset in list
        active = self.m_ActiveAssetList.GetItemText(item, col=1)
        # print(type(value))
        AssetList.updateParam(label,value,item,active)
        event.Skip()

    def listItemSelected( self, event ):
        """Populates the parameter list with the parameters of the selected asset.
        
        Whenever an asset (or object) is selected from the active assets list,
        its parameters will be displayed on the active asset parameters list.

        """
        
        item = self.m_ActiveAssetList.GetFocusedItem() #active asset in list
        active = self.m_ActiveAssetList.GetItemText(item, col=1)
        AssetList.populateParameterList(self, item, active)
        self.refreshModels()
        event.Skip()

    def createNewProject( self, event ):
        """Creates a new Project.
        
        A new project contains an Energy system, with directories within the
        energy system for storing objects, such as Assets, Markets, and Network Objects.
        The new project will be created within the UserData directory.

        """
        # User input to get project name
        a = Dialogues.NewProjectDialogue(self)
        print(a.ShowModal())
        
        # Creates new Standard Project with user inputted name
        new_project_path = os.getcwd() + r"/UserData/" + a.name
        os.mkdir(new_project_path)
        os.mkdir(new_project_path+r"/ENERGY_SYSTEM")
        os.mkdir(new_project_path+r"/ENERGY_SYSTEM/ASSETS")
        os.mkdir(new_project_path+r"/ENERGY_SYSTEM/MARKET")
        os.mkdir(new_project_path+r"/ENERGY_SYSTEM/NETWORK")
        os.mkdir(new_project_path+r"/SIMULATIONS")
        print("Project " + a.name + " created at " + new_project_path)
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        
        # Display active project on status bar
        self.m_statusBar.SetStatusText("Active Project: "+a.name+" | Located at: "+new_project_path)
        self.active_project_name = a.name
        self.active_project_path = new_project_path
        
        # Set project path in the user library
        self.m_userLibrary.SetPath(self.active_project_path)
        
        event.Skip()
    
    def createNewAsset( self, event ):
        """Opens the dialogue for creating a new asset.
        
        Once the items in the dialogue have been selected by the user,
        a new asset is selected and sent to the active asset list.

        """
        
        a = Dialogues.NewAssetDialogue(self)
        print(a.ShowModal())
        column = self.m_ActiveAssetList.GetSize()[0] /2 - 2
        AssetList.populateAssetList(self, "Assets", column)
        #TODO make sure this stuff is stored in files!
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        event.Skip()
    
    def createNewMarket( self, event ):
        """Creates a new Market Object.
        
        Creates a Market Object with arbitrary default parameters.

        """
        
        AssetList.ActiveMarket("Active Market")
        column = self.m_ActiveAssetList.GetSize()[0] /2 - 2
        AssetList.populateAssetList(self, "Market", column)
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        event.Skip()
        
    def shutDown( self, event):
        """Closes the application

        """
        
        self.Close()
        event.Skip()

    def saveProject(self, event):
        """Saves all instatiated objects in the ENERGY_SYSTEM Directory.

        Calls on the function SaveData.saveObject() for every asset and market in the project.
        """
        
        #TODO add markets and network
        for asset in AssetList.ActiveAsset.active_assets:
            saveObject(asset.asset, asset.name, self.active_project_path, "Asset")
        
        for market in AssetList.ActiveMarket.active_markets:
            saveObject(market.market, market.name, self.active_project_path, "Market")
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        
        event.Skip()

    def saveData( self, event ):
        """Saves the data in the grid as a .txt or .xml file,
        depending on user choice from a pop-up window.

        """
        
        #take active file as default save name
        default_name = self.active_file.rsplit('\\', 1)[-1]   
        default_name = default_name.rsplit('.', 1)[0]
        print(default_name)

        #take user input
        a = Dialogues.SaveDialogue(self, default_name)
        print(a.ShowModal())
        
        #need a variable for rows and columns first... For now test with local variables:
        rows = self.m_gridData.GetNumberRows()
        columns = self.m_gridData.GetNumberCols()
        outputdata = []
        inputdata = []
        for row in range(rows):
            for column in range(columns):
                # if self.m_gridData.GetCellValue(row, column) != "":
                inputdata.append(self.m_gridData.GetCellValue(row, column))
            outputdata.append(list(inputdata))
            inputdata = []
        # print(outputdata)
        print(a.name)
        writeToCSV(outputdata, a.name, a.filetype) #should have a dialogue here that displays what the filename is
        #also, is it possible to change the directory that it saves in? Eventually there should be a DATA folder...
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        
        #Set selected folder to SaveData
        new_directory = os.getcwd() + r"\SaveData\data.csv"
        self.m_userLibrary.SetPath(new_directory)
        self.m_userLibrary.Layout()
        self.m_userLibrary.FitInside()
        #FIXME Make sure user library is refreshed!!!!
        event.Skip()

    def loadProject( self, event=None ):
        """Loads the entire project from projects in UserData directory.

        Args:
            event (_type_): _description_
        """
        
        a = Dialogues.ActiveProjectDialogue(self)
        print(a.ShowModal())
        project = a.item
        
        # Display active project on status bar
        new_project_path = os.getcwd() + r"/UserData/" + project
        self.m_statusBar.SetStatusText("Active Project: "+project+" | Located at: "+new_project_path)
        self.active_project_name = project
        self.active_project_path = new_project_path
        
        # Set project path in the user library
        self.m_userLibrary.SetPath(self.active_project_path)
        
        # LOAD ALL OBJECTS IN ENERGY_SYSTEM
        #----------------------------------
        energy_system_path = new_project_path + "/ENERGY_SYSTEM/"
        
        # ASSETS
        AssetList.ActiveAsset.clear() # clear existing assets
        assets_path = energy_system_path + "ASSETS/"
        assets = os.listdir(assets_path)
        for asset in assets:
            loadObject(asset, assets_path, "Asset")
        
        # MARKETS
        AssetList.ActiveMarket.clear() # clear existing assets
        market_path = energy_system_path + "MARKET/"
        markets = os.listdir(market_path)
        for market in markets:
            loadObject(market, market_path, "Market")
            
        
        #TODO Have some way of refreshing everything
        # event.Skip()
        
    def loadData( self, event ):
        """Loads data from selected file into the data grid.

        """
        
        #Data to be loaded
        self.active_file = self.m_userLibrary.GetFilePath()
        loadeddata = readFromCSV(self.active_file)
        # loadeddata = readFromCSV("data")
        if loadeddata == None: return
        
        #Confirmation
        #TODO Check if empty
        text = "Load file: \n" + str(self.active_file) + "?"
        b = Popups.GenericConfirmation(text)
        print(b.ShowModal())
        
        if b.choice == True:
            #Loading
            rows = self.m_gridData.GetNumberRows()
            columns = self.m_gridData.GetNumberCols()
            itemsinrowlist = [len(x) for x in loadeddata if x] # list of active cell count per row in loaded data
            rowsused = len(itemsinrowlist) # number of active rows in the loaded data
            columnsused = itemsinrowlist[0] # number of active columns in the loaded data

            #while loop to make sure normal grid is big enough.
            while (rows < rowsused):
                self.m_gridData.AppendRows()
                rows = self.m_gridData.GetNumberRows()

            while (columns < columnsused):
                self.m_gridData.AppendCols()
                columns = self.m_gridData.GetNumberCols()

            for column in range(columnsused):
                data = [item[column] for item in loadeddata if item]
                for row in range(rowsused): 
                    try:
                        gotdata = data[row] #defined a data thing here for error handling
                    except IndexError:
                        gotdata = ''
                    if not data[row]: #Do I still need this???
                        self.m_gridData.SetCellValue(row, column, "")
                    else:
                        self.m_gridData.SetCellValue(row, column, str(gotdata))

            self.m_notebookCentral.ChangeSelection(3)
            #task complete
            b = Popups.GenericTaskComplete(self)
            print(b.ShowModal())
        else:
            pass
        event.Skip()

    # def importData( self, event ):
    #     event.Skip()

    # def exportData( self, event ):
    #     event.Skip()
    
    def updateCurves(self):
        """Prints the plots from OPEN simulation into the curves tab of the main canvas.

        """
        
        self.m_curves.Clear()
        # self.m_curves.Destroy()
        for plot in curves.plots:
            print(plot)
            self.m_curves.Add(plot, 1, wx.ALL, 5)
            plot.draw()
        # self.Layout()
        # self.Update()
        self.m_panelCurves.Layout()
        self.m_panelCurves.FitInside()
        self.refreshModels()
        # event.Skip()

    def runOPENTest( self, event ):
        """Runs the building_test.py simulation. 
        
        Currently the only simulation interaction with OPEN.

        """
        
        # Here we import network settings
        # ex: StaticText int(voltage) str(name) for each
        ##Bus1 vn_kv name
        #pass this through to the dialogue... is that possible?
        for asset in AssetList.ActiveAsset.active_assets:
            Dialogues.OPENTestDialogue.assets.append(asset.asset)
        for market in AssetList.ActiveMarket.active_markets:
            Dialogues.OPENTestDialogue.markets.append(market.market)
        a = Dialogues.OPENTestDialogue(self, self.m_panelCurves, self.m_curves)
        print(a.ShowModal())
        self.updateCurves()
        self.refreshModels()
        
        #task complete
        b = Popups.GenericTaskComplete(self)
        print(b.ShowModal())
        event.Skip()
    
    def videoTutorials( self, event ):
        """Opens the video tutorials wep page in the user's default browser.

        """
        
        link("https://gregorjmathieson.github.io/OPEN_GUI_Devlog/webhelp.html")
        event.Skip()
    
    def OPENDocs( self, event ):
        """Opens the OPEN documentation on the internal web viewer.

        """
        
        web = Dialogues.WebHelpDialogue(self).Show()
        print(web)
        event.Skip()
        
    def reportIssue( self, event ):
        """Opens the GitHub "report an issue" page for OPENGUI.

        """
        
        link("https://github.com/EsaLaboratory/OPENGUI/issues/new")
        event.Skip()
    
    


#run the program
app = wx.App()
frame = frameMain(None)
frame.Show()
frame.Maximize(True)
frame.loadProject()
app.MainLoop()