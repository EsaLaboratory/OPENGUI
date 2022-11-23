import wx

class MyApp(wx.App):

  def OnInit(self):
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    return True

class InsertFrame(wx.Frame):

  def __init__(self, parent, id):
    wx.Frame.__init__(self, parent, id, 'Test Frame', size = (300,100))
    panel = wx.Panel(self)
    pos_y = 0
    for i in range(5):
      pos_y += 20
      cb = wx.CheckBox(panel, label="sample checkbox", pos=(20, pos_y))

if __name__ == "__main__":
  app = MyApp()
  app.MainLoop()