from subpub import SubPub
import threading
from dictobj import DictionaryObject
import wx
import time

gui_lock = threading.Lock()
internal_lock = threading.Lock()
sp = SubPub()
queue_event = sp.subscribe(r"gui/event(.*)")


def controlByName(name=str()):
    assert type(name) is str, "name is not a string: %r" % name
    with internal_lock:
        control = wx.FindWindowByName(name)
        assert control is not None, "Could not find control: %r " % name
    return control


def getEventQueue():
    return sp.subscribe(r"gui/event(.*)")


def getEvent(queue):
    try:
        return queue.get_nowait()
    except:
        raise


def setEvent(event):
    with internal_lock:
        control = event.GetEventObject()
        name = control.GetName()
        sp.publish(topic="gui/event/" + name,
                   data=DictionaryObject({"control": control, "name": name, "time": time.time()}),
                   retain=False)
