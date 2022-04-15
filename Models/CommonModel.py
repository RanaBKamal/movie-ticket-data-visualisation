# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table
from Models.TicketModel import Ticket
from Models.MovieModel import Movie
from Models.CustomerModel import Customer
from Utils.MovieSeatHelper import MovieSeatHelper
import sqlite3

class Common:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to book ticket for customer
    def bookCustomerTicket(self, cust_full_name, email, gender, age, movie_id, ticket_type, price, posX, posY, user_id):
        try:
            customerModel = Customer(self.connObj)
            ticketModel = Ticket(self.connObj)
            movieModel = Movie(self.connObj)

            #create customer
            customerModel.insertData(cust_full_name, email, gender, age)
            cust_id = customerModel.getDataByEmail(email)[0][0]
            movie = movieModel.getDataById(movie_id)
            movie_seat_array = MovieSeatHelper.convertStringArrayToArray(movie[0][2])
            movie_seat_array = MovieSeatHelper.bookSeatAt(posX, posY, movie_seat_array);
            movie_seat_string = MovieSeatHelper.convertArrayToStringArray(movie_seat_array)
            movieModel.updateSeatStatus(movie_id, movie_seat_string)
            seat_position = "["+str(posX)+","+str(posY)+"]"
            ticketModel.insertData(movie_id, ticket_type, price, seat_position, cust_id,user_id)
        except:
            return False
        else:
            return True






