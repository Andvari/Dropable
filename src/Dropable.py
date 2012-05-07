'''
Created on 07.05.2012

@author: kapitan Nemo
'''

import wx

class DropablePanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(DropablePanel, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvents)
        self.fDragged = False
        
    def OnMouseEvents(self, e):
        if(e.Dragging()):
            if(self.fDragged):
                self.SetPosition(e.GetPosition())
                
            

            
        
        

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.G
        
        self.mpnl = wx.Panel(self)
        
        
        
        
        self.Center()
        self.Show()



App = wx.App()
mw = MainWindow(None, title = "Dropable Panels", size = (600, 600))
App.MainLoop()