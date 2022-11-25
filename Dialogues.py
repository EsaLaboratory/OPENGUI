"""OPENGUI Dialogues module

The Dialogues module contains all of the dialogue boxes for OPENGUI.
Dialogue boxes are instantiated from the main gui (CurrentFullCanvas) module.

"""

import wx
import building_test
import AssetList as ass
import System.Assets as sys_ass
import numpy as np
import os
# import CurrentFullCanvas

###########################################################################
## DIALOGUE
###########################################################################
####################
# Select Active Project DIALOGUE
####################
class ActiveProjectDialogue ( wx.Dialog ):
    """Dialogue for selecting a project to be the active project.

    """

    def __init__( self, parent ):
        """Constructor
        
        """
        #FIXME Get this dialogue up and running
        
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select Active Project", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        #initialise variables
        self.item = ""

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bNewProjectFrameMain = wx.BoxSizer( wx.VERTICAL )

        bNewProjectMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_NewProjectActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bNewProjectSizer = wx.BoxSizer( wx.VERTICAL )

        bNewProjectSizer.SetMinSize( wx.Size( 200,60 ) )
        # bNewProjectRow1 = wx.BoxSizer( wx.VERTICAL )
        
        # self.m_ProjectAttribute1 = wx.StaticText( self.m_NewProjectActiveArea, wx.ID_ANY, u"Project", wx.DefaultPosition, wx.DefaultSize, 1 )
        # self.m_ProjectAttribute1.Wrap( -1 )

        # bNewProjectRow1.Add( self.m_ProjectAttribute1, 1, wx.ALL, 0 )
        
        # self.m_ProjectAttribute1Value = wx.TextCtrl( self.m_NewProjectActiveArea, wx.ID_ANY, initial, wx.DefaultPosition, wx.DefaultSize, 0 )
        # bNewProjectRow1.Add( self.m_ProjectAttribute1Value, 1, wx.ALL, 0 )
        size = wx.Size(400, 200)
        self.m_ProjectAttribute1Value = wx.ListCtrl( self.m_NewProjectActiveArea, wx.ID_ANY, wx.DefaultPosition, size, wx.LC_REPORT | wx.BORDER_NONE | wx.LC_EDIT_LABELS )
        
        self.m_ProjectAttribute1Value.ClearAll()
        self.m_ProjectAttribute1Value.InsertColumn(0, "Available Projects", wx.LIST_FORMAT_LEFT, 400 )
        
        listfont = self.m_ProjectAttribute1Value.GetFont()
        headfont = listfont.MakeBold()
        headAttr = wx.ItemAttr((0,0,0), (240,240,240), headfont)
        self.m_ProjectAttribute1Value.SetHeaderAttr(headAttr)
        
        #FIXME Add try and exception for sphinx MAYBE UNECESSARY
        try:
            path = os.getcwd() + "/UserData/"
            projects = os.listdir(path)
            for i, project in enumerate(projects):
                print(project)
                a = self.m_ProjectAttribute1Value.InsertItem( i, project )
                print(a)
        except:
            return LookupError
            
        bNewProjectSizer.Add( self.m_ProjectAttribute1Value, 1, wx.ALL, 1 )
        
        # m_FileTypeChoiceChoices = [".csv", ".txt"]

        # self.m_FileTypeChoice = wx.Choice( self.m_NewProjectActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_FileTypeChoiceChoices, 0 )
        # self.m_FileTypeChoice.SetSelection( 0 )
        # bNewProjectRow1.Add( self.m_FileTypeChoice, 1, wx.ALL, 0 )

        # bNewProjectSizer.Add( bNewProjectRow1, 1, wx.EXPAND, 1 )

        self.m_ProjectOK = wx.Button( self.m_NewProjectActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewProjectSizer.Add( self.m_ProjectOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.m_NewProjectActiveArea.SetSizer( bNewProjectSizer )
        self.m_NewProjectActiveArea.Layout()
        bNewProjectSizer.Fit( self.m_NewProjectActiveArea )
        bNewProjectMainFrame.Add( self.m_NewProjectActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bNewProjectFrameMain.Add( bNewProjectMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bNewProjectFrameMain )
        self.Layout()
        bNewProjectFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_ProjectOK.Bind( wx.EVT_BUTTON, self.ProjectOK)

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def ProjectOK( self, event ):
        """Takes the project name and saves the file.
        
        Is activated by clicking the "OK" button in the dialogue.
        Once selected, the data is then sent to a file with the data selected.

        """
        
        # ass.ActiveAsset(str(self.m_ProjectAttribute1Value.GetValue()), self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        # print(self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection()))
        # print(self.m_FileTypeChoice.GetSelection())
        # self.name = self.m_ProjectAttribute1Value.GetValue()
        # self.filetype = self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection())
        focus = self.m_ProjectAttribute1Value.GetFocusedItem()
        self.item = self.m_ProjectAttribute1Value.GetItemText(focus)
        self.Close()
        event.Skip()
        
####################
# New Project DIALOGUE
####################
class NewProjectDialogue ( wx.Dialog ):
    """Dialogue for creating a New Project.

    #TODO
    """

    def __init__( self, parent, initial=""):
        """Constructor
        
        """
        
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Project", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        #initialise variables
        self.name = ""
        # self.filetype = ""

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bNewProjectFrameMain = wx.BoxSizer( wx.VERTICAL )

        bNewProjectMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_NewProjectActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bNewProjectSizer = wx.BoxSizer( wx.VERTICAL )

        bNewProjectSizer.SetMinSize( wx.Size( 200,60 ) )
        bNewProjectRow1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_ProjectAttribute1 = wx.StaticText( self.m_NewProjectActiveArea, wx.ID_ANY, u"Project Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ProjectAttribute1.Wrap( -1 )

        bNewProjectRow1.Add( self.m_ProjectAttribute1, 1, wx.ALL, 0 )
        
        self.m_ProjectAttribute1Value = wx.TextCtrl( self.m_NewProjectActiveArea, wx.ID_ANY, initial, wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewProjectRow1.Add( self.m_ProjectAttribute1Value, 1, wx.ALL, 0 )

        # m_FileTypeChoiceChoices = [".csv", ".txt"]

        # self.m_FileTypeChoice = wx.Choice( self.m_NewProjectActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_FileTypeChoiceChoices, 0 )
        # self.m_FileTypeChoice.SetSelection( 0 )
        # bNewProjectRow1.Add( self.m_FileTypeChoice, 1, wx.ALL, 0 )

        bNewProjectSizer.Add( bNewProjectRow1, 1, wx.EXPAND, 0 )

        self.m_ProjectOK = wx.Button( self.m_NewProjectActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewProjectSizer.Add( self.m_ProjectOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.m_NewProjectActiveArea.SetSizer( bNewProjectSizer )
        self.m_NewProjectActiveArea.Layout()
        bNewProjectSizer.Fit( self.m_NewProjectActiveArea )
        bNewProjectMainFrame.Add( self.m_NewProjectActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bNewProjectFrameMain.Add( bNewProjectMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bNewProjectFrameMain )
        self.Layout()
        bNewProjectFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_ProjectOK.Bind( wx.EVT_BUTTON, self.ProjectOK)

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def ProjectOK( self, event ):
        """Takes the project name and saves the file.
        
        Is activated by clicking the "OK" button in the dialogue.
        Once selected, the data is then sent to a file with the data selected.

        """
        
        # ass.ActiveAsset(str(self.m_ProjectAttribute1Value.GetValue()), self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        # print(self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection()))
        # print(self.m_FileTypeChoice.GetSelection())
        self.name = self.m_ProjectAttribute1Value.GetValue()
        # self.filetype = self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection())
        self.Close()
        event.Skip()

####################
# Save File DIALOGUE
####################
class SaveDialogue ( wx.Dialog ):
    """Dialogue for saving Data.
    
    Contains a method of selecting what file type to save the data as,
    as well as a filename text control box.

    """

    def __init__( self, parent, initial=""):
        """Constructor
        
        """
        
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save Data", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        #initialise variables
        self.name = ""
        self.filetype = ""

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSaveDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bSaveDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_SaveDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSaveDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bSaveDialogueSizer.SetMinSize( wx.Size( 200,60 ) )
        bSaveDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_SaveAttribute1 = wx.StaticText( self.m_SaveDialogueActiveArea, wx.ID_ANY, u"File Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_SaveAttribute1.Wrap( -1 )

        bSaveDialogueRow1.Add( self.m_SaveAttribute1, 1, wx.ALL, 0 )
        
        self.m_SaveAttribute1Value = wx.TextCtrl( self.m_SaveDialogueActiveArea, wx.ID_ANY, initial, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSaveDialogueRow1.Add( self.m_SaveAttribute1Value, 1, wx.ALL, 0 )

        m_FileTypeChoiceChoices = [".csv", ".txt"]

        self.m_FileTypeChoice = wx.Choice( self.m_SaveDialogueActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_FileTypeChoiceChoices, 0 )
        self.m_FileTypeChoice.SetSelection( 0 )
        bSaveDialogueRow1.Add( self.m_FileTypeChoice, 1, wx.ALL, 0 )

        bSaveDialogueSizer.Add( bSaveDialogueRow1, 1, wx.EXPAND, 0 )

        self.m_SaveOK = wx.Button( self.m_SaveDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSaveDialogueSizer.Add( self.m_SaveOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.m_SaveDialogueActiveArea.SetSizer( bSaveDialogueSizer )
        self.m_SaveDialogueActiveArea.Layout()
        bSaveDialogueSizer.Fit( self.m_SaveDialogueActiveArea )
        bSaveDialogueMainFrame.Add( self.m_SaveDialogueActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bSaveDialogueFrameMain.Add( bSaveDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bSaveDialogueFrameMain )
        self.Layout()
        bSaveDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_SaveOK.Bind( wx.EVT_BUTTON, self.saveOK)

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def saveOK( self, event ):
        """Completes the data entry and saves the file.
        
        Is activated by clicking the "OK" button in the dialogue.
        Once selected, the data is then sent to a file with the data selected.

        """
        
        # ass.ActiveAsset(str(self.m_SaveAttribute1Value.GetValue()), self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        print(self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection()))
        # print(self.m_FileTypeChoice.GetSelection())
        self.name = self.m_SaveAttribute1Value.GetValue()
        self.filetype = self.m_FileTypeChoice.GetString(self.m_FileTypeChoice.GetSelection())
        self.Close()
        event.Skip()
        
#####################
# Class WebDialogue
#####################
class WebHelpDialogue ( wx.Dialog ):
    """Dialogue for OPEN Documentation.
    
    Opens the website leading to the OPEN documentation in a window within
    the GUI.

    """

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Web Help", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        # Check if "DONE!" Pop-Up Needed
        self.task_complete = 1
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bWebHelpDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bWebHelpDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_WebHelpDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        # self.m_WebHelpDialogueActiveArea = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        # self.m_WebHelpDialogueActiveArea.SetAutoLayout(1)
        # self.m_WebHelpDialogueActiveArea.SetScrollRate(10,10)
        bWebHelpDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bWebHelpDialogueSizer.SetMinSize( wx.Size( 800,800 ) )
        # bWebHelpDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_browser = wx.html2.WebView.New(self.m_WebHelpDialogueActiveArea)
        # self.m_browser.LoadURL("gregorjmathieson.github.io/OPEN_GUI_Devlog/")
        self.m_browser.LoadURL("https://open-platform-for-energy-networks.readthedocs.io/en/latest/api_reference.html")
        bWebHelpDialogueSizer.Add( self.m_browser, 1, wx.EXPAND, 5)
        
        self.m_CloseOK = wx.Button( self.m_WebHelpDialogueActiveArea, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self.Bind( wx.EVT_CLOSE, self.on_close )

    def __del__( self ):
        pass
    
    def on_close(self, event):
        self.task_complete = 0
        self.Destroy()

    # Virtual event handlers, override them in your derived class
    def closeOK( self, event ):
        """Closes the dialogue.

        """

        self.Close()
        event.Skip()

####################
# NEW ASSET PARAMETERS DIALOGUE
####################
class NewAssetParametersDialogue ( wx.Dialog ):
    """Dialogue for inputting the parameters of a new asset.
    
    Contains text control boxes for each parameter of an asset to be instantiated.

    """
    #TODO Have all of the parameters as inputs on this dialogue depending on the asset type.
    def __init__( self, parent, name, choice ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Asset Parameters", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.name = name
        self.asset_type = ""
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bNewAssetParametersDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bNewAssetParametersDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_NewAssetParametersDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bNewAssetParametersDialogueSizer = wx.BoxSizer( wx.VERTICAL )
        
        #Start here -----------
        #TODO Make this work without repeating AssetList.py(103)
        pos_y = 0
        
        if choice == "Asset":
            # Instantiate asset
            self.asset_type = "Asset"
            self.asset = sys_ass.Asset(0,0,0,0)
            pass
        
        elif choice == "Building":
            # Instantiate asset
            self.asset_type = "BuildingAsset"
            self.asset = sys_ass.BuildingAsset(18,16,90,200,17,500,0.0337,3,1,0,1,1/60,1440,0.25,0.166667)
            pass
        
        elif choice == "Storage":
            # Instantiate asset
            self.asset_type = "StorageAsset"
            self.asset = sys_ass.StorageAsset([0],[0],[0],[0],0.0,0.0,0.0,0.0,0,0.0,0)
            pass
        
        elif choice == "NonDispatch":
            # Instantiate asset
            self.asset_type = "NondispatchableAsset"
            self.asset = sys_ass.NondispatchableAsset(0.0,0.0,0.0,0.0,0)
            pass
        
        elif choice == "Asset (3 phase)":
            # Instantiate asset
            self.asset_type = "Asset_3ph"
            self.asset = sys_ass.Asset_3ph(0.0,[0],0.0,0)
            pass
        
        elif choice == "Storage (3 phase)":
            # Instantiate asset
            self.asset_type = "StorageAsset_3ph"
            self.asset = sys_ass.StorageAsset_3ph([0],[0],[0],[0],0.0,0.0,0.0,[0],0.0,0,0.0,0)
            pass
        
        elif choice == "NonDispatch (3 phase)":
            # Instantiate asset
            self.asset_type = "NondispatchableAsset_3ph"
            self.asset = sys_ass.NondispatchableAsset_3ph(0.0,0.0,0.0,[0],0.0,0)
            pass
        else:
            return TypeError #TODO Proper error handling here pls

        bNewAssetParametersDialogueSizer.SetMinSize( wx.Size( 200,200 ) )
        
        self.boxes = [] # The wx.TextCtrl object for each text box
        for param, value in self.asset.__dict__.items(): # WORKS!!!!!!!!!!!!!
            #TODO add support for arrays etc
            pos_y += 40
            box = wx.BoxSizer( wx.HORIZONTAL )
            label = wx.StaticText(self.m_NewAssetParametersDialogueActiveArea, wx.ID_ANY, label=param, pos=(20,pos_y))
            text = wx.TextCtrl(self.m_NewAssetParametersDialogueActiveArea, wx.ID_ANY, value=str(value), pos=(120,pos_y))
            box.Add(label, 1, wx.ALL, 0)
            box.Add(text, 1, wx.ALL, 0)
            bNewAssetParametersDialogueSizer.Add( box, 1, wx.ALL, 0 )
            self.boxes.append(text)

        self.m_NewAssetOK = wx.Button( self.m_NewAssetParametersDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewAssetParametersDialogueSizer.Add( self.m_NewAssetOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_NewAssetParametersDialogueActiveArea.SetSizer( bNewAssetParametersDialogueSizer )
        self.m_NewAssetParametersDialogueActiveArea.Layout()
        bNewAssetParametersDialogueSizer.Fit( self.m_NewAssetParametersDialogueActiveArea )
        bNewAssetParametersDialogueMainFrame.Add( self.m_NewAssetParametersDialogueActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bNewAssetParametersDialogueFrameMain.Add( bNewAssetParametersDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bNewAssetParametersDialogueFrameMain )
        self.Layout()
        bNewAssetParametersDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_NewAssetOK.Bind( wx.EVT_BUTTON, self.newAssetParamsOK)
        

    def __del__( self ):
        pass
    
    # Virtual event handlers, override them in your derived class
    def newAssetParamsOK( self, event ):
        """Creates a new asset with the selected type and name.

        """

        # Assign values from text boxes to parameters
        for i, (parameter, value) in enumerate(self.asset.__dict__.items()):
            newValue = self.boxes[i].GetValue()
            self.asset.__setattr__(parameter, newValue)
        
        # Instantiate new asset
        ass.ActiveAsset(self.name, self.asset_type, self.asset)
        
        self.Close()
        event.Skip()

##################################################################
####################
# NEW ASSET DIALOGUE
####################
class NewAssetDialogue ( wx.Dialog ):
    """Dialogue for creating a new asset.
    
    Has a drop down menu with different asset types.
    Once an asset type is selected, the name of the asset can also be chosen.
    The asset is instantiated once the OK button is selected.

    """
    #TODO Have all of the parameters as inputs on this dialogue depending on the asset type.
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Asset", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.task_complete = 1
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bNewAssetDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bNewAssetDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_NewAssetDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bNewAssetDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bNewAssetDialogueSizer.SetMinSize( wx.Size( 200,200 ) )
        bNewAssetDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_AssetType = wx.StaticText( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"Asset Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_AssetType.Wrap( -1 )

        bNewAssetDialogueRow1.Add( self.m_AssetType, 1, wx.ALL, 0 )

        m_AssetTypeChoiceChoices = ["Asset", "Building", "Storage", "NonDispatch", "Asset (3 phase)", "Storage (3 phase)", "NonDispatch (3 phase)"]

        self.m_AssetTypeChoice = wx.Choice( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AssetTypeChoiceChoices, 0 )
        self.m_AssetTypeChoice.SetSelection( 0 )
        bNewAssetDialogueRow1.Add( self.m_AssetTypeChoice, 1, wx.ALL, 0 )


        bNewAssetDialogueSizer.Add( bNewAssetDialogueRow1, 1, wx.EXPAND, 0 )

        bNewAssetDialogueRow2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_NewAssetAttribute1 = wx.StaticText( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_NewAssetAttribute1.Wrap( -1 )

        bNewAssetDialogueRow2.Add( self.m_NewAssetAttribute1, 1, wx.ALL, 0 )

        self.m_NewAssetAttribute1Value = wx.TextCtrl( self.m_NewAssetDialogueActiveArea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bNewAssetDialogueRow2.Add( self.m_NewAssetAttribute1Value, 1, wx.ALL, 0 )


        bNewAssetDialogueSizer.Add( bNewAssetDialogueRow2, 1, wx.EXPAND, 0 )

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
        self.Bind( wx.EVT_CLOSE, self.on_close )

    def __del__( self ):
        pass

    def on_close(self, event):
        self.task_complete = 0
        self.Destroy()

    # Virtual event handlers, override them in your derived class
    def newAssetOK( self, event ):
        """Creates a new asset with the selected type and name.

        """
        
        #CALL NEW ASSET PARAMETER DIALOGUE
        a = NewAssetParametersDialogue(self, str(self.m_NewAssetAttribute1Value.GetValue()), self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        print(a.ShowModal())
        
        # ass.ActiveAsset(str(self.m_NewAssetAttribute1Value.GetValue()), self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        # print(self.m_AssetTypeChoice.GetString(self.m_AssetTypeChoice.GetSelection()))
        # print(self.m_AssetTypeChoice.GetSelection())
        self.Close()
        event.Skip()

    # def getData(self):
    #     data = []
    #     # data.append(self.m_AssetTypeChoice.GetSelection().GetString()) #This doesn't work hmmmm
    #     data.append(self.m_AssetTypeChoice.GetSelection())
    #     # data.append(self.m_NewAssetAttribute1Value.GetValue())
    #     # data.append(self.m_NewAssetAttribute1Value.GetValue())
    #     return data

##################################################################
####################
# OPENTESTDIAGLOGUE 
####################
class OPENTestDialogue ( wx.Dialog ): #remember to come and change these variable names
    """Dialogue for running an OPEN simulation.
    
    Does the building case study simulation. Has a drop down menu with
    the ability to select either "summer" or "winter".

    """
    
    assets = []
    markets = []

    def __init__( self, parent, curves_inherit, curve_container ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"OPEN Simulation Test Parameters", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.curves_inherit = curves_inherit
        self.container = curve_container
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bTestDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bTestDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_TestDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bTestDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        bTestDialogueSizer.SetMinSize( wx.Size( 200,200 ) )
        bTestDialogueRow1 = wx.BoxSizer( wx.HORIZONTAL )

        #Season Chooser######
        self.m_SeasonType = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"Season", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_SeasonType.Wrap( -1 )

        bTestDialogueRow1.Add( self.m_SeasonType, 1, wx.ALL, 0 )

        m_SeasonTypeChoiceChoices = ["Summer", "Winter"]
        self.m_SeasonTypeChoice = wx.Choice( self.m_TestDialogueActiveArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_SeasonTypeChoiceChoices, 0 )
        self.m_SeasonTypeChoice.SetSelection( 0 )
        bTestDialogueRow1.Add( self.m_SeasonTypeChoice, 1, wx.ALL, 0 )


        bTestDialogueSizer.Add( bTestDialogueRow1, 1, wx.EXPAND, 0 )
        #####################
        #TODO add for loop implementation so you can have as many buses as you want???
        #TODO add a "more options" button to allow for more attributes to be added (transformer...etc)
        #BUS ATTRIBUTES#######
        # Bus 1 ####
        bTestDialogueRow2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_TestAttribute1 = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"Bus 1", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_TestAttribute1.Wrap( -1 )

        bTestDialogueRow2.Add( self.m_TestAttribute1, 1, wx.ALL, 0 )

        self.m_TestAttribute1Voltage = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, "20.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow2.Add( self.m_TestAttribute1Voltage, 1, wx.ALL, 0 )
        
        self.m_TestAttribute1Units = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"kV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow2.Add( self.m_TestAttribute1Units, 1, wx.ALL, 2 )
        
        self.m_TestAttribute1Name = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, u"BUS 1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow2.Add( self.m_TestAttribute1Name, 1, wx.ALL, 0 )

        bTestDialogueSizer.Add( bTestDialogueRow2, 1, wx.EXPAND, 0 )
        ############
        
        # Bus 2 ####
        bTestDialogueRow3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_TestAttribute2 = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"Bus 2", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_TestAttribute2.Wrap( -1 )

        bTestDialogueRow3.Add( self.m_TestAttribute2, 1, wx.ALL, 0 )
        self.m_TestAttribute2Voltage = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, "0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow3.Add( self.m_TestAttribute2Voltage, 1, wx.ALL, 0 )
        
        self.m_TestAttribute2Units = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"kV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow3.Add( self.m_TestAttribute2Units, 1, wx.ALL, 2 )
        
        self.m_TestAttribute2Name = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, u"BUS 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow3.Add( self.m_TestAttribute2Name, 1, wx.ALL, 0 )

        bTestDialogueSizer.Add( bTestDialogueRow3, 1, wx.EXPAND, 0 )
        ############
        
        # Bus 3 ####
        bTestDialogueRow4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_TestAttribute3 = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"Bus 3", wx.DefaultPosition, wx.DefaultSize, 0 ) 
        self.m_TestAttribute3.Wrap( -1 )

        bTestDialogueRow4.Add( self.m_TestAttribute3, 1, wx.ALL, 0 )
        self.m_TestAttribute3Voltage = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, "0.4", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow4.Add( self.m_TestAttribute3Voltage, 1, wx.ALL, 0 )
        
        self.m_TestAttribute3Units = wx.StaticText( self.m_TestDialogueActiveArea, wx.ID_ANY, u"kV", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow4.Add( self.m_TestAttribute3Units, 1, wx.ALL, 2 )
        
        self.m_TestAttribute3Name = wx.TextCtrl( self.m_TestDialogueActiveArea, wx.ID_ANY, u"BUS 3", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueRow4.Add( self.m_TestAttribute3Name, 1, wx.ALL, 0 )

        bTestDialogueSizer.Add( bTestDialogueRow4, 1, wx.EXPAND, 0 )
        ############
        
        # OK BUTTON #######
        self.m_TestOK = wx.Button( self.m_TestDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTestDialogueSizer.Add( self.m_TestOK, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


        self.m_TestDialogueActiveArea.SetSizer( bTestDialogueSizer )
        self.m_TestDialogueActiveArea.Layout()
        bTestDialogueSizer.Fit( self.m_TestDialogueActiveArea )
        bTestDialogueMainFrame.Add( self.m_TestDialogueActiveArea, 1, wx.EXPAND |wx.ALL, 5 )


        bTestDialogueFrameMain.Add( bTestDialogueMainFrame, 1, wx.EXPAND, 5 )
        ####################

        self.SetSizer( bTestDialogueFrameMain )
        self.Layout()
        bTestDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_TestOK.Bind( wx.EVT_BUTTON, self.TestOK)

    #Default Parameters
    parameters = [18,16,17,90,200,3,1,0.04,0.07,0.10,500,-500] #set to default values
    
    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def TestOK( self, event ):
        """Runs the OPEN simulation once the OK button is selected.

        """
        
        print(self.parameters)
        #TODO make sure that there is an error case if the voltages aren't numbers!!!
        season, network = self.getData()
        print(season, network)
        for asset in OPENTestDialogue.assets:
            print(asset)
        self.Close()
        building_test.__main__(season, network, OPENTestDialogue.markets[0], OPENTestDialogue.assets, self.curves_inherit, self.container)
        event.Skip()

    def getData(self):
        """Receives the data from the OPENTestdialogue.
        
        Takes selection in order to send variables to the simulation file.
        
        Returns
        -------
        season
            The selected season to run the simulation with.
        
        network
            The network array with the names and voltages of each bus in the power system.

        """
        
        network = []
        season = self.m_SeasonTypeChoice.GetSelection()
        network.append([self.m_TestAttribute1Voltage.GetValue(),self.m_TestAttribute2Voltage.GetValue(),self.m_TestAttribute3Voltage.GetValue()]) #gets the inputted voltages!
        network.append([self.m_TestAttribute1Name.GetValue(),self.m_TestAttribute2Name.GetValue(),self.m_TestAttribute3Name.GetValue()]) #gets the inputted names!
        return season, network
    

##################################################################