from subprocess import call

def unzip(view):
    xs  = view.get_pick_list()
    dst = view.get_curselection_path()
    cmd = 'unzip %s -d "%s"' % (' '.join(map(lambda it: '"%s"' % it, xs)), dst)
    call(cmd, shell=True)
    view.update_all_views()
    view.activate()

def install(view):
    view.install((1, '<Control-e>', lambda event: unzip(event.widget))) 








