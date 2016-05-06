def install(view):
    view.install((1, '<Alt-o>', lambda event: event.widget.xview('scroll', -1, 'pages')),
                 (1, '<Alt-p>', lambda event: event.widget.xview('scroll', 1, 'pages'))) 


