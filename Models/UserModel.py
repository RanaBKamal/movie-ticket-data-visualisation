# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table
from datetime import datetime


class User:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to create table on the database
    def createUserTable(self):
        try:
            self.connObj.getCursor().execute('''
                CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR(40) NOT NULL,
                    username VARCHAR(20) NOT NULL UNIQUE,
                    email VARCHAR(40) NOT NULL UNIQUE,
                    password VARCHAR(40) NOT NULL,
                    user_type VARCHAR(10) NOT NULL DEFAULT "admin",
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            ''')
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to drop the table Users if exists
    def dropUserTable(self):
        try:
            self.connObj.getCursor().execute('''
                DROP TABLE IF EXISTS Users;
            ''')
        except:
            return False
        else:
            return True

    # method to insert data to the users table
    def insertData(self, full_name, username, email, password, user_type):
        try:
            self.connObj.getCursor().execute('''
                INSERT INTO Users(full_name, username, email, password,user_type)
                VALUES
                (?, ?, ?, ?, ?);
            ''', (full_name, username, email, password, user_type))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True
