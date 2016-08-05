from cmdlib.ask import Get
from re import escape, split

class QuickSearch(object):
    def __init__(self, view):
        """

        """
        self.view = view
        self.seq  = None
        view.install((1, '<Key-g>', lambda event: self.start()))

    def start(self):
        jump =lambda data: self.seq.next()
        ask = Get(self.view, events = {'<Alt-p>': lambda wid: self.search_down(), 
                                       '<Alt-o>': lambda wid: self.search_up(), 
                                       '<Control-j>': lambda wid: self.search_down(), 
                                       '<Control-k>': lambda wid: self.search_up(), 
                                       '<<Data>>':self.on_data, '<BackSpace>': self.on_data, 
                                       '<Return>': lambda wid: True, 
                                       '<Escape>': lambda wid: True})

    def on_data(self, wid):
        data     = wid.get()
        data     = split(' +', data)
        data     = '.+'.join(map(lambda ind: escape(ind), data))
        self.seq = tuple(self.view.find(data))
        self.index = -1
        self.search_down()

    def search_up(self):
        if self.index - 1 < 0: return
        self.view.set_curselection(self.seq[self.index - 1])
        self.index = self.index - 1

    def search_down(self):
        if self.index + 1 >= len(self.seq): return
        self.view.set_curselection(self.seq[self.index + 1])
        self.index = self.index + 1

install = QuickSearch







