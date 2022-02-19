import wx
import building_test
# import CurrentFullCanvas

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
        # #TEST HERE
        # self.variable = 100
        # ####
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"OPEN Simulation Test Parameters", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

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

    #parameters
    parameters = [18,16,17,90,200,3,1,0.04,0.07,0.10,500,-500] #set to default values
    
    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def TestOK( self, event ):
        print(self.parameters)
        #TODO make sure that there is an error case if the voltages aren't numbers!!!
        season, network = self.getData()
        print(season, network)
        #TODO add market and assets input
        market = assets = 0 # for now
        building_test.__main__(season, network, market, assets, self.parameters)
        self.Close()
        event.Skip()

    def getData(self):
        network = []
        season = self.m_SeasonTypeChoice.GetSelection()
        network.append([self.m_TestAttribute1Voltage.GetValue(),self.m_TestAttribute2Voltage.GetValue(),self.m_TestAttribute3Voltage.GetValue()]) #gets the inputted voltages!
        network.append([self.m_TestAttribute1Name.GetValue(),self.m_TestAttribute2Name.GetValue(),self.m_TestAttribute3Name.GetValue()]) #gets the inputted names!
        return season, network
    

##################################################################