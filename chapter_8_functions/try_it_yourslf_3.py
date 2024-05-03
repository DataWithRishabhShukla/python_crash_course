

import os 
os.system('clear')

def make_album(artist,title):
    """ Returns the album information in dictionary."""
    album_info = {'artist':artist, 'title':title}
    return album_info

while True:
    artist_name = input('Please enter artist name: ')
    title = input('Please enter the album name: ')
    print('\n Enter q to exit anytime.')
    
    if artist_name == 'q' or title == 'q':
        break
    print(make_album(artist_name,title))

