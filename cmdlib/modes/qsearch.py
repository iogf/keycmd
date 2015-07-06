from cmdlib.ask import *
from re import escape
from cmdlib.app import root

class QuickSearch(object):
    def __init__(self, view):
        """

        """
        view.add_mode('Quick Search')
        view.install(('Quick Search', '<Key>', lambda event: self.add_data(event.widget, event.keysym_num)),
                        (1, '<Key-backslash>', lambda event: event.widget.chmode('Quick Search')),
                        ('Quick Search', '<Escape>', lambda event: self.clear_data(event.widget)),
                        ('Quick Search', '<BackSpace>', lambda event: self.del_data(event.widget)))


        self.data = []

    def clear_data(self, view):
        root.statusbar.set_msg('')
        del self.data[:]

    def add_data(self, view, char):
        """

        """
        try:
            char = chr(char)
        except ValueError:
            return
        else:
            char = escape(char)
            self.data.append(char)

        data = ''.join(self.data)
        root.statusbar.set_msg(data)
        view.find_item(data)

    def del_data(self, view):
        """

        """

        try:
            self.data.pop()
        except IndexError:
            return

        data = ''.join(self.data)
        root.statusbar.set_msg(data)
        view.find_item(data)


install = QuickSearch


