from cmdlib.ask import Get
from re import escape

class QuickSearch(object):
    def __init__(self, view):
        """

        """
        self.view = view
        self.seq  = None
        view.install((1, '<Key-g>', lambda event: self.start()))

    def start(self):
        jump =lambda data: self.seq.next()
        edit = Get(self.view, on_data=self.on_data, on_done=lambda data: None, on_next=jump, on_prev=jump)

    def on_data(self, data):
        self.seq = self.view.find(escape(data))
        self.seq.next()

install = QuickSearch






