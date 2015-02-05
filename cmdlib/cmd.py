# cmd.py
# Description:
#
#
#
#
#
#
#

from ask import Ask
import os
import nix

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

"""
def go_prev_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    iidz = view.prev(iidm)

    if not iidz: return
    view.set_curselection(iidz)
"""

def go_prev_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    if iidn == iidm: iidz = view.prev(iidm)
    else: iidz = iidm

    view.set_curselection(iidz if iidz else iidm)

"""
def go_next_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)
    iidz = view.next(iidm)

    if not iidz: return
    view.set_curselection(iidz)
"""

def go_next_dir(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    iidz = view.next(iidm)

    view.set_curselection(iidz if iidz else iidn)


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

def rename(view):
    ph = view.get_curselection_path()
    dir = os.path.dirname(ph)

    ask = Ask(view, 'File name')
    nix.mv((ph,), os.path.join(dir, ask.data))

    view.update_view_list()
    view.set_curselection_on()

def open_with(view):
    ph = view.get_curselection_path()
    nix.open_with(ph)

def open_with_default(view):
    ph = view.get_curselection_path()
    nix.open_with_default(ph)


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

"""
def go_end(view):
    iidn = view.get_curselection()
    iidm = view.get_item_dir(iidn)

    xs = view.get_children(iidm)
    iidz = xs[-1] if xs else iidm
    view.set_curselection(iidz)
"""

def flip_show_hidden(view):
    view.show_hidden = False if view.show_hidden else True
    view.update_view_list()
    view.set_curselection_on()

def clip_curselection(view):
    iidn = view.get_curselection()
    ph = view.get_item_path(iidn)

    view.clipboard_clear()
    view.clipboard_append(ph)

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

def unzip(view):
    xs  = view.get_pick_list()
    dst = view.get_curselection_path()
    cmd = 'unzip %s -d "%s"' % (' '.join(map(lambda it: '"%s"' % it, xs)), dst)
    nix.call(cmd)
    view.update_view_list()
    view.set_curselection_on()


def load(view):
    import utils
    INSTALL = [('<Key-k>', lambda view: view.event_generate('<Key-Up>')), 
               ('<Key-j>', lambda view: view.event_generate('<Key-Down>')),
               ('<Key-c>', add_node), 
               ('<Key-e>', cd_dir), 
               ('<Key-y>', cp), 
               ('<Control-y>', cp_with_prefix), 
               ('<Control-e>', unzip), 
               ('<Control-h>', flip_show_hidden), 

               ('<Key-E>', cd_dir_path), 
               ('<Key-b>', cd_prev_dir), 
               ('<Key-h>', go_prev_dir), 
               ('<F2>', new_dir),
               ('<Key-l>', go_next_dir), 
               ('<Key-m>', mv), 
               ('<Key-d>', rm), 
               ('<F3>', rename), 
               ('<Control-u>', clip_curselection), 
               ('<F1>', create_text_file),
               ('<Key-o>', open_with), 
               ('<Key-i>', open_with_default), 
               ('<Key-z>', remove_node), 
               ('<Key-s>', lambda view: view.pick())]
            

    utils.install(INSTALL, view)

    view.tag_configure('d', foreground='red')
    view.tag_configure('-', foreground='blue')
    view.tag_configure('sel', background='grey')























