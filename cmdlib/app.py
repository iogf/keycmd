########## 

from Tkinter import *
from ttk import Treeview
import subprocess
from utils import *


# The default directoy path which will be viewed when
# keycmd launches.
DEFAULT_PATH = '/home/tau'


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

        self.view.pack(expand=True, fill=BOTH, side='left')
        self.frame1.pack(expand=True, fill=BOTH, side='left')


        self.view.set_curselection_on()
        self.view.focus_set()

        import cmd
        cmd.load(self.view)



if __name__ == '__main__':
    app = App()
    app.root.mainloop()

























