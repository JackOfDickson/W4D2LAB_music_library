from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    result = run_sql(sql)
    
    for row in result:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists
    