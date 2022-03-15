from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    result = run_sql(sql)
    
    for row in result:
        album = Album(row['title'], row['genre'], row['artist_id'], row['id'])
        albums.append(album)
    return albums