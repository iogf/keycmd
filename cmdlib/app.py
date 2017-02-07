########## 

from Tkinter import *
import ttk
from ttk import Treeview
import subprocess
from cmdlib.view import *
from cmdlib.statusbar import *
import sys
from os.path import expanduser

# The default directoy path which will be viewed when
# keycmd launches.
DEFAULT_PATH = expanduser("~")

# It points to the root toplevel window of vy. It is the one whose AreaVi instances
# are placed on. 
root = None

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV  = dict()


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Keycmd')        
        self.frame1 = Frame(self, relief = RAISED,
                            padx=3, pady=3,
                            border=3)

    
        self.view = View(DEFAULT_PATH, False, self.frame1, height=20)
        ysb = ttk.Scrollbar(self.frame1, orient='vertical', command=self.view.yview)
        xsb = ttk.Scrollbar(self.frame1, orient='horizontal', command=self.view.xview)
        self.view.configure(yscrollcommand=ysb.set)
        self.view.configure(xscrollcommand=xsb.set)

        ysb.pack(side='right', fill=Y)
        xsb.pack(side='bottom', fill=X)

        self.view.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.view.column('#0', width=500, stretch=True)

        self.view.heading('#0', text='File Name', anchor='w')

        self.view['columns'] = ('permission', 'links', 'owner', 'group', 'size', 'month', 'day', 'hour')

        self.view.heading('permission', text='Permission', anchor='w')
        self.view.column('permission', stretch=True)

        self.view.heading('links', text='Links', anchor='w')
        self.view.column('links', stretch=True)

        self.view.heading('owner', text='Owner', anchor='w')
        self.view.column('owner', stretch=True)

        self.view.heading('group', text='Group', anchor='w')
        self.view.column('group', stretch=True)

        self.view.heading('size', text='Size', anchor='w')
        self.view.column('size', stretch=True)

        self.view.heading('month', text='Month', anchor='w')
        self.view.column('month', stretch=True)

        self.view.heading('day', text='Day', anchor='w')
        self.view.column('day', stretch=True)

        self.view.heading('hour', text='Hour', anchor='w')
        self.view.column('hour', stretch=True)

        self.read_data = Frame(self)

        self.statusbar = StatusBar(self)

        self.view.pack(expand=True, fill=BOTH, side=TOP)
        self.frame1.grid(row=0, sticky='wens')

        self.statusbar.grid(row=2, sticky='we')

        self.view.activate()
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

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)



if __name__ == '__main__':
    app = App()
    app.mainloop()




