
import wx


class InsertFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Frame With Button", size=(300, 200))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Close", pos=(125, 10), size=(50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        print("inside close me now")
        self.Close(True)

    def OnCloseWindow(self, event):
        print("inside close window")
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()