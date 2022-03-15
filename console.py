import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository



artist_1 = Artist('Jim Bob')

artist_repository.save(artist_1)

artists = artist_repository.select_all()
for artist in artists:
    print(artist.__dict__)

album_1 = Album('good jams', 'human music', artist_1)
album_repository.save(album_1)

albums = album_repository.select_all()
for album in albums:
    print(album.__dict__)
    
print(album_repository.select(1))
    

pdb.set_trace()