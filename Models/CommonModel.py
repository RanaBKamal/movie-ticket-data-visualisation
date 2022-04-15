# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table
from Models.TicketModel import Ticket
from Models.MovieModel import Movie
from Models.CustomerModel import Customer
import sqlite3
class Common:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to book ticket for customer
    def book
