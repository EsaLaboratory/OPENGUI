from re import S
from numpy import arange, sin, pi
import matplotlib

from AssetList import T
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

import wx

plots = []

class CanvasPanel(wx.Panel):
    def __init__(self, parent, x1, y1, line1="--", label1="", xlabel="", ylabel="", x2=[], y2=[], line2="--", label2=""):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(1,1,1) #was 111
        
        # Put plt stuff here
        # self.figsize1 = figsize1
        self.x1 = x1
        self.y1 = y1
        self.line1 = line1
        self.label1 = label1
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x2 = x2
        self.y2 = y2
        self.line2 = line2
        self.label2 = label2
                
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        
    def draw(self):
    #     # t = arange(0.0, 3.0, 0.01)
    #     # s = sin(2 * pi * t)
        self.axes.clear()
        self.axes.plot(self.x1, self.y1, self.line1, self.label1)
        self.axes.plot(self.x2, self.y2, self.line2, self.label2)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        

def newgraph(inherit, x1, y1, line1="--", label1="", xlabel="", ylabel="", x2=[], y2=[], line2="--", label2=""):
    graph = CanvasPanel(inherit, x1, y1, line1, label1, xlabel, ylabel, x2, y2, line2, label2)
    # graph.draw(t, s)
    plots.append(graph)

# print(graph.axes)