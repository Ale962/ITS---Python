# Lesson 4 Exercise 8.7

'''
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artists: str, albums: str, songs = "None"):
    disk: dict[str] = {"artist": artists, "album": albums, "songs_number": songs}
    return disk

artist_1: str = input("Which singer or band do you like the most? ")
albums_1: str = input("Which is her/his/their album that you prefer? ")
artist_2: str = input("Another singer or band that do you like? ")
albums_2: str = input("Which is her/his/their album that you prefer? ")
songs_2: str = input("How many songs have this album? ")
artist_3: str = input("Another singer or band that do you like? ")
albums_3: str = input("Which is her/his/their album that you prefer? ")
songs_3: str = input("How many songs have this album? ")

first_disk = make_album(artist_1, albums_1)
second_disk = make_album(artist_2, albums_2, songs_2)
third_disk = make_album(artist_3, albums_3, songs_3)

print(*first_disk.values())
print(*second_disk.values())
print(*third_disk.values())