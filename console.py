import imp
import pdb
from models.album import Album
from models.artist import Artist
import respositories.album_respository as album_respository
import respositories.artist_repository as artist_repository


artist_1 = Artist('Jim Bob')

artist_repository.save(artist_1)

artists = artist_repository.select_all()


for artist in artists:
    print(artist.__dict__)
    

pdb.set_trace()