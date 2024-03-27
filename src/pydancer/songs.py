# prob want this to just read the titles of song files instead of hard coded?
def listSongs(genre):
    if genre == 'Rock':
        return "Rock Songs:\n Blood And Steel"
    elif genre == 'House':
        return "House Songs:\nTwo In The Rain"
    else:
        return "Rock Songs:\nBlood And Steel \nHouse Songs:\nTwo In The Rain"
