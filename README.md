keycmd
======

A modal file manager. Keycmd is a very flexible file manager, probably the most flexible one that exists.
It is easily extensible since it is python and implemented on top of Tkinter. 


Overview
========

A file system can be abstracted as a tree. Subdirectories can be seen as nodes of such a tree. 
Keycmd has the feature of viewing a file system as a set of nodes, such nodes correspond to directories
of the tree. The nodes are grouped into a sequential style.

Installation
============

**Note:** 
It demands python2.

    pip install keycmd

Basic usage
===========

The scheme below introduces a simple idea of how keycmd works.

![screenshot-1](screenshot-1.jpg)


The line whose background is blue is the cursor. It is used to select files/directories to have commands performed on.
The lines with a small delta at the beginning are the nodes of the tree. It is possible to have as many nodes as necessary.
The lines below a view are named subviews. These are files belonging to the view/dir.

I'll refer to nodes as views sometimes, so a view in this context is the same as a node. Keycmd is a modal file manager
it can have as many modes as you want. There is no need for mouse at all. Everything is done with the keyboard.

I believe that the best way to learn a modal thing is through examples. I'll walk you through basic examples of usage it is
important to have keycmd running.

**Getting ready to start**

First of all, you need to create some files and directories to play around with cmd.


    cd ~
    mkdir alpha
    cd alpha
    mkdir dir1
    mkdir dir2
    cd dir1
    echo '' >> file1
    cd ..
    cd dir2
    echo '' >> file2


Once you have created these files, it is time to run keycmd.


Type in a terminal 

    keycmd

that should be enough to launch the program.

Keycmd for default opens a view corresponding to the user home directory.
If you have created the files above then the directory alpha should be listed
in a view.


**Changing cursor position**

The most useful set of keys are the keys 'Key-j' and 'Key-k', these keys are
responsible by moving the cursor down and up. 

Test it until you getting comfortable.


**Opening views**

It is possible to have as many views as needed. You'll find yourself opening a lot of views in some situations
to move, copy files from a directory to other. You can open views for directories and files. 

Put the cursor over the directory alpha then type 'Key-c'. It will open a view for the directory alpha with
all the files and directories listed under this view.

Try it with dir1 and dir2.

**Changing cursor between views**

Once you have followed the steps above you'll have some views opened. Now, try the keys 'Key-h' and 'Key-l'
These keys move the cursor one view up and one view down.


**Select files**

Some commands perform operations based on selected views/subviews. In order to select
a view or a subview you put the cursor over the given item then press 'Key-s'
You can have selections under multiple views.

Try it out !

**Unselect files**

To unselect a given view/subview you just put the cursor over then press 'Key-s'.

**Delete some files**

Deleting files works altogether with selecting files. You first select the files to be removed
then press 'Key-d' to delete them.


**Remove a view**

Sometimes you don't need to work with a view anymore then you can
remove it with 'Key-z' when the cursor is over it or over one of its subviews.

Try opening a view for alpha twice then press 'Key-z' when the cursor is over the view alpha
or over one of its subviews.


**Changing a directory view**

Sometimes you don't need another view, you just need to go a directory down or a directory up
from a given view. You use the key 'Key-e' to change a view path. Put the cursor
over a given subview that matches a directory then type 'Key-e' it will make the view of that
subview turn into the subview's path. 

**Going a directory up**

You will find situations that you need to go a directory upwards from a given view.
If your view lists the file of a directory named /home/tau/dir and you want
that view to list files from /home/tau, all you need to do is putting the cursor
over the view /home/tau/dir or over one of its subviews then pressing 'Key-b'.

Try it out.

**Creating a file**

In order to create a file you put the cursor over a view then press 'Control-n'.
It will open an edit area where you will type the filename.

**Creating a directory**

Put the cursor over a view then type 'Control-f', it opens an edit area where to type
the dir name.

**Renaming files**

Put the cursor over a view or a subview then press 'Key-r', it will open an edit area
where to insert the new name.

