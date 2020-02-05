import wx
import wx.html

def OnLinkClicked(e):
    wx.TheClipboard.UsePrimarySelection(False)
    if not wx.TheClipboard.Open():
        return
    data = e.GetLinkInfo().GetHref()
    wx.TheClipboard.SetData(wx.TextDataObject(data))
    wx.TheClipboard.Close()
    print("You Clicked:",e.GetLinkInfo().GetHref())
    return

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)

        wx.Frame.__init__(self, parent, -1, title, size=(1000, 600))

        html = wx.html.HtmlWindow(self)

        if "gtk2" in wx.PlatformInfo: 
            html.SetStandardFonts()

            self.textWidget = wx.TextCtrl(self, size=(985, 450), style=wx.TE_MULTILINE)
            self.textWidget.SetMaxLength(0)
            
            displayHTML_button = wx.Button(self, -1,"Display HTML",pos=(500,500)) 

            self.Bind(wx.EVT_BUTTON, self.display_HTML, id = displayHTML_button.GetId())

        def display_HTML(self, e):
            raw_HTML = self.textWidget.GetValue()
            htmlViewerInstance = HtmlViewer(None, raw_HTML)
            htmlViewerInstance.Bind(wx.html.EVT_HTML_LINK_CLICKED,OnLinkClicked)
            htmlViewerInstance.Show()

class HtmlViewer(wx.Frame):
        def __init__(self, parent, raw_HTML):
            wx.Frame.__init__(self, parent, -1, "HTML Viewer", size = (800, 600))

            # Open a new HtmlWindow that is capable of rendering such content
            html = wx.html.HtmlWindow(self)
            
            if "gtk2" in wx.PlatformInfo: 
                html.SetStandardFonts()

            # Load the selected file in the viewer
            html.SetPage(raw_HTML)

app = wx.App()

frm = MyHtmlFrame(None, "HTML viewer")
frm.Bind(wx.html.EVT_HTML_LINK_CLICKED,OnLinkClicked)
frm.Show()

app.MainLoop()
