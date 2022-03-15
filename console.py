import imp
import pdb
from re import A
from models.album import Album
from models.artist import Artist
import respositories.album_respository as album_respository
import respositories.artist_repository as artist_repository



artist_1 = Artist('Jim Bob')

artist_repository.save(artist_1)

artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)

album_1 = Album('good jams', 'human music', artist_1)
album_respository.save(album_1)

albums = album_respository.select_all()

for album in albums:
    print(album.__dict__)
    

pdb.set_trace()