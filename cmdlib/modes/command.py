from cmdlib.ask import Ask
import os
from cmdlib import nix

def cp(view):
    """
    """
    xs = view.get_pick_list()
    dst = view.get_curselection_path()
    nix.cp(tuple(xs), dst)

    view.update_view_list()
    view.set_curselection_on()

def rm(view):
    xs = view.get_pick_list()
    nix.rm(tuple(xs))
    view.update_view_list()
    view.set_curselection_on()

def mv(view):
    xs = view.get_pick_list()
    dst = view.get_curselection_path()
    nix.mv(tuple(xs), dst)

    view.update_view_list()
    view.set_curselection_on()

def rename(view):
    ph = view.get_curselection_path()
    dir = os.path.dirname(ph)

    ask = Ask(view, 'File name')
    nix.mv((ph,), os.path.join(dir, ask.data))

    view.update_view_list()
    view.set_curselection_on()

def cp_with_prefix(view):
    """
    """
    from os.path import basename, normpath
    # Maybe it should return a tuple.
    xs  = view.get_pick_list()
    dst = view.get_curselection_path()

    for ind in xs:
        filename = normpath(ind)
        filename = basename(filename)
        nix.cp((ind, ), '%s/%s\'' % (dst, filename))

    view.update_view_list()
    view.set_curselection_on()


def install(view):
    view.install((1, '<Key-y>', lambda event: cp(event.widget)), 
               (1, '<Control-y>', lambda event: cp_with_prefix(event.widget)), 
               (1, '<Key-m>',lambda event:  mv(event.widget)), 
               (1, '<Key-d>',lambda event:  rm(event.widget)), 
               (1, '<F3>', lambda event: rename(event.widget)))






