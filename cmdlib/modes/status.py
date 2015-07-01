from cmdlib.app import root
TIME = 1000

def update_mode(view):
    """
    It is used to update the mode status bar 
    in TIME interval.
    """

    def cave():
        if not cave.keep: return
        root.statusbar.set_mode('Mode: %s' % view.id)
        view.after(TIME, cave)

    """
    The cave function is used
    to update the status bar.

    When the AreaVi loses focus it sets cave.keep to False then
    cave no more calls after.
    It may be interesting to call 
    
    area.after_idle.
    """

    cave.keep = True
    cave()
    def stop(): cave.keep = False
    view.hook(-1, '<FocusOut>', lambda event: stop())

def install(view):
    view.install((-1, '<FocusIn>', lambda event: update_mode(event.widget)))


