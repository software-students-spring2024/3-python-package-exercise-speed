def listOptions(args): 
    if args.characters and args.difficulties:
        return 'Characters:\ngirl\nboy\nDifficulties:\neasy\nmedium\nhard'
    elif args.characters:
        return 'Characters:\ngirl\nboy'
    elif args.difficulties:
        return 'Difficulties:\neasy\nmedium\nhard'
    else:
        return 'Characters:\ngirl\nboy\nDifficulties:\neasy\nmedium\nhard'