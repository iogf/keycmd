
def set_std_mode(view):
    view.chmode(1)

def install(view):
    view.add_mode(1, opt=True)
    view.chmode(1)

    view.install((-1, '<Escape>', lambda event: set_std_mode(event.widget))),


