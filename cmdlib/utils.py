def install(args, view):
    for event, handle in args:
        view.bind(event, lambda e, v=view, h=handle: h(v))

