from cmdlib.ask import Ask
import os
from cmdlib import nix

def cp(view):
    """
    """
    xs = view.get_pick_list()
    dst = view.get_curselection_path()
    nix.cp(tuple(xs), dst)

    view.update_all_views()
    view.activate()

def rm(view):
    xs = view.get_pick_list()
    nix.rm(tuple(xs))
    view.update_all_views()
    view.activate()

def mv(view):
    xs = view.get_pick_list()
    dst = view.get_curselection_path()
    nix.mv(tuple(xs), dst)

    view.update_all_views()
    view.activate()

def rename(view):
    ph = view.get_curselection_path()
    dir = os.path.dirname(ph)

    ask = Ask(view)
    nix.mv((ph,), os.path.join(dir, ask.data))

    view.update_all_views()
    view.activate()

def mkdir(view):
    ask = Ask(view)
    if not ask.data: return
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    ph = view.get_item_path(iidm)
    nix.mkdir(os.path.join(ph, ask.data))

    view.update_all_views()
    view.activate()

def create_text_file(view):
    ask = Ask(view)
    if not ask.data: return
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    ph = view.get_item_path(iidm)

    fd = open(os.path.join(ph, ask.data), 'a+')
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




