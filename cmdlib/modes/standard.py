# cmd.py
# Description:
#
#
#
#
#
#
#

from cmdlib.ask import Ask
import os
from cmdlib import nix

def add_node(view):
    """

    """

    iidn = view.get_curselection()
    ph = view.get_item_path(iidn)

    iidm = view.add_view(ph)
    view.set_curselection(iidm)


def cd_prev_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    ph = view.get_item_path(iidm)
    view.change_view(iidm, os.path.dirname(ph))

    view.set_curselection(iidm)


def cd_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    ph = view.get_item_path(iidn)

    view.change_view(iidm, ph)
    view.set_curselection(iidm)

def cd_dir_path(view):
    ask = Ask(view, 'File name:')
    if not ask.data: return

    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    view.change_view(iidm, ask.data)
    view.set_curselection(iidm)

def go_prev_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    if iidn == iidm: iidz = view.prev(iidm)
    else: iidz = iidm

    view.set_curselection(iidz if iidz else iidm)

def go_next_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    iidz = view.next(iidm)

    view.set_curselection(iidz if iidz else iidn)

def create_text_file(view):
    ask = Ask(view, 'File name:')
    if not ask.data: return
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    ph = view.get_item_path(iidm)

    fd = open(os.path.join(ph, ask.data), 'a+')
    fd.close()

    view.update_view_list()
    view.set_curselection_on()

def remove_node(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    view.delete(iidm)               
    view.set_curselection_on()

def new_dir(view):
    ask = Ask(view, 'Directory name:')
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    ph = view.get_item_path(iidm)
    nix.mkdir(os.path.join(ph, ask.data))

    view.update_view_list()
    view.set_curselection_on()

def flip_show_hidden(view):
    view.show_hidden = False if view.show_hidden else True
    view.update_view_list()
    view.set_curselection_on()

def clip_curselection(view):
    iidn = view.get_curselection()
    ph = view.get_item_path(iidn)

    view.clipboard_clear()
    view.clipboard_append(ph)

def toggle_pick(view):
    iid  = view.selection()[0]

    if not view.tag_has('sel', iid): view.pick()
    else: view.unpick()

def add_view_from_ph(view):
    ask = Ask(view, 'Insert path.')

    iidm = view.add_view(ask.data)
    view.set_curselection(iidm)


def install(view):
    view.install((1, '<Key-k>', lambda event: event.widget.event_generate('<Key-Up>')), 
               (1, '<Key-j>', lambda event: event.widget.event_generate('<Key-Down>')),
               (1, '<Key-c>', lambda event: add_node(event.widget)), 
               (1, '<Key-e>', lambda event: cd_dir(event.widget)), 
               (1, '<Control-h>', lambda event: flip_show_hidden(event.widget)), 
               (1, '<Key-E>',lambda event:  cd_dir_path(event.widget)), 
               (1, '<Key-t>',lambda event:  add_view_from_ph(event.widget)), 
               (1, '<Key-b>', lambda event: cd_prev_dir(event.widget)), 
               (1, '<Key-h>',lambda event:  go_prev_dir(event.widget)), 
               (1, '<F2>',lambda event:  new_dir(event.widget)),
               (1, '<Key-l>', lambda event: go_next_dir(event.widget)), 
               (1, '<F3>', lambda event: rename(event.widget)), 
               (1, '<Control-u>', lambda event: clip_curselection(event.widget)), 
               (1, '<F1>', lambda event: create_text_file(event.widget)),
               (1, '<Key-z>', lambda event: remove_node(event.widget)), 
               (1, '<Key-s>', lambda event: toggle_pick(event.widget)))
           








