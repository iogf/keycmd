from subprocess import Popen

def run_app(view):
    iidn = view.get_curselection()
    ph = view.get_item_path(iidn)
    Popen(['xdg-open', ph])

def install(view):
    print 'foo'
    view.install((1, '<Key-o>', lambda event: run_app(event.widget))) 


