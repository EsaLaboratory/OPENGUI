# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
###########################################################################

import os
# from this import d
from SaveData import readFromCSV, writeToCSV
import wx
import wx.xrc
import wx.grid
import wx.propgrid as pg
from wx import html2

#Dialogues
import Dialogues
import Popups

# #OPEN
# import building_test

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


        bSizerMainPanelUserLibrary.Add( bSizerPanelMainUserLibrary, 1, wx.EXPAND, 0 )


        self.m_panelUserLibrary.SetSizer( bSizerMainPanelUserLibrary )
        self.m_panelUserLibrary.Layout()
        bSizerMainPanelUserLibrary.Fit( self.m_panelUserLibrary )
        bSizerLeft.Add( self.m_panelUserLibrary, 1, wx.ALL|wx.EXPAND, 0 )

        self.m_panelOPENLibrary = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanelOPENLibrary = wx.BoxSizer( wx.VERTICAL )

        bSizerPanelMainOPENLibrary = wx.BoxSizer( wx.VERTICAL )

        self.m_treeCtrl = wx.TreeCtrl( self.m_panelOPENLibrary, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizerPanelMainOPENLibrary.Add( self.m_treeCtrl, 1, wx.EXPAND, 0 )


        bSizerMainPanelOPENLibrary.Add( bSizerPanelMainOPENLibrary, 1, wx.EXPAND, 0 )


        self.m_panelOPENLibrary.SetSizer( bSizerMainPanelOPENLibrary )
        self.m_panelOPENLibrary.Layout()
        bSizerMainPanelOPENLibrary.Fit( self.m_panelOPENLibrary )
        bSizerLeft.Add( self.m_panelOPENLibrary, 1, wx.EXPAND |wx.ALL, 0 )


        bSizerActiveArea.Add( bSizerLeft, 0, wx.EXPAND, 0 )

#--Centre--#########################################################################################################################################################################################
        bSizerCentral = wx.BoxSizer( wx.VERTICAL )

        self.m_notebookCentral = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # MODELS PANEL
        self.m_panelModels = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerModels = wx.BoxSizer( wx.VERTICAL )
        self.m_panelModels.SetSizer( bSizerModels )
        self.m_panelModels.Layout()
        bSizerModels.Fit( self.m_panelModels )
        self.m_notebookCentral.AddPage( self.m_panelModels, u"MODELS", True )
        
        # PF PANEL
        self.m_panelPF = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerPF = wx.BoxSizer( wx.VERTICAL )
        self.m_panelPF.SetSizer( bSizerPF )
        self.m_panelPF.Layout()
        bSizerPF.Fit( self.m_panelPF )
        self.m_notebookCentral.AddPage( self.m_panelPF, u"PF", False )
        
        # CURVES PANEL
        self.m_panelCurves = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerCurves = wx.BoxSizer( wx.VERTICAL )
        self.m_panelCurves.SetSizer( bSizerCurves )
        self.m_panelCurves.Layout()
        bSizerCurves.Fit( self.m_panelCurves )
        self.m_notebookCentral.AddPage( self.m_panelCurves, u"CURVES", False )
        
        #DATA PANEL
        self.m_panelDATA = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerData = wx.BoxSizer( wx.VERTICAL )
        
        bSizerDataButtons = wx.BoxSizer( wx.HORIZONTAL )

        self.m_buttonAddRow = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Row", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddRow, 0, wx.ALL, 5 )

        self.m_buttonAddColumn = wx.Button( self.m_panelDATA, wx.ID_ANY, u"Add Column", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerDataButtons.Add( self.m_buttonAddColumn, 0, wx.ALL, 5 )
        bSizerData.Add( bSizerDataButtons, 0, wx.ALIGN_RIGHT, 0 )

        self.m_gridData = wx.grid.Grid( self.m_panelDATA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        #TODO add a clear all button
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
        
        # PARAMETERS PANEL (Currently just for building case study)
        self.m_panelParams = wx.Panel( self.m_notebookCentral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerParams = wx.BoxSizer( wx.VERTICAL )
        
        # set group title font size
        titlefont = wx.Font( 20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL )
        
        # Initialise Groups
        bParamGroup1 = wx.BoxSizer( wx.VERTICAL )
        bParamGroup2 = wx.BoxSizer( wx.VERTICAL )
        
        # Initialise Rows 3 Parameters per row
        bParamRow1 = wx.BoxSizer( wx.HORIZONTAL )
        bParamRow2 = wx.BoxSizer( wx.HORIZONTAL )
        bParamRow3 = wx.BoxSizer( wx.HORIZONTAL )
        bParamRow4 = wx.BoxSizer( wx.HORIZONTAL )
        bParamRow5 = wx.BoxSizer( wx.HORIZONTAL )
        
        # Building Parameters
        
        self.m_ParamGroupTitle1 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Building Parameters", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_ParamGroupTitle1.SetFont(titlefont)
        self.m_ParamGroupTitle1.Wrap( -1 )
        bParamGroup1.Add( self.m_ParamGroupTitle1, 0, wx.EXPAND, 3)
        
        bParam1 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param1 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Maximum Temperature", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param1.Wrap( -1 )
        bParam1.Add( self.m_Param1, 0, wx.ALL, 3 )
        self.m_Param1Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"18", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam1.Add( self.m_Param1Data, 0, wx.ALL, 0 )
        self.m_Param1Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam1.Add( self.m_Param1Units, 1, wx.ALL, 0 )
        
        bParam2 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param2 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Minimum Temperature", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param2.Wrap( -1 )
        bParam2.Add( self.m_Param2, 0, wx.ALL, 3 )
        self.m_Param2Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"16", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam2.Add( self.m_Param2Data, 0, wx.ALL, 0 )
        self.m_Param2Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam2.Add( self.m_Param2Units, 1, wx.ALL, 0 )

        bParam3 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param3 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Starting Temperature", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param3.Wrap( -1 )
        bParam3.Add( self.m_Param3, 0, wx.ALL, 3 )
        self.m_Param3Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"17", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam3.Add( self.m_Param3Data, 0, wx.ALL, 0 )
        self.m_Param3Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam3.Add( self.m_Param3Units, 1, wx.ALL, 0 )
        
        bParam4 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param4 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Maximum Heating Supplied", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param4.Wrap( -1 )
        bParam4.Add( self.m_Param4, 0, wx.ALL, 3 )
        self.m_Param4Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"90", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam4.Add( self.m_Param4Data, 0, wx.ALL, 0 )
        self.m_Param4Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"kW", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam4.Add( self.m_Param4Units, 1, wx.ALL, 0 )
        
        bParam5 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param5 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Maximum Cooling Supplied", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param5.Wrap( -1 )
        bParam5.Add( self.m_Param5, 0, wx.ALL, 3 )
        self.m_Param5Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam5.Add( self.m_Param5Data, 0, wx.ALL, 0 )
        self.m_Param5Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"kW", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam5.Add( self.m_Param5Units, 1, wx.ALL, 0 )
        
        bParam6 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param6 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Heating Coefficient of Performance", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param6.Wrap( -1 )
        bParam6.Add( self.m_Param6, 0, wx.ALL, 3 )
        self.m_Param6Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam6.Add( self.m_Param6Data, 0, wx.ALL, 0 )
        # self.m_Param6Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bParam6.Add( self.m_Param6Units, 1, wx.ALL, 2 )
        
        bParam7 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param7 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Cooling Coefficient of Performance", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param7.Wrap( -1 )
        bParam7.Add( self.m_Param7, 0, wx.ALL, 3 )
        self.m_Param7Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam7.Add( self.m_Param7Data, 0, wx.ALL, 0 )
        # self.m_Param7Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        # bParam7.Add( self.m_Param7Units, 1, wx.ALL, 2 )

        
        # Market Parameters
        self.m_ParamGroupTitle2 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Market Parameters", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_ParamGroupTitle2.SetFont(titlefont)
        self.m_ParamGroupTitle2.Wrap( -1 )
        bParamGroup2.Add( self.m_ParamGroupTitle2, 0, wx.EXPAND, 3)

        bParam8 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param8 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Net Export Money Received", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param8.Wrap( -1 )
        bParam8.Add( self.m_Param8, 0, wx.ALL, 3 )
        self.m_Param8Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"0.04", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam8.Add( self.m_Param8Data, 0, wx.ALL, 0 )
        self.m_Param8Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"£", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam8.Add( self.m_Param8Units, 1, wx.ALL, 0 )
        
        #TODO make the price of net import variable with time
        bParam9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param9 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Price of Net Imports", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param9.Wrap( -1 )
        bParam9.Add( self.m_Param9, 0, wx.ALL, 3 )
        self.m_Param9Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"0.07", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam9.Add( self.m_Param9Data, 0, wx.ALL, 0 )
        self.m_Param9Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"£", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam9.Add( self.m_Param9Units, 1, wx.ALL, 0 )
        
        bParam10 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param10 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Price per kW for Maximum Demand", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param10.Wrap( -1 )
        bParam10.Add( self.m_Param10, 0, wx.ALL, 3 )
        self.m_Param10Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"0.10", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam10.Add( self.m_Param10Data, 0, wx.ALL, 0 )
        self.m_Param10Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"£", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam10.Add( self.m_Param10Units, 1, wx.ALL, 0 )
        
        bParam11 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param11 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Maximum Import Power", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param11.Wrap( -1 )
        bParam11.Add( self.m_Param11, 0, wx.ALL, 3 )
        self.m_Param11Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"500", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam11.Add( self.m_Param11Data, 0, wx.ALL, 0 )
        self.m_Param11Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"kW", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam11.Add( self.m_Param11Units, 1, wx.ALL, 0 )
        
        bParam12 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_Param12 = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"Maximum Export Power", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_Param12.Wrap( -1 )
        bParam12.Add( self.m_Param12, 0, wx.ALL, 3 )
        self.m_Param12Data = wx.TextCtrl( self.m_panelParams, wx.ID_ANY, u"-500", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam12.Add( self.m_Param12Data, 0, wx.ALL, 0 )
        self.m_Param12Units = wx.StaticText( self.m_panelParams, wx.ID_ANY, u"kW", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParam12.Add( self.m_Param12Units, 1, wx.ALL, 0 )
        
        # Building Parameter Rows
        bParamRow1.Add( bParam1, 1, wx.EXPAND, 0)
        bParamRow1.Add( bParam2, 1, wx.EXPAND, 0)
        bParamRow1.Add( bParam3, 1, wx.EXPAND, 0)
        bParamRow2.Add( bParam4, 1, wx.EXPAND, 0)
        bParamRow2.Add( bParam5, 1, wx.EXPAND, 0)
        bParamRow3.Add( bParam6, 1, wx.EXPAND, 0)
        bParamRow3.Add( bParam7, 1, wx.EXPAND, 0)
        
        # Market Parameter Rows
        bParamRow4.Add( bParam8, 1, wx.EXPAND, 0)
        bParamRow4.Add( bParam9, 1, wx.EXPAND, 0)
        bParamRow4.Add( bParam10, 1, wx.EXPAND, 0)
        bParamRow5.Add( bParam11, 1, wx.EXPAND, 0)
        bParamRow5.Add( bParam12, 1, wx.EXPAND, 0)
        
        #Building Group
        bParamGroup1.Add( bParamRow1, 0, wx.EXPAND, 0 )
        bParamGroup1.Add( bParamRow2, 0, wx.EXPAND, 0 )
        bParamGroup1.Add( bParamRow3, 0, wx.EXPAND, 0 )
        
        #Market Group
        bParamGroup2.Add( bParamRow4, 0, wx.EXPAND, 0 )
        bParamGroup2.Add( bParamRow5, 0, wx.EXPAND, 0 )
        

        
        # Add groups to panel
        bSizerParams.Add( bParamGroup1, 1, wx.EXPAND, 0 )
        bSizerParams.Add( bParamGroup2, 1, wx.EXPAND, 0 )
        
        #Refresh Button
        bParamRefresh = wx.BoxSizer( wx.HORIZONTAL )
        self.m_buttonRefresh = wx.Button( self.m_panelParams, wx.ID_ANY, u"Refresh Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
        bParamRefresh.Add( self.m_buttonRefresh, 0, wx.ALL, 5 )
        bSizerParams.Add( bParamRefresh, 0, wx.ALIGN_RIGHT, 5 )
        
        self.m_panelParams.SetSizer( bSizerParams )
        self.m_panelParams.Layout()
        bSizerParams.Fit( self.m_panelParams )
        
        self.m_notebookCentral.AddPage( self.m_panelParams, u"PARAMETERS", False )
        

        bSizerCentral.Add( self.m_notebookCentral, 1, wx.EXPAND |wx.ALL, 0 )


        bSizerActiveArea.Add( bSizerCentral, 1, wx.EXPAND, 0 )

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
        self.m_buttonRefresh.Bind( wx.EVT_BUTTON, self.refreshParams )
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
        self.m_gridData.AppendRows()
        event.Skip()

    def addColumn( self, event ):
        self.m_gridData.AppendCols()
        event.Skip()
        
    def refreshParams( self, event ):
        a = Dialogues.OPENTestDialogue(self)
        #TODO maybe just having it as one array is hard to read...
        a.parameters[0] = self.m_Param1Data.GetValue()
        a.parameters[1] = self.m_Param2Data.GetValue()
        a.parameters[2] = self.m_Param3Data.GetValue()
        a.parameters[3] = self.m_Param4Data.GetValue()
        a.parameters[4] = self.m_Param5Data.GetValue()
        a.parameters[5] = self.m_Param6Data.GetValue()
        a.parameters[6] = self.m_Param7Data.GetValue()
        a.parameters[7] = self.m_Param8Data.GetValue()
        a.parameters[8] = self.m_Param9Data.GetValue()
        a.parameters[9] = self.m_Param10Data.GetValue()
        a.parameters[10] = self.m_Param11Data.GetValue()
        a.parameters[11] = self.m_Param12Data.GetValue()
        event.Skip()

    def listItemSelected( self, event ):
        event.Skip()

    def createNewAsset( self, event ):
        event.Skip()

    def saveData( self, event ):
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
        print(outputdata)
        writeToCSV(outputdata, "data") #should have a dialogue here that displays what the filename is
        #also, is it possible to change the directory that it saves in? Eventually there should be a DATA folder...
        event.Skip()

    def loadData( self, event ):
        loadeddata = readFromCSV("data")
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
        # Should definitely have a "Done!" pop-up
        event.Skip()

    def importData( self, event ):
        event.Skip()

    def exportData( self, event ):
        event.Skip()

    def runOPENTest( self, event ):
        # Here we import network settings
        # ex: StaticText int(voltage) str(name) for each
        ##Bus1 vn_kv name
        #pass this through to the dialogue... is that possible?
        a = Dialogues.OPENTestDialogue(self)
        print(a.ShowModal())
        event.Skip()
    
    def webHelp( self, event ):
        web = Dialogues.WebHelpDialogue(self).ShowModal()
        print(web)
        event.Skip()


#run the program
app = wx.App()
frame = frameMain(None)
frame.Show()
app.MainLoop()