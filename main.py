from datetime import datetime
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

# creating tickets model
# ticketModel = Ticket(connectionObject)
# userModel = User(connectionObject)
# user = userModel.getAllData();
# customer = customerModel.getAllData()
# movie = movieModel.getDataById(1)
# ticket = ticketModel.getDataById(1)
# print(movie[0][2])

# userModel.insertData("Kamal B. Rana", "kamalbrana", "kamal@kamal.com", "hello", "Admin")
print(MovieSeatHelper.createNewMovieSeats())
my_arr = MovieSeatHelper.convertStringArrayToArray(MovieSeatHelper.createNewMovieSeats())
print(my_arr)
connectionObject.closeConnection()
