from subprocess import check_output as run, CalledProcessError, STDOUT
from cmdlib.ask import Ask
from cmdlib.app import root
import os

def cp(view):
    """
    """
    xs   = view.get_pick_list()
    dst  = view.get_curselection_path()
    args = ['cp', '-R'] 
    args.extend(xs) 
    args.append(dst)
    run(args)
    view.update_all_views()
    view.activate()

def rm(view):
    xs   = view.get_pick_list()
    args = ['rm', '-fr']
    args.extend(xs)
    run(args)

    view.update_all_views()
    view.activate()

def mv(view):
    xs   = view.get_pick_list()
    dst  = view.get_curselection_path()
    args = ['mv']
    args.extend(xs)
    args.append(dst)
    run(args)

    view.update_all_views()
    view.activate()

def rename(view):
    ph  = view.get_curselection_path()
    dir = os.path.dirname(ph)
    ask = Ask(view)
    run(('mv', ph, os.path.join(dir, ask.data)))

    view.update_all_views()
    view.activate()

def mkdir(view):
    ask = Ask(view)
    if not ask.data: return
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    ph   = view.get_item_path(iidm)

    run(('mkdir', os.path.join(ph, ask.data)))
    
    view.update_all_views()
    view.activate()

def create_text_file(view):
    ask = Ask(view)
    if not ask.data: return
    iidn   = view.get_curselection()
    iidm   = view.get_item_dir(iidn)
    ph     = view.get_item_path(iidm)

    try:
        fd = open(os.path.join(ph, ask.data), 'a+')
    except Exception as e:
        root.statusbar.set_msg(e)
    else:
        fd.close()

    view.update_all_views()
    view.activate()


def install(view):
    view.install((1, '<Key-y>', lambda event: cp(event.widget)), 
               (1, '<Key-m>',lambda event:  mv(event.widget)), 
               (1, '<Key-d>',lambda event:  rm(event.widget)), 
               (1, '<F1>', lambda event: create_text_file(event.widget)),
               (1, '<F2>',lambda event:  mkdir(event.widget)),
               (1, '<F3>', lambda event: rename(event.widget)))



