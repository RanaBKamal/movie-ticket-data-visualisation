# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table

from Utils.MovieSeatHelper import MovieSeatHelper
class Movie:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to create table on the database
    def createMovieTable(self):
        try:
            self.connObj.getCursor().execute('''
                    CREATE TABLE IF NOT EXISTS Movies(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name VARCHAR(40) NOT NULL,
                        seat_status VARCHAR(1000) NOT NULL,
                        movie_type VARCHAR(10) NOT NULL,
                        movie_image VARCHAR(100),
                        release_date DATE NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    );
                ''')
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to drop the customer table
    def dropMovieTable(self):
        try:
            self.connObj.getCursor().execute('''
                    DROP TABLE IF EXISTS Movies;
                ''')
        except:
            return False
        else:
            return True

    # method to insert into customers table
    def insertData(self, movie_name, seat_status, movie_type, movie_image, release_date):
        try:
            self.connObj.getCursor().execute('''
                    INSERT INTO Movies(movie_name, seat_status, movie_type, movie_image, release_date)
                    VALUES
                    (?, ?, ?, ?);
                ''', (movie_name, seat_status, movie_type, movie_image, release_date))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to delete the model
    def deleteDataById(self, movie_id):
        try:
            self.connObj.getCursor().execute('''
                DELETE FROM Movies
                WHERE
                id = ?;
            ''', (movie_id,))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # function to get the movies by id
    def getDataById(self, movie_id):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Movies
                WHERE
                id = ?;
            ''', (movie_id,))
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # function to get all data
    def getAllData(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Movies
            ''')
            rows = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return rows

    # get latest movie
    def getLatestMovie(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Movies  
                ORDER BY created_at DESC LIMIT 1
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # update seat status
    def updateSeatStatus(self, movie_id, seat_status_string_array):
        try:
            self.connObj.getCursor().execute('''
                UPDATE Movies
                SET seat_status = ?
                WHERE id = ?;
            ''', (seat_status_string_array, movie_id))
            self.connObj.commitChanges();
        except:
            return False
        else:
            return True

    # method to create new movie to the movies table
    def createNewMovie(self, movie_name, movie_type, movie_image, release_date):
        # create new seat status here
        try:
            seat_status = MovieSeatHelper.createNewMovieSeatsStringArray()
            self.insertData(movie_name, seat_status, movie_type, movie_image, release_date)
        except:
            return False
        else:
            return True
