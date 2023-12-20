import json

with open("songs.json", "r") as f:
    data = json.load(f)

"""
This code prints the json file contents in a nice format,
however, it converts it from a dict to a string
"""
# new_songs = json.dumps(songs, indent=2)
# print(new_songs)

# print(songs['elvis']['christmas'])

"""
This prints all the christmas song titles by elvis
"""
# for s in songs['elvis']['christmas']:
#     print(s['song_name'])

"""
Prints all songs under the 'elvis' key
"""
for category, songs in data['elvis'].items():
    print(f"{category.capitalize()} Songs:")
    for song in songs:
        print(song['song_name'])
    print()
