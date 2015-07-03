from ttk import Treeview
from os.path import exists 
from os.path import join
import os
from nix import *
from re import search


class View(Treeview):
    def __init__(self, default_path, show_hidden, *args, **kwargs):
        """

        """
        Treeview.__init__(self, *args, **kwargs)
        self.setup       = {}
        self.show_hidden = show_hidden

        self.add_view(default_path)
    

    def chmode(self, id):
        """
        This function is used to change the AreaVi instance's mode.
        It receives one parameter named id which means the
        mode number.
        """
        opt     = self.setup[id]
        self.id = id

        MODE_X = 'mode%s-1' % self
        MODE_Y = 'mode%s%s' % (self, id)

        if opt: self.bindtags((MODE_X, MODE_Y, self, 'Treeview', '.'))
        else: self.bindtags((MODE_X, MODE_Y, self, '.'))

    def add_mode(self, id, opt=False):
        """
        It adds a new mode. The opt argument means whether
        it should propagate the event to the internal text widget callbacks.
        """

        self.setup[id] = opt

    def del_mode(self, id):
        """
        It performs the opposite of add_mode.
        """

        del self.setup[id]


    def hook(self, id, seq, callback):
        """
        This method is used to hook a callback to a sequence
        specified with its mode. The standard modes are insert and selection.
        The insert mode prints the key character on the text area.
        """
        MODE_Y = 'mode%s%s' % (self, id)

        self.bind_class(MODE_Y, seq, callback, add=True)


    def unhook(self, id, seq, callback):
        """
        It performs the opposite of unhook.
        """

        pass

    def install(self, *args):
        """
        It is like self.hook but accepts
        a sequence of (id, seq, callback).
        """

        for id, seq, callback in args:
            self.hook(id, seq, callback)

    def uninstall(self, *args):
        """
        Like self.hook but accepts.
        (id, seq, callback).
        """

        for id, seq, callback in args:
            self.unhook(id, seq, callback)


    
    def add_view(self, ph):
        """

        """
        if not os.path.exists(ph): return
        iid = self.insert('', 'end', text=ph, tags=('d', ))

        self.put_view_data(iid)

        self.item(iid, open=True)
        return iid

    def rm_view(self, ph):
        pass

    def change_view(self, iid, ph):
        """

        """
        self.delete_view_data(iid)
        self.item(iid, text=ph)
        self.put_view_data(iid)


    def update_view(self, iid):
        """
        """

        ph = self.get_item_path(iid)

        if exists(ph):  # I should verify if it remains being a dir.
            self.delete_view_data(iid)
            self.put_view_data(iid)
        else:
            self.delete(iid)


    def update_view_list(self):
        """

        """
        for indi in self.get_children(''):
            self.update_view(indi)

    def put_view_data(self, iid):
        """

        """

        ph = self.get_item_path(iid)
        for ind in listdir(ph, self.show_hidden):
            self.insert(iid, 'end', 
                        text=ind[-1], tags=(ind[0][0],),
                        values=(ind[0], ind[2], ind[3], ind[4]))

    def delete_view_data(self, iid):
        """
        """
        self.delete(*self.get_children(iid))

    def get_item_dir(self, iid):
        """
        """

        iidn = self.parent(iid)
        iidn = iidn if iidn else iid
        return iidn
    
    def get_item_path(self, iid):
        """
        """
        iidn = self.parent(iid)

        if not iidn:
            return self.item(iid, 'text')

        dirname = self.item(iidn, 'text')
        return join(dirname, self.item(iid , 'text'))

    def get_item_coord(self, iid):
        """
        It returns a tuple like (a, b, c, ...)
        Which corresponds to an item depth in the tree.
        """
        pass

    def get_pick_list(self):
        xs = self.tag_has('sel')
        return map(lambda iid: self.get_item_path(iid), xs)

    def unpick_all(self):
        pass

    def unpick(self):
        """
        Maybe there is a better way to rewrite it.
        """

        iid  = self.selection()[0]
        tags = self.item(iid, 'tags')
        tags = list(tags)

        try:
            index = tags.index('sel')
        except ValueError:
            pass
        else:
            del tags[index]

        self.item(iid, tags=tags)


    def pick(self):
        iid  = self.selection()[0]
        tags = self.item(iid, 'tags')
        tags = tags + ('sel',)
        self.item(iid, tags=tags)

    def get_curselection(self):
        """
        """

        return self.selection()[0]

    def get_curselection_path(self):
        iid = self.selection()[0]
        return self.get_item_path(iid)

    def set_curselection_with_coord(self, coord):
        pass

    def set_curselection(self, iid):
        """
        """
        self.selection_remove(self.selection())
    
        self.focus(iid)
        self.selection_add((iid, ))
        self.see(iid)

    def set_curselection_on(self):
        """
        """
        self.set_curselection(self.get_children('')[0])

    def find_item(self, regex):
        for ind in self.get_children(self.get_item_dir(self.selection()[0])):
            if search(regex, self.item(ind, 'text')): 
                self.set_curselection(ind)
                break






