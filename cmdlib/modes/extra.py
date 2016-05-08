from subprocess import Popen

def install(view, app):
    view.hook('1', '<Key-i>', lambda event: Popen([app, 
                event.widget.get_item_path(event.widget.get_curselection())]))

