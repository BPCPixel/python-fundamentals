"""
Practice: Create a program to manage a playlist.

Author: Lalo Téllez
"""

print(f'{"=" * 20} Playlist {"=" * 20}\n')

playlist = []
counter_song = 1

# User enters the number of songs
songs_number = int(input('Number of songs: '))

# Adding songs to playlist
for i in range(songs_number):
    name_song = input(f'Name song {i + 1}: ')
    playlist.append(name_song)

# Sorting the list in alphabetical order
playlist.sort()
print(f'\nYour playlist in alphabetical order:\n{playlist}')

# Sorting the list in descending alphabetical order
playlist.sort(reverse=True)
print(f'\nYour playlist in descending alphabetical order:\n{playlist}')

# Iterating playlist
print('\nIterating playlist')
for song in playlist:
    print(f'{counter_song} - {song}')
    counter_song += 1
    
print(f'\n{"=" * 50}')
