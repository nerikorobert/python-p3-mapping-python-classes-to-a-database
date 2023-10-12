from config import CONN, CURSOR


class Song:

    def __init__(self, name, album) -> None:
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()  # Commit the transaction

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        id, song_name, song_album =song.save()
        print(id, song_name, song_album)
        
        return song

    def save(self):
        sql = f"""
            INSERT INTO songs (name, album)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  # Commit the transaction
       
        return CURSOR.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            (f'{self.name}', f'{self.album}')
        ).fetchone()