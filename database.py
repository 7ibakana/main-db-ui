import sqlite3
import ui

db = 'art.sqlite'

class artsqlite3():
    def __init__(self):
        with sqlite3.connect(db) as con:
            con.execute('CREATE TABLE IF NOT EXISTS artists (artistid INTEGER PRIMARY KEY, artistname TEXT UNIQUE, artistemail TEXT)')
            con.execute('CREATE TABLE IF NOT EXISTS artworks (artname TEXT UNIQUE, artistname TEXT, availability TEXT, artist INTEGER, FOREIGN KEY(artist) REFERENCES artists(artistid))')
        con.close()

    def add_artist(self, artist, email):

        artistName = artist
        artistEmail = email

        try:
            with sqlite3.connect(db) as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM artists WHERE artistname = ?', (artistName,))
                artist_check = cursor.fetchone()
                if artist_check is None:
                    con.execute('INSERT INTO artists VALUES (NULL, ?, ?)', (artistName, artistEmail))
                    print('\nArtist added to database')
                else:
                    print('\nArtist already exists in database')
        except sqlite3.IntegrityError:
            raise artwork(f'\nError inserting: cannot not add duplicate artist')
        con.close()


    def add_artwork(self, artwork, artist):

        availability = 'Unavailable'
        
        try:
            with sqlite3.connect(db) as con:
                cursor = con.cursor()
                cursor.execute('SELECT artistid FROM artists WHERE artistname = ?', (artist,))
                artistCheck = cursor.fetchone()
                if artistCheck:
                    idInt = int(artistCheck[0])
                cursor.execute('SELECT * FROM artworks WHERE artname = ?', (artwork,))
                artcheck = cursor.fetchone()

                if artistCheck is None:
                    print('\nNo Artists found by that name - Add artist before adding artwork')
                elif artcheck:
                    print('\nThat artwork is already in the database.')
                else:
                    con.execute('INSERT INTO artworks VALUES (?, ?, ?, ?)', (artwork, artist, availability, idInt))
                    print('\nArtwork added to database')
        except:
            raise artwork('\nError inserting artwork')
        con.close()
 
    def delete_artwork(self, artwork):

        try:
            with sqlite3.connect(db) as con:
                cursor = con.cursor()
                cursor.execute('SELECT * FROM artworks WHERE artname = ?', (artwork,))
                resultTest = con.execute('SELECT * FROM artworks WHERE artname like ?', (artwork,))
                if cursor.fetchone() is None:
                    print('\nNo artwork found with that name')
                else:
                    for row in resultTest:
                        print('\nArtwork: ' + row[0] + ' | Artist: ' + row[1] + ' | Availability: ' + row[2])
                        userInput = ui.get_positive_float('\nConfirm deletion? ')
                        if userInput == 'Yes':
                            con.execute('DELETE FROM artworks WHERE artname = ?', (artwork,))
                            print('Artwork deleted from database')
                        else:
                            pass
            con.close()
        except:
            raise artwork('\nError searching for artwork')

    def available_artwork(self):

        availability = 'Available'
        try:
            with sqlite3.connect(db) as con:
                cursor = con.cursor()
                resultsCheck = cursor.execute('SELECT * FROM artworks WHERE availability = ?', (availability,))
                results = con.execute('SELECT * FROM artworks WHERE availability = ?', (availability,))
                if resultsCheck.fetchone() is None:
                    print('\nNo artwork available at this time')
                else:
                    for row in results:
                        print('\nArtist: ' + row[1] + ' | Artwork: ' + row[0] + ' | Availability: ' + row[2])
            con.close()
        except:
            raise artwork('\nError fetching artwork')  

# todo other DB interaction