import wx
import wx.grid

from dictobj import DictionaryObject


class GridFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(GridFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        # Create a wxGrid object
        self.__grid = wx.grid.Grid(pnl, -1, name="grid")

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        self.__grid.CreateGrid(20, 10)

        # We can set the sizes of individual rows and columns
        # in pixels
        self.__grid.SetRowSize(0, 60)
        self.__grid.SetColSize(0, 120)

        # And set grid cell contents as strings
        self.__grid.SetCellValue(0, 0, 'wxGrid is good')

        # We can specify that some cells are read.only
        self.__grid.SetCellValue(0, 3, 'This is read.only')
        self.__grid.SetReadOnly(0, 3)

        # Colours can be specified for grid cell contents
        self.__grid.SetCellValue(3, 3, 'red on grey')
        self.__grid.SetCellTextColour(3, 3, wx.BLACK)
        self.__grid.SetCellBackgroundColour(3, 3, wx.RED)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        self.__grid.SetColFormatFloat(5, 6, 2)
        self.__grid.SetCellValue(0, 6, '3.1415')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__grid, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 2))
        pnl.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # and a status bar
        self.CreateStatusBar()

        self.SetSize(self.__grid.GetBestWidth(0) + 100, self.__grid.GetBestHeight(0) + 100)
        self.SetBackgroundColour(wx.WHITE)

    def OnClose(self, event):
        self.Show(False)


