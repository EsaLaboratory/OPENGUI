# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
###########################################################################

import os
from SaveData import readFromCSV, writeToCSV
import constant
import wx
import wx.xrc
import wx.grid
import wx.propgrid as pg
from wx import html2

#OPEN
import building_test

###########################################################################
## DIALOGUE
###########################################################################
# Class WebDialogue
#####################
class WebHelpDialogue ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Web Help", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bWebHelpDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bWebHelpDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_WebHelpDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bWebHelpDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bWebHelpDialogueSizer.SetMinSize( wx.Size( 800,800 ) )
        # bWebHelpDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_browser = wx.html2.WebView.New(self)
        self.m_browser.LoadURL("gregorjmathieson.github.io/OPEN_GUI_Devlog/")
        bWebHelpDialogueSizer.Add( self.m_browser, 1, wx.EXPAND, 5)
        
        self.m_CloseOK = wx.Button( self.m_WebHelpDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bWebHelpDialogueSizer.Add( self.m_CloseOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

        self.m_WebHelpDialogueActiveArea.SetSizer( bWebHelpDialogueSizer )
        self.m_WebHelpDialogueActiveArea.Layout()
        bWebHelpDialogueSizer.Fit( self.m_WebHelpDialogueActiveArea )
        bWebHelpDialogueMainFrame.Add( self.m_WebHelpDialogueActiveArea, 1, wx.EXPAND, 5 )


        bWebHelpDialogueFrameMain.Add( bWebHelpDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bWebHelpDialogueFrameMain )
        self.Layout()
        bWebHelpDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_CloseOK.Bind( wx.EVT_BUTTON, self.closeOK)

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def closeOK( self, event ):

        self.Close()
        event.Skip()

# OPENTESTDIAGLOGUE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class OPENTestDialogue ( wx.Dialog ): #remember to come and change these variable names

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"OPEN Simulation Test Parameters", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bNewAssetDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bNewAssetDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_NewAssetDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bNewAssetDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bNewAssetDialogueSizer.SetMinSize( wx.Size( 200,200 ) )
        bNewAssetDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_AssetType = wx.StaticText( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"Season", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_AssetType.Wrap( -1 )

        bNewAssetDialogueRow1.Add( self.m_AssetType, 1, wx.ALL, 0 )

        m_AssetTypeChoiceChoices = ["Summer", "Winter"]
        self.m_AssetTypeChoice = wx.Choice( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AssetTypeChoiceChoices, 0 )
        self.m_AssetTypeChoice.SetSelection( 0 )
        bNewAssetDialogueRow1.Add( self.m_AssetTypeChoice, 1, wx.ALL, 0 )


        bNewAssetDialogueSizer.Add( bNewAssetDialogueRow1, 1, wx.EXPAND, 0 )

        bNewAssetDialogueRow2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_NewAssetAttribute1 = wx.StaticText( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"TBD", wx.DefaultPosition, wx.DefaultSize, 0 ) #Change here
        self.m_NewAssetAttribute1.Wrap( -1 )

        bNewAssetDialogueRow2.Add( self.m_NewAssetAttribute1, 1, wx.ALL, 0 )

        self.m_NewAssetAttribute1Value = wx.TextCtrl( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewAssetDialogueRow2.Add( self.m_NewAssetAttribute1Value, 1, wx.ALL, 0 )


        bNewAssetDialogueSizer.Add( bNewAssetDialogueRow2, 1, wx.EXPAND, 0 )

        bNewAssetDialogueRow3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_NewAssetAttribute2 = wx.StaticText( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"TDB", wx.DefaultPosition, wx.DefaultSize, 0 ) #Change here
        self.m_NewAssetAttribute2.Wrap( -1 )

        bNewAssetDialogueRow3.Add( self.m_NewAssetAttribute2, 1, wx.ALL, 0 )

        self.m_NewAssetAttribute2Value = wx.TextCtrl( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewAssetDialogueRow3.Add( self.m_NewAssetAttribute2Value, 1, wx.ALL, 0 )


        bNewAssetDialogueSizer.Add( bNewAssetDialogueRow3, 1, wx.EXPAND, 0 )

        self.m_NewAssetOK = wx.Button( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewAssetDialogueSizer.Add( self.m_NewAssetOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.m_NewAssetDialogueActiveArea.SetSizer( bNewAssetDialogueSizer )
        self.m_NewAssetDialogueActiveArea.Layout()
        bNewAssetDialogueSizer.Fit( self.m_NewAssetDialogueActiveArea )
        bNewAssetDialogueMainFrame.Add( self.m_NewAssetDialogueActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bNewAssetDialogueFrameMain.Add( bNewAssetDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bNewAssetDialogueFrameMain )
        self.Layout()
        bNewAssetDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_NewAssetOK.Bind( wx.EVT_BUTTON, self.newAssetOK)

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def newAssetOK( self, event ):
        data = self.getData()
        print(data)
        building_test.__main__(data[0])
        self.Close()
        event.Skip()

    def getData(self):
        data = []
        # data.append(self.m_AssetTypeChoice.GetSelection().GetString()) #This doesn't work hmmmm
        data.append(self.m_AssetTypeChoice.GetSelection())
        data.append(self.m_NewAssetAttribute1Value.GetValue())
        data.append(self.m_NewAssetAttribute2Value.GetValue())
        return data

##################################################################

###########################################################################
## Class frameMain
###########################################################################
class frameMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OPEN_CANVAS", pos = wx.DefaultPosition, size = wx.Size( 1555,897 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

        bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

        bSizerActiveArea = wx.BoxSizer( wx.HORIZONTAL )

#--LEFT--############################################################################################################################################################################################
        bSizerLeft = wx.BoxSizer( wx.VERTICAL )

        self.m_panelUserLibrary = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelUserLibrary = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainUserLibrary = wx.BoxSizer( wx.VERTICAL )

    #Here I am using os.getcwd() to get the current directory
        self.m_dirPicker = wx.DirPickerCtrl( self.m_panelUserLibrary, wx.ID_ANY, os.getcwd(), u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizerPanelMainUserLibrary.Add( self.m_dirPicker, 0, 0, 1 )

        self.m_userLibrary = wx.GenericDirCtrl( self.m_panelUserLibrary, wx.ID_ANY, os.getcwd(), wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

        self.m_userLibrary.ShowHidden( False )
        bSizerPanelMainUserLibrary.Add( self.m_userLibrary, 1, wx.EXPAND, 1 )


        bSizerMainPanelUserLibrary.Add( bSizerPanelMainUserLibrary, 1, wx.EXPAND, 5 )


        self.m_panelUserLibrary.SetSizer( bSizerMainPanelUserLibrary )
        self.m_panelUserLibrary.Layout()
        bSizerMainPanelUserLibrary.Fit( self.m_panelUserLibrary )
        bSizerLeft.Add( self.m_panelUserLibrary, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_panelOPENLibrary = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelOPENLibrary = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainOPENLibrary = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl = wx.TreeCtrl( self.m_panelOPENLibrary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizerPanelMainOPENLibrary.Add( self.m_treeCtrl, 1, wx.EXPAND, 0 )


        bSizerMainPanelOPENLibrary.Add( bSizerPanelMainOPENLibrary, 1, wx.EXPAND, 5 )


        self.m_panelOPENLibrary.SetSizer( bSizerMainPanelOPENLibrary )
        self.m_panelOPENLibrary.Layout()
        bSizerMainPanelOPENLibrary.Fit( self.m_panelOPENLibrary )
        bSizerLeft.Add( self.m_panelOPENLibrary, 1, wx.EXPAND |wx.ALL, 5 )


        bSizerActiveArea.Add( bSizerLeft, 0, wx.EXPAND, 5 )

#--Centre--#########################################################################################################################################################################################
        bSizerCentral = wx.BoxSizer( wx.VERTICAL )

        self.m_notebookCentral = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panelModels = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerModels = wx.BoxSizer( wx.VERTICAL )


        self.m_panelModels.SetSizer( bSizerModels )
        self.m_panelModels.Layout()
        bSizerModels.Fit( self.m_panelModels )
        self.m_notebookCentral.AddPage( self.m_panelModels, u"MODELS", True )
        self.m_panelPF = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerPF = wx.BoxSizer( wx.VERTICAL )


        self.m_panelPF.SetSizer( bSizerPF )
        self.m_panelPF.Layout()
        bSizerPF.Fit( self.m_panelPF )
        self.m_notebookCentral.AddPage( self.m_panelPF, u"PF", False )
        self.m_panelCurves = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerCurves = wx.BoxSizer( wx.VERTICAL )


        self.m_panelCurves.SetSizer( bSizerCurves )
        self.m_panelCurves.Layout()
        bSizerCurves.Fit( self.m_panelCurves )
        self.m_notebookCentral.AddPage( self.m_panelCurves, u"CURVES", False )
        self.m_panelDATA = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerData = wx.BoxSizer( wx.VERTICAL )
                
        bSizerDataButtons = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonAddRow = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Row", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddRow, 0, wx.ALL, 5 )

        self.m_buttonAddColumn = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Column", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddColumn, 0, wx.ALL, 5 )


        bSizerData.Add( bSizerDataButtons, 1, wx.ALIGN_RIGHT, 5 )

        self.m_gridData = wx.grid.Grid( self.m_panelDATA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        #Grid Variables
        Rows = 40
        Columns = 15

        # Grid
        self.m_gridData.CreateGrid( Rows, Columns )
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

        bSizerCentral.Add( self.m_notebookCentral, 1, wx.EXPAND |wx.ALL, 5 )


        bSizerActiveArea.Add( bSizerCentral, 1, wx.EXPAND, 5 )

#--RIGHT--###########################################################################################################################################################################################
        bSizerRight = wx.BoxSizer( wx.VERTICAL )

        self.m_panelSelectedAssetAttributes = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelSelectedAssetAttributes = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainSelectedAssetAttributes = wx.BoxSizer( wx.VERTICAL )

        self.m_propertyGrid = pg.PropertyGrid(self.m_panelSelectedAssetAttributes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE)
        self.m_propertyGrid.SetMinSize( wx.Size( 200,-1 ) )

        self.m_propertyGridItem1 = self.m_propertyGrid.Append( pg.StringProperty( u"Name1", u"Name1" ) )
        self.m_propertyGridItem2 = self.m_propertyGrid.Append( pg.StringProperty( u"Name2", u"Name2" ) )
        self.m_propertyGridItem3 = self.m_propertyGrid.Append( pg.StringProperty( u"Name3", u"Name3" ) )
        self.m_propertyGridItem4 = self.m_propertyGrid.Append( pg.StringProperty( u"Name4", u"Name4" ) )
        self.m_propertyGridItem5 = self.m_propertyGrid.Append( pg.StringProperty( u"Name5", u"Name5" ) )
        self.m_propertyGridItem6 = self.m_propertyGrid.Append( pg.StringProperty( u"Name6", u"Name6" ) )
        self.m_propertyGridItem7 = self.m_propertyGrid.Append( pg.StringProperty( u"Name7", u"Name7" ) )
        self.m_propertyGridItem8 = self.m_propertyGrid.Append( pg.StringProperty( u"Name8", u"Name8" ) )
        self.m_propertyGridItem9 = self.m_propertyGrid.Append( pg.StringProperty( u"Name9", u"Name9" ) )
        self.m_propertyGridItem10 = self.m_propertyGrid.Append( pg.StringProperty( u"Name10", u"Name10" ) )
        self.m_propertyGridItem11 = self.m_propertyGrid.Append( pg.StringProperty( u"Name11", u"Name11" ) )
        self.m_propertyGridItem12 = self.m_propertyGrid.Append( pg.StringProperty( u"Name12", u"Name12" ) )
        self.m_propertyGridItem13 = self.m_propertyGrid.Append( pg.StringProperty( u"Name13", u"Name13" ) )
        self.m_propertyGridItem14 = self.m_propertyGrid.Append( pg.StringProperty( u"Name14", u"Name14" ) )
        self.m_propertyGridItem15 = self.m_propertyGrid.Append( pg.StringProperty( u"Name15", u"Name15" ) )
        self.m_propertyGridItem16 = self.m_propertyGrid.Append( pg.StringProperty( u"Name16", u"Name16" ) )
        self.m_propertyGridItem17 = self.m_propertyGrid.Append( pg.StringProperty( u"Name17", u"Name17" ) )
        self.m_propertyGridItem18 = self.m_propertyGrid.Append( pg.StringProperty( u"Name18", u"Name18" ) )
        self.m_propertyGridItem19 = self.m_propertyGrid.Append( pg.StringProperty( u"Name19", u"Name19" ) )
        self.m_propertyGridItem20 = self.m_propertyGrid.Append( pg.StringProperty( u"Name20", u"Name20" ) )
        bSizerPanelMainSelectedAssetAttributes.Add( self.m_propertyGrid, 1, wx.EXPAND, 0 )


        bSizerMainPanelSelectedAssetAttributes.Add( bSizerPanelMainSelectedAssetAttributes, 1, wx.EXPAND, 0 )


        self.m_panelSelectedAssetAttributes.SetSizer( bSizerMainPanelSelectedAssetAttributes )
        self.m_panelSelectedAssetAttributes.Layout()
        bSizerMainPanelSelectedAssetAttributes.Fit( self.m_panelSelectedAssetAttributes )
        bSizerRight.Add( self.m_panelSelectedAssetAttributes, 1, wx.EXPAND, 0 )

        self.m_panelActiveAssetList = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelActiveAssetList = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainActiveAssetList = wx.BoxSizer( wx.VERTICAL )

        self.m_ActiveAssetList = wx.ListCtrl( self.m_panelActiveAssetList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_LIST )
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
        self.m_statusBar = self.CreateStatusBar( 1, wx.STB_DEFAULT_STYLE, wx.ID_ANY )
        self.m_menuBar = wx.MenuBar( 0 )
    #File ---------------------------------
        self.m_menuFile = wx.Menu()
        self.m_subMenuNew = wx.Menu()
        self.m_MenuItemAsset = wx.MenuItem( self.m_subMenuNew, wx.ID_ANY, u"Asset", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_subMenuNew.Append( self.m_MenuItemAsset )

        self.m_menuFile.AppendSubMenu( self.m_subMenuNew, u"New" )

        self.m_Quit = wx.Menu()
        self.m_menuFile.AppendSubMenu( self.m_Quit, u"Quit" )

        self.m_menuBar.Append( self.m_menuFile, u"File" )

    #Data ---------------------------------------------------
        self.m_menuData = wx.Menu()
        self.m_DataSave = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuData.Append( self.m_DataSave )

        self.m_DataLoad = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Load", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuData.Append( self.m_DataLoad )

        self.m_DataImport = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Import", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuData.Append( self.m_DataImport )

        self.m_DataExport = wx.MenuItem( self.m_menuData, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuData.Append( self.m_DataExport )

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
        self.m_webHelp = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"Web Help", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuHelp.Append( self.m_webHelp )

        self.m_menuBar.Append( self.m_menuHelp, u"Help")


        self.SetMenuBar( self.m_menuBar )


        self.Centre( wx.BOTH )

        # Connect Events
        self.m_dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.changeActiveDirectory )
        self.m_buttonAddRow.Bind( wx.EVT_BUTTON, self.addRow )
        self.m_buttonAddColumn.Bind( wx.EVT_BUTTON, self.addColumn )
        self.m_ActiveAssetList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.listItemSelected )
        self.Bind( wx.EVT_MENU, self.createNewAsset, id = self.m_MenuItemAsset.GetId() )
        self.Bind( wx.EVT_MENU, self.saveData, id = self.m_DataSave.GetId() )
        self.Bind( wx.EVT_MENU, self.loadData, id = self.m_DataLoad.GetId() )
        self.Bind( wx.EVT_MENU, self.importData, id = self.m_DataImport.GetId() )
        self.Bind( wx.EVT_MENU, self.exportData, id = self.m_DataExport.GetId() )
        self.Bind( wx.EVT_MENU, self.runOPENTest, id = self.m_menuItemOPENTest.GetId() )
        self.Bind( wx.EVT_MENU, self.webHelp, id = self.m_webHelp.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def changeActiveDirectory( self, event ):
        self.m_userLibrary.SetPath(self.m_dirPicker.GetPath())
        event.Skip()

    def addRow( self, event ):
        self.Rows += 1
        event.Skip()

    def addColumn( self, event ):
        self.Columns += 1
        event.Skip()

    def listItemSelected( self, event ):
        event.Skip()

    def createNewAsset( self, event ):
        event.Skip()

    def saveData( self, event ):
        #need a variable for rows and columns first... For now test with local variables:
        rows = 40
        columns = 15
        outputdata = []
        inputdata = []
        for row in range(rows):
            for column in range(columns):
                if self.m_gridData.GetCellValue(row, column) != "":
                    inputdata.append(self.m_gridData.GetCellValue(row, column))
            outputdata.append(list(inputdata))
            inputdata = []
        print(outputdata)
        writeToCSV(outputdata, "data") #should have a dialogue here that displays what the filename is
        #also, is it possible to change the directory that it saves in? Eventually there should be a DATA folder...
        event.Skip()

    def loadData( self, event ):
        #Possible problem for this method is if there is more data than there are cells available.
        loadeddata = readFromCSV("data")
        itemsinrowlist = [len(x) for x in loadeddata if x]
        columnsused = len(itemsinrowlist)

        for column in range(columnsused):
            data = [item[column] for item in loadeddata if item]
            for row in range(itemsinrowlist[column]): 
                if not data[row]:
                    self.m_gridData.SetCellValue(row, column, "")
                else:
                    self.m_gridData.SetCellValue(row, column, str(data[row]))
        event.Skip()

    def importData( self, event ):
        event.Skip()

    def exportData( self, event ):
        event.Skip()

    def runOPENTest( self, event ):
        a = OPENTestDialogue(self).ShowModal()
        print(a)
        event.Skip()
    
    def webHelp( self, event ):
        web = WebHelpDialogue(self).ShowModal()
        print(web)
        event.Skip()


#run the program
app = wx.App()
frame = frameMain(None)
frame.Show()
app.MainLoop()