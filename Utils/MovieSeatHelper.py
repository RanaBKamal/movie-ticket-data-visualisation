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
        seat_status = seat_status.strip('[]')
        seat_status_array = np.fromstring(seat_status, dtype=int, sep=',')
        return seat_status_array

    @staticmethod
    def convertArrayToStringArray(seat_status_array):
        return np.array2string(seat_status_array, separator=',')

    @staticmethod
    def getSeatStatus(row, col, seat_status_array):
        position_counter = 0
        for i in range(10):
            for j in range(6):
                if i == row and j == col:
                    return seat_status_array[position_counter]
                else:
                    return False
                position_counter += 1

    @staticmethod
    def bookSeatAt(row, col, seat_status_array):
        position_counter = 0
        break_out_flag = False
        for i in range(10):
            for j in range(6):
                if i == row and j == col:
                    seat_status_array[position_counter] = True
                    break_out_flag = True
                    break
                position_counter += 1

            if break_out_flag:
                break
        return seat_status_array

    @staticmethod
    def unBookSeatAt(row, col, seat_status_array):
        position_counter = 0
        break_out_flag = False
        for i in range(10):
            for j in range(6):
                if i == row and j == col:
                    seat_status_array[position_counter] = False
                    break_out_flag = True
                    break
                position_counter += 1

            if break_out_flag:
                break
        return seat_status_array
