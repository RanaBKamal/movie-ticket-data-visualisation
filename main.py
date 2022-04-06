from datetime import datetime
import numpy as np

import Models.ConnectionModel as ConnectionModel
import Models.UserModel as UserModel
import Models.CustomerModel as CustomerModel
import Models.MovieModel as MovieModel
import Models.TicketModel as TicketModel

connectionObject = ConnectionModel.Connection("Database/database.db")

customerModel = CustomerModel.Customer(connectionObject)
movieModel = MovieModel.Movie(connectionObject)

# creating tickets model
# ticketModel = TicketModel.Ticket(connectionObject)
# userModel = UserModel.User(connectionObject)
# user = userModel.getAllData();
# customer = customerModel.getAllData()
# movie = movieModel.getDataById(1)
# ticket = ticketModel.getDataById(1)
# print(movie[0][2])

movie_status = '0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0'
print(np.fromstring(movie_status, dtype=bool, sep=','))

# userModel.insertData("Kamal B. Rana", "kamalbrana", "kamal@kamal.com", "hello", "Admin")

connectionObject.closeConnection()
