from Tkinter import *

class Ask(Toplevel):
    def __init__(self, view, title, default_data ='', *args, **kwargs):
        self.view = view
        Toplevel.__init__(self, view, *args, **kwargs)

        # self.protocol("WM_DELETE_WINDOW", self.destroy())
        self.bind('<Escape>', lambda event: self.restore_focus_scheme())
        self.bind('<Return>', lambda event: self.ok())
        
        self.title(title)
        self.transient(view)
        self.resizable(width=False, height=False)
        self.frame = Frame(self, relief='raised', border=1,  padx=3, pady=3)
        
        self.entry = Entry(self.frame)

        self.frame.pack(side='top', expand=True, fill=BOTH)
        self.entry.pack(side='left', expand=True, fill=BOTH)

        self.entry.focus_set()

        # It seems that if i put self.data = default_data
        # after self.view.wait_window(self) it sets self.data
        # after it has being set in self.ok then i get
        # the insert mark being reset to insert again.

        self.data = default_data
        self.view.wait_window(self)

    def ok(self):
        self.data = self.entry.get()
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        """ 
        It gives focus back to the view.
        """

        self.view.focus_set()
        self.destroy()

    
if __name__ == '__main__':
    view = Tk()
    search_dialog = Ask(view, 'Ask')
    view.mainloop()






