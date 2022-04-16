from datetime import date
import numpy as np

from Models.ConnectionModel import Connection
from Models.UserModel import User
from Models.CustomerModel import Customer
from Models.MovieModel import Movie
from Models.CommonModel import Common
from Utils.MovieSeatHelper import MovieSeatHelper
from Models.TicketModel import Ticket
from Visualisation.Visualisation import Visualisation


# bar graph here
import matplotlib.pyplot as plt
# make data
# x = np.array(["Male", "Female", "Other"])
# y = np.array([20, 30, 4])
# plt.bar(x, y)
# plt.show()
#
# # pie
# y = np.array([35, 25, 25])
# myLabels = ["Male", "Female", "Other"]
#
# plt.pie(y, labels=myLabels)
# plt.show()
#
# ypoints = np.array([3, 8, 7, 10])
#
# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()


# visualisation based on movie type
connectionObject = Connection("Database/database.db")
visualisation = Visualisation(connectionObject)
visualisation.visualizeByMovieCategory()
# movies_by_type = visualisation.getMoviesByCategory()
# mov_x_array = []
# mov_y_array = []
#
# for item in movies_by_type:
#     mov_x_array.append(item[0])
#     mov_y_array.append(item[1])
# mov_x_np = np.array(mov_x_array)
# mov_y_np = np.array(mov_y_array)
# plt.title("Visualisation by Movie Type")
# plt.bar(mov_x_np, mov_y_np, )
# plt.show()

customerModel = Customer(connectionObject)
# customerModel.insertData("test test", "testtest4@gmail", "lamo", 34)
# print(customerModel.getDataByEmail("testtest4@gmail"))
commonModel = Common(connectionObject)
if(commonModel.bookCustomerTicket("test test","testtest55@gtest", "Male", 44, 11, "Gold", 400, 4, 4, 1)):
    print("success")
else:
    print("failed")
movieModel = Movie(connectionObject)
# print(movieModel.createNewMovie("XXX", "ACTION", "image/img.JPG", date.today()))
# current_movie = movieModel.getLatestMovie()
#
# if current_movie:
#     seatStringArray = current_movie[0][2]
# else:
#     seatStringArray = "[]";
# seatArray = MovieSeatHelper.convertStringArrayToArray(seatStringArray)
# print(seatArray)



# creating tickets model
# ticketModel = Ticket(connectionObject)
# userModel = User(connectionObject)
# user = userModel.getAllData();
# customer = customerModel.getAllData()
# movie = movieModel.getDataById(1)
# ticket = ticketModel.getDataById(1)
# print(movie[0][2])

# userModel.insertData("Kamal B. Rana", "kamalbrana", "kamal@kamal.com", "hello", "Admin")
# print(MovieSeatHelper.createNewMovieSeatsStringArray())

# my_arr = MovieSeatHelper.bookSeatAt(0, 0, my_arr)
# print(my_arr)
# print(MovieSeatHelper.convertArrayToStringArray(my_arr))
#
connectionObject.closeConnection()
