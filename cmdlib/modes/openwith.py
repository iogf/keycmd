from os.path import splitext
from subprocess import Popen

def install(view, map, default):
    def open_with(view):
        ph            = view.get_curselection_path()
        filename, ext = splitext(ph)

        try:
            app = map[ext]
        except KeyError:
            Popen([default, ph], shell=False)
        else:
            Popen([app, ph], shell=False)

    def open_with_default(view):
        ph = view.get_curselection_path()
        Popen([default, ph], shell=False)

    view.install((1, '<Key-o>', lambda event: open_with(event.widget)), 
                 (1, '<Key-i>', lambda event: open_with_default(event.widget)))




