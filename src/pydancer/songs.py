# prob want this to just read the titles of song files instead of hard coded?
def listSongs(genre):
    if genre == 'country':
        return "Country Songs:\ncountry song 1\ncountry song 2"
    elif genre == 'pop':
        return "Pop Songs:\npop song 1\npop song 2"
    else:
        return "Country Songs:\ncountry song 1\ncountry song 2\nPop Songs:\npop song 1\npop song 2"
