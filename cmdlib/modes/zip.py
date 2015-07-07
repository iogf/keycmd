from cmdlib import nix

def unzip(view):
    xs  = view.get_pick_list()
    dst = view.get_curselection_path()
    cmd = 'unzip %s -d "%s"' % (' '.join(map(lambda it: '"%s"' % it, xs)), dst)
    nix.call(cmd)
    view.update_view_list()
    view.set_curselection_on()

def install(view):
    view.install((1, '<Control-e>', lambda event: unzip(event.widget))) 


