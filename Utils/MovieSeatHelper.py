# Written Date: April 07, 2022
# Written for: Python II Project W22, Lambton College Mississauga
# Description: This class contains helper methods related to seats
# By default we have used 10x6 seats structure
import numpy as np


class MovieSeatHelper:

    @staticmethod
    def createNewMovieSeats():
        initial_seats = np.zeros(60, dtype=int)
        return np.array2string(initial_seats, separator=',')

    @staticmethod
    def convertStringArrayToArray(seat_status):
        seat_status_array = np.fromstring(seat_status, dtype=bool)
        return seat_status_array
