def listDisplay(args):     
    if args.characters and args.themes:
        return 'Characters:\ngirl character\nboy character\nThemes:\npink\nblue'
    elif args.characters:
        return 'Characters:\ngirl character\nboy character'
    elif args.themes:
        return 'Themes:\npink\nblue'
    else:
        return 'Characters:\ngirl character\nboy character\nThemes:\npink\nblue'