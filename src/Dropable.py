'''
Created on 07.05.2012

@author: kapitan Nemo
'''

import wx

class DropablePanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(DropablePanel, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvents)
        self.fDragging = False
        
    def OnMouseEvents(self, e):
        abs_coords = e.GetEventObject().GetPosition() + e.GetPosition()
          
        if(e.LeftDown()):
            for child in e.GetEventObject().GetParent().GetChildren():
                if (child.fDragging):
                    child.fDragging = False
                    break
            e.GetEventObject().fDragging = True;
            e.GetEventObject().SetPosition((abs_coords[0] - e.GetEventObject().GetSize()[0]/2, abs_coords[1] - e.GetEventObject().GetSize()[1]/2))
            
        if(e.LeftUp()):
            for child in e.GetEventObject().GetParent().GetChildren():
                if (child.fDragging):
                    child.fDragging = False
                    break
                
        if(e.Dragging()):
            for child in e.GetEventObject().GetParent().GetChildren():            
                if (child.fDragging):
                    child.SetPosition((abs_coords[0] - child.GetSize()[0]/2, abs_coords[1] - child.GetSize()[1]/2))
                    break


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        mpnl = DropablePanel(self)
        
        pnl = DropablePanel(mpnl, wx.ID_ANY, size = (400, 400), pos = (0, 0), style = wx.BORDER_SIMPLE)
        
        self.dp1 = DropablePanel(pnl, wx.ID_ANY, size = (20, 20), pos = (0, 0), style = wx.BORDER_SIMPLE)
        self.dp1.SetBackgroundColour("BLACK")
        
        self.dp2 = DropablePanel(pnl, wx.ID_ANY, size = (40, 40), pos = (100, 100), style = wx.BORDER_SIMPLE)
        self.dp2.SetBackgroundColour("BLUE")
        
        self.dp3 = DropablePanel(pnl, wx.ID_ANY, size = (60, 60), pos = (100, 100), style = wx.BORDER_SIMPLE)
        self.dp3.SetBackgroundColour("RED")
        
        self.Center()
        self.Show()


App = wx.App()
mw = MainWindow(None, title = "Dropable Panels", size = (600, 600))
App.MainLoop()