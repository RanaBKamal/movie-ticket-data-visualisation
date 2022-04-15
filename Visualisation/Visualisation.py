# class to get required data from database for visualisation
class Visualisation:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to get movies based on category
    def getMoviesByCategory(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT movie_type, count(*) FROM Movies GROUP BY movie_type;
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row
