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
    
    def SetPosition(self, pos):
        fFree = True
        
        print pos
        s_lx = pos[0]
        s_rx = pos[0] + self.GetSize()[0]
        s_uy = pos[1]
        s_dy = pos[1] + self.GetSize()[1]
        
        for child in self.GetParent().GetChildren():
            if (self != child):
                p_lx = child.GetPosition()[0]
                p_rx = child.GetPosition()[0] + child.GetSize()[0]
                p_uy = child.GetPosition()[1]
                p_dy = child.GetPosition()[1] + child.GetSize()[1]
                if ((s_rx < p_lx)|(s_lx > p_rx)|(s_dy < p_uy)|(s_uy > p_dy)):
                    pass
                else:
                    fFree = False
            
        if (fFree):
            super(DropablePanel, self).SetPosition(pos)
        
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
                
        e.GetEventObject().GetParent().Refresh()

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        mpnl = DropablePanel(self)
        
        pnl = DropablePanel(mpnl, wx.ID_ANY, size = (400, 400), pos = (0, 0), style = wx.BORDER_SIMPLE)
        
        self.dp1 = DropablePanel(pnl, wx.ID_ANY, size = (30, 30), pos = (0, 0), style = wx.BORDER_SIMPLE)
        self.dp1.SetBackgroundColour("BLACK")
        
        self.dp2 = DropablePanel(pnl, wx.ID_ANY, size = (30, 30), pos = (100, 100), style = wx.BORDER_SIMPLE)
        self.dp2.SetBackgroundColour("BLUE")
        
        self.dp3 = DropablePanel(pnl, wx.ID_ANY, size = (30, 30), pos = (200, 200), style = wx.BORDER_SIMPLE)
        self.dp3.SetBackgroundColour("RED")
        
        self.Center()
        self.Show()


App = wx.App()
mw = MainWindow(None, title = "Dropable Panels", size = (600, 600))
App.MainLoop()