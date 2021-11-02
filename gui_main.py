"""
Hello World, but with more meat.
"""

import wx
import wx.grid
from gui_grid import GridFrame
import gui_node as gui
from dictobj import DictionaryObject
import winsound

import threading


def sound_nein():
    winsound.PlaySound("Gertis_nein_kurz.wav", winsound.SND_FILENAME)

def sound_ja():
    winsound.PlaySound("Gertis_ja_kurz.wav", winsound.SND_FILENAME)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(MainFrame, self).__init__(*args, **kw)
        self.grid = GridFrame(self, -1)

        # create a panel in the frame
        pnl = wx.Panel(self)

        btn = wx.Button(pnl, name="bt1")
        btn.SetLabelText("Press to show Grid")
        btn.Bind(wx.EVT_BUTTON, self.OnGridButton)

        # put some text with a larger bold font on it
        self.st1 = wx.StaticText(pnl, name="st1", label="Schatzi Morli geht raus an die frische Luft")
        self.st2 = wx.StaticText(pnl, name="st2", label="ohh")
        self.cb1 = wx.CheckBox(pnl, name="cb1", label="Take your choice")
        self.cb2 = wx.CheckBox(pnl, name="cb2", label="Take your second choice")
        self.cb1.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        self.cb2.Bind(wx.EVT_CHECKBOX, self.OnCheckBox)
        font = self.st1.GetFont()
        font.PointSize += 5
        font = font.Bold()
        self.st1.SetFont(font)
        self.st2.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.st1, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        sizer.Add(self.st2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        sizer.Add(self.cb1, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        sizer.Add(self.cb2, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        sizer.Add(btn, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 50))

        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        self.SetSize(800, 500)
        self.OnTimer()

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK | wx.ICON_INFORMATION)

    def OnGridButton(self, event):
        self.grid.Show()
        try:
            threading.Thread(target=sound_ja).start()
            threading.Thread(target=sound_nein).start()
        except:
            pass

    def OnCheckBox(self, event):
        try:
            gui.setEvent(event)
        except:
            raise

    def OnTimer(self):
        wx.CallLater(millis=100, callableObj=self.OnTimer)


class App(wx.App):
    def __init__(self, *args, **kw):
        super(App, self).__init__(*args, **kw)
        self.mainframe = MainFrame(None, -1, name="mainframe")
        print(self.mainframe.GetName())
        self.mainframe.Show()


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = App(False)
    app.MainLoop()
