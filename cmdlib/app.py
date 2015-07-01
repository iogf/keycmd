########## 

from Tkinter import *
from ttk import Treeview
import subprocess
from cmdlib.view import *
from cmdlib.statusbar import *
import sys


# The default directoy path which will be viewed when
# keycmd launches.
DEFAULT_PATH = '/home/tau'

# It points to the root toplevel window of vy. It is the one whose AreaVi instances
# are placed on. 
root = None
# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV  = dict()

# A special dict used to execute on the fly python code.
DEV  = dict()


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Keycmd')        
        self.frame1 = Frame(self.root, relief = RAISED,
                            padx=3, pady=3,
                            border=3)

    
        self.view = View(DEFAULT_PATH, False, self.frame1, height=20)
        self.view.column('#0', width=600)
        self.view.heading('#0', text='File Name')

        self.view['columns'] = ('permission', 'owner', 'group', 'size')

        self.view.heading('permission', text='Permission')
        self.view.column('permission', width=100, anchor='center')
        self.view.heading('owner', text='Owner')
        self.view.column('owner', width=100, anchor='center')

        self.view.heading('group', text='Group')
        self.view.column('group', width=100, anchor='center')

        self.view.heading('size', text='Size')
        self.view.column('size', width=100, anchor='center')

        self.frame1.pack(expand=True, fill=BOTH, side=TOP)
        self.statusbar = StatusBar(self.root)

        self.view.pack(expand=True, fill=BOTH, side=TOP)
        self.statusbar.pack(side=BOTTOM, fill=X)

        self.view.set_curselection_on()
        self.view.focus_set()

        global root
        root      = self

        from os.path import expanduser, join, exists, dirname
        from os import mkdir
        from shutil import copyfile
        
        dir = join(expanduser('~'), '.keycmd')
        rc  = join(dir, 'cmdrc')
        
        if not exists(dir):
            mkdir(dir)
        
        if not exists(rc):
            copyfile(join(dirname(__file__), 'cmdrc'), rc)
        
        execfile(rc, ENV)

        from cmdlib.modes import INSTALL, HANDLE

        for mode, args, kwargs in INSTALL:
            mode.install(self.view, *args, **kwargs)

        for handle, args, kwargs in HANDLE:
            handle(self.view, *args, **kwargs)

        self.view.add_mode(1, opt=True)
        self.view.chmode(1)


if __name__ == '__main__':
    app = App()
    app.root.mainloop()




























