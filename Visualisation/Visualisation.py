# class to get required data from database for visualisation
import matplotlib.pyplot as plt
import numpy as np


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

    # function to visualize data
    def visualizeByMovieCategory(self):
        movies_by_type = self.getMoviesByCategory()
        mov_x_array = []
        mov_y_array = []

        for item in movies_by_type:
            mov_x_array.append(item[0])
            mov_y_array.append(item[1])
        mov_x_np = np.array(mov_x_array)
        mov_y_np = np.array(mov_y_array)
        plt.title("Visualisation by Movie Type")
        plt.bar(mov_x_np, mov_y_np, )
        plt.show()