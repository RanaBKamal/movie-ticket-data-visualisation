from datetime import date
import numpy as np

from Models.ConnectionModel import Connection
from Models.UserModel import User
from Models.CustomerModel import Customer
from Models.MovieModel import Movie
from Utils.MovieSeatHelper import MovieSeatHelper
from Models.TicketModel import Ticket

connectionObject = Connection("Database/database.db")

customerModel = Customer(connectionObject)
movieModel = Movie(connectionObject)
print(movieModel.createNewMovie("XXX", "ACTION", "image/img.JPG", date.today()))

# creating tickets model
# ticketModel = Ticket(connectionObject)
# userModel = User(connectionObject)
# user = userModel.getAllData();
# customer = customerModel.getAllData()
# movie = movieModel.getDataById(1)
# ticket = ticketModel.getDataById(1)
# print(movie[0][2])

# userModel.insertData("Kamal B. Rana", "kamalbrana", "kamal@kamal.com", "hello", "Admin")
print(MovieSeatHelper.createNewMovieSeatsStringArray())

# my_arr = MovieSeatHelper.bookSeatAt(0, 0, my_arr)
# print(my_arr)
# print(MovieSeatHelper.convertArrayToStringArray(my_arr))
#
connectionObject.closeConnection()
