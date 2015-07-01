from Tkinter import *

class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.is_on = False
        self.config(border=1)
        self.msg = Label(self, bd=1, relief=SUNKEN, anchor=W)

        self.msg.pack(side='left', expand=True, fill=X)
        self.mode = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.mode.pack(side='right', fill=X)


    def set_msg(self, data):
        self.msg.config(text=data)
        self.msg.update_idletasks()

    def clear_msg(self):
        self.msg.config(text="")
        self.msg.update_idletasks()

    def set_mode(self, mode):
        self.mode.config(text='Mode: %s' % mode)
        self.mode.update_idletasks()

    def pack(self, *args, **kwargs):
        Frame.pack(self, *args, **kwargs)
        self.args   = args
        self.kwargs = kwargs
        self.is_on  = True

    def pack_forget(self):
        Frame.pack_forget(self)
        self.is_on = False

    def switch(self):    
        if self.is_on: self.pack_forget()
        else: self.pack(*self.args, **self.kwargs)






