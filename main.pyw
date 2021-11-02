from dictobj import DictionaryObject
import main
from gui_main import App
import threading
import time
from gui_node import gui_lock
import gui_node as gui
import wx

lock = threading.Lock()
stopThreads = False
app = App(False)


def loop():
    count = 0
    q = gui.getEventQueue()
    while True:
        with lock:
            if stopThreads:
                break
        time.sleep(0.02)
        try:
            event = gui.getEvent(q)
            control = event.data.control
            print(control.GetName(), control.IsChecked(), event.data.time)
        except:
            pass
        try:
            grid = gui.controlByName("grid")
            st1 = gui.controlByName("st1")
            st2 = gui.controlByName("st2")
            bt1 = gui.controlByName("bt1")
            with gui_lock:
                grid.SetCellValue(5, 7, str(count / 100))
                st1.SetForegroundColour(wx.RED)
                st1.Refresh()
                st1.SetLabelText(str(count * 100))
                st2.SetLabelText(str(count + 100))
                bt1.SetLabelText(str(count * 10))
        except Exception as e:
            # some windows are closed, so we also exit this loop amd shutdown this app
            pass  # break
            print(e)

        # print("LOOP" + str(count))
        count += 1


def loop1():
    count = 1000
    while True:
        with lock:
            if stopThreads:
                break
        time.sleep(0.02)
        try:
            st1 = gui.controlByName("st1")
            with gui_lock:
                st1.SetForegroundColour(wx.BLUE)
                st1.Refresh()
                st1.SetLabelText(str(count * 100))
        except Exception as e:
            # some windows are closed, so we also exit this loop amd shutdown this app
            pass  # break
            print(e)

        # print("LOOP" + str(count))
        count += 1


threading.Thread(target=loop).start()
threading.Thread(target=loop1).start()

app.MainLoop()
# Stop all Threads
with lock:
    stopThreads = True
