"""OPENGUI curves module

The curves module is module containing the logic for processing and displaying output curves for OPENGUI.
This module is called from the simulation file, and will output its curves to the main canvas under "curves" on the central window.

"""

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
    """Class representing the curves panel on the central window.
    
    Output curves from any OPEN simulations are displayed in this window.

    """

    def __init__(self, parent, x1, y1, line1="--", label1="", xlabel="", ylabel="", x2=[], y2=[], line2="--", label2=""):
        wx.Panel.__init__(self, parent)
        """Constructor
        
        Parameters
        -------
        parent
            The parent of the canvas panel (wx.Panel)
        
        x1
            The 1st x axis input array.

        y1
            The 1st y axis input array.

        line1
            The type of line to be displayed for x1/y1 (Default "--" dotted line).

        label1
            The type of label to be displayed for x1/y1 (Default "" no label).

        xlabel
            The x axis label (Default "" no label).

        ylabel
            The y axis label (Default "" no label).

        x2
            The 2nd x axis input array.

        y2
            The 2nd y axis input array.

        line2
            The type of line to be displayed for x2/y2 (Default "--" dotted line).

        label2
            The type of label to be displayed for x2/y2 (Default "" no label).

        """

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
        """Draw function to draw the output curve from the inputted x1/y1 x2/y2 values.
        
        Has no returns, but has internal plot and label functions called to draw the curves and labels.
            
        """

    #     # t = arange(0.0, 3.0, 0.01)
    #     # s = sin(2 * pi * t)
        self.axes.clear()
        self.axes.plot(self.x1, self.y1, self.line1, self.label1)
        self.axes.plot(self.x2, self.y2, self.line2, self.label2)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        

def newgraph(inherit, x1, y1, line1="--", label1="", xlabel="", ylabel="", x2=[], y2=[], line2="--", label2=""):
    """Creates a new graph with the inputted data and adds it to the canvaspanel as a subplot.
    
    #TODO How does this actually work?
    No returns, however the resulting curve is appended to the canvas.
    
    Parameters
    -------
    x1
        The 1st x axis input array.

    y1
        The 1st y axis input array.

    line1
        The type of line to be displayed for x1/y1 (Default "--" dotted line).

    label1
        The type of label to be displayed for x1/y1 (Default "" no label).

    xlabel
        The x axis label (Default "" no label).

    ylabel
        The y axis label (Default "" no label).

    x2
        The 2nd x axis input array.

    y2
        The 2nd y axis input array.

    line2
        The type of line to be displayed for x2/y2 (Default "--" dotted line).

    label2
        The type of label to be displayed for x2/y2 (Default "" no label).
        
    """

    graph = CanvasPanel(inherit, x1, y1, line1, label1, xlabel, ylabel, x2, y2, line2, label2)
    # graph.draw(t, s)
    plots.append(graph)

# print(graph.axes)