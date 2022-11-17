import  wx
#Works!!!!
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.splittermain = wx.SplitterWindow(self)
        self.splittermini = wx.SplitterWindow(self.splittermain)
        
        win1 = wx.Window(self.splittermini)
        bSizerWin1 = wx.BoxSizer( wx.VERTICAL )
        
        win2 = wx.Window(self.splittermini)
        bSizerWin2 = wx.BoxSizer( wx.VERTICAL )
        
        win3 = wx.Window(self.splittermain)
        bSizerWin3 = wx.BoxSizer( wx.VERTICAL )

        pan1 = wx.Panel(win1, style=wx.BORDER_SUNKEN)
        pan1.SetBackgroundColour("yellow")
        text1 = wx.StaticText(pan1, -1, "My Left Panel")
        text2 = wx.StaticText(pan1, -1, "AHHHH")
        bSizerWin1.Add(pan1,1,wx.EXPAND,1)

        pan2 = wx.Panel(win1, style=wx.BORDER_SUNKEN)
        pan2.SetBackgroundColour("orange")
        wx.StaticText(pan2, -1, "my Right Panel")
        bSizerWin1.Add(pan2,1,wx.EXPAND,1)
        
        win1.SetSizer(bSizerWin1)

        pan3 = wx.Panel(win2, style=wx.BORDER_SUNKEN)
        pan3.SetBackgroundColour("blue")
        wx.StaticText(pan3, -1, "my other Panel")
        bSizerWin2.Add(pan3,1,wx.EXPAND,1)
        
        win2.SetSizer(bSizerWin2)
        
        pan4 = wx.Panel(win3, style=wx.BORDER_SUNKEN)
        pan4.SetBackgroundColour("blue")
        wx.StaticText(pan4, -1, "my other Panel1")
        bSizerWin3.Add(pan4,1,wx.EXPAND,1)

        pan5 = wx.Panel(win3, style=wx.BORDER_SUNKEN)
        pan5.SetBackgroundColour("blue")
        wx.StaticText(pan5, -1, "my other Panel2")
        bSizerWin3.Add(pan5,1,wx.EXPAND,1)
        
        win3.SetSizer(bSizerWin3)
        
        self.splittermini.SplitVertically(win1,win2,-100)
        self.splittermain.SplitVertically(self.splittermini, win3, -100)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()