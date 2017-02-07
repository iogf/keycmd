"""
This module implements basic input data scheme.
"""

from Tkinter import *
from cmdlib.app import root
import string

class DataEvent(object):
    def __init__(self, widget):
        self.widget = widget
        self.widget.bind('<Key>', self.dispatch_data, add=True)

    def dispatch_data(self, event):
        keysym = chr(event.keysym_num)
        self.widget.event_generate('<<Data>>', data=keysym)

class IdleEvent(object):
    def __init__(self, widget):
        self.widget.bind('<<Data>>', self.dispatch_idle, add=True)
        self.widget  = widget
        self.timeout = 400
        self.funcid  = ''

    def dispatch_idle(self, event):
        self.widget.after_cancel(self.funcid)
        self.funcid = self.widget.after(self.timeout, 
        lambda: self.widget.event_generate('<<Idle>>'))

class InputBox(object):
    def __init__(self, area, default_data=''):
        self.default_data = default_data
        self.area    = area
        self.frame   = Frame(root.read_data, border=1, padx=3, pady=3)
        self.entry   = Entry(self.frame)
        self.entry.config(background='grey')
        self.entry.focus_set()
        self.entry.bind('<FocusOut>', lambda event: self.done())
        self.entry.insert('end', default_data)
        self.entry.pack(side='left', expand=True, fill=BOTH)
        self.frame.pack(expand=True, fill=X)

        root.read_data.grid(row=1, sticky='we')

    def done(self):
        self.entry.destroy()
        self.frame.destroy()
        root.read_data.grid_forget()
        self.area.focus_set()

class Get(InputBox, DataEvent, IdleEvent):
    def __init__(self, area, events={}, default_data=''):
        InputBox.__init__(self, area, default_data)
        DataEvent.__init__(self, self.entry)
        IdleEvent.__init__(self, self.entry)

        self.entry.bindtags(('Entry', self.entry, '.', 'all'))
        for indi, indj in events.iteritems():
            self.entry.bind(indi, lambda event, handle=indj: 
                        self.dispatch(handle) , add=True)

    def dispatch(self, handle):
        is_done = handle(self.entry)
        if is_done == True: 
            self.done()

class Ask(InputBox):
    """
    """

    def __init__(self, area, default_data =''):
        InputBox.__init__(self, area, default_data)
        self.entry.bind('<Return>', lambda event: self.on_success())
        self.entry.bind('<Escape>', lambda event: self.done())
        self.data = ''
        self.area.wait_window(self.frame)

    def on_success(self):
        self.data = self.entry.get()
        InputBox.done(self)

    def __str__(self):
        return self.data

    __repr__ = __str__



