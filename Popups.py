import wx
# import CurrentFullCanvas

###########################################################################
## POP-UPS
###########################################################################
#TODO add error dialog
###########################
# Task Complete generic case
###########################
class GenericTaskComplete ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__( self, parent, id = wx.ID_ANY, title = u"Task Complete", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bTaskCompleteDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bTaskCompleteDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_TaskCompleteDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bTaskCompleteDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        # bTaskCompleteDialogueSizer.SetMinSize( wx.Size( 800,400 ) )

        #add static text here
        self.m_label = wx.StaticText(self.m_TaskCompleteDialogueActiveArea, -1, style = wx.ALIGN_CENTER)
        self.m_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        self.m_txt = "Done!"
        self.m_label.SetFont(self.m_font)
        self.m_label.SetLabel(self.m_txt)
        bTaskCompleteDialogueSizer.Add( self.m_label, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_CloseOK = wx.Button( self.m_TaskCompleteDialogueActiveArea, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bTaskCompleteDialogueSizer.Add( self.m_CloseOK, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_TaskCompleteDialogueActiveArea.SetSizer( bTaskCompleteDialogueSizer )
        self.m_TaskCompleteDialogueActiveArea.Layout()
        bTaskCompleteDialogueSizer.Fit( self.m_TaskCompleteDialogueActiveArea )
        bTaskCompleteDialogueMainFrame.Add( self.m_TaskCompleteDialogueActiveArea, 1, wx.EXPAND, 5 )


        bTaskCompleteDialogueFrameMain.Add( bTaskCompleteDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bTaskCompleteDialogueFrameMain )
        self.Layout()
        bTaskCompleteDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_CloseOK.Bind( wx.EVT_BUTTON, self.closeOK)

    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    def closeOK( self, event ):

        self.Close()
        event.Skip()

###########################
# Loading bar generic case
###########################

class GenericLoadingDialogue ( wx.Dialog ): #changed from Dialog

    def __init__( self ): #removing parent here
        # parent = wx.Dialog # None below used to be parent
        wx.Dialog.__init__( self, None, id = wx.ID_ANY, title = u"Task in Progress", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        # wxWindow.Update() #FIXME Text not appearing
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bLoadingDialogueFrameMain = wx.BoxSizer( wx.VERTICAL )

        bLoadingDialogueMainFrame = wx.BoxSizer( wx.VERTICAL )

        self.m_LoadingDialogueActiveArea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bLoadingDialogueSizer = wx.BoxSizer( wx.VERTICAL )

        # bLoadingBarDialogueSizer.SetMinSize( wx.Size( 100,400 ) )

        #add static text here
        self.m_label = wx.StaticText(self.m_LoadingDialogueActiveArea, -1, style = wx.ALIGN_CENTER)
        self.m_font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        self.m_txt = "Loading..."
        self.m_label.SetFont(self.m_font)
        self.m_label.SetLabel(self.m_txt)
        bLoadingDialogueSizer.Add( self.m_label, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_LoadingDialogueActiveArea.SetSizer( bLoadingDialogueSizer )
        self.m_LoadingDialogueActiveArea.Layout()
        bLoadingDialogueSizer.Fit( self.m_LoadingDialogueActiveArea )
        bLoadingDialogueMainFrame.Add( self.m_LoadingDialogueActiveArea, 1, wx.EXPAND, 5 )


        bLoadingDialogueFrameMain.Add( bLoadingDialogueMainFrame, 1, wx.EXPAND, 5 )


        self.SetSizer( bLoadingDialogueFrameMain )
        self.Layout()
        bLoadingDialogueFrameMain.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        # self.Bind( wx.EVT_MOTION, self.onStart)


    def __del__( self ):
        pass

    # Virtual event handlers, override them in your derived class
    # def onStart(self, event):
    #     pass

    # def closeOK( self, event ):

    #     self.Close()
    #     event.Skip()