**Quickly changing cursor to a view/subview**

Keycmd supports a mode named Quick Search which permits you to type
some simple patterns then quickly change the cursor to a given subview.

Once you press 'Key-g' or 'g' in standard mode it will enter quick search mode.
Whatever you type will be interpreted as a pattern and it will select the subview
that matches that pattern. Press 'Escape' or 'Return' to exit Quick Search mode.

**Copying dirs/files**

The way to copy files with keycmd consists of selectiong a set of views or subviews
then putting the cursor over a given view or subview then pressing 'Key-y'.
Keycmd will copy whatever is selected to the directory whose cursor is over.

**Mounting filesystems**
It is possible to implement a key command to execute mount command
to mount some device. I haven't felt that need so far. Whenever
i need to mount usb storages there is the usbmount package which does it for me.

**Configuration file**

Keycmd has a configuration file where you can set options for the plugins as well as
set some personalized stuff for the graphical interface. Set which plugins should be loaded etc.

The file is cmdrc and should be created in your home directory inside .keycmd after
keycmd is launched for a first time.

The file cmdrc is a python script that is executed wheneer keycmd is launched.

~~~python
# cmdrc

import sys
##############################################################################

from os.path import expanduser, join
sys.path.append(join(expanduser('~'), '.keycmd'))
##############################################################################

# Functions used to load the plugins.
from cmdlib.modes import autoload, autocall
##############################################################################
# Important plugins.

# Define the modes.
import cmdlib.modes.default_mode
autoload(cmdlib.modes.default_mode)

##############################################################################
# modes, plugins.

# The basic set of key commands that keycmd supports.
import cmdlib.modes.basic_jumps
autoload(cmdlib.modes.basic_jumps)

# Used to update the statusbar mode field in which keycmd is in.
import cmdlib.modes.status
autoload(cmdlib.modes.status)

# Used to quickly jump to views/subviews.
import cmdlib.modes.qsearch
autoload(cmdlib.modes.qsearch)

# Used to unpack files.
# import cmdlib.modes.zip
# autoload(cmdlib.modes.zip)

# Used to open files with xdg-open.

import cmdlib.modes.xdg
autoload(cmdlib.modes.xdg)

# Basic commands.
import cmdlib.modes.basic_commands
autoload(cmdlib.modes.basic_commands)

# View scroll.
import cmdlib.modes.view_scroll
autoload(cmdlib.modes.view_scroll)

##############################################################################

# This function is called when keycmd launches and is used
# to set configurations for keycmd.
def setup(view):
    view.tag_configure('d', foreground='red')        # Set the color for directories.
    view.tag_configure('-', foreground='yellow')       # Set the color for files.
    view.tag_configure('sel', background='white')     # Set the color for selected items.

    # Used to set background, foreground colors.
    import ttk
    ttk.Style().configure("Treeview", background="black", 
                          foreground="green", fieldbackground="black")
    view.master.master.geometry('300x500')

autocall(setup) 
~~~

**Opening files**

Keycmd uses xdg-open application to open files. Check the manpages for xdg-open program.
Suppose you have defined to open '.c' files with gedit, if you put the cursor
over a file named 'cool.c' then type 'Key-o' it will launch gedit with the cool.c file
opened in it.

**Moving files**

Moving files works pretty much like copying files. You selected the files
then put the cursor over a given view/subview then press 'Key-m'.

**Adding a view from path.**

Sometimes you may need to add a view from a text path.
You do so by pressing 'Key-t' then inserting the path then pressing
'Return'


**Copy view/subview path to the clipboard**

Sometimes it is interesting to have the complete path of a given view/subview in the clipboard.
So you can paste it anywhere. For such, you put the cursor over a givem view/subview then
press 'Control-u' it will copy the path to the clipboard then you can paste it over anywhere.


Support
=======

#### Freenode

**Address:** irc.freenode.org

**Channel:** #vy




