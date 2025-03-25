# Lesson 4 Exercise 8.8

'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''

def make_album(artist: str, album: str, songs = "None"):
    disk: dict = {"artist": artist, "album": album, "songs_number": songs}
    return disk

albums: dict = {}

while True:

    artist = input("Which singer or band you like?: ")
    album = input("Which is her/his/their album that you prefer?: ")
    songs = input("How many songs have this album? ")

    disk = make_album(artist, album, songs)

    albums[artist] = disk

    question: str = input("Do you want to add a new singer? (y/n)")

    if question == "n":
        break
    else:
        continue

print(*albums.values())

