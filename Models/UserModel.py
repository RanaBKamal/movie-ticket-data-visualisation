# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table

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
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            ''')
        except:
            return False
        else:
            return True
        self.connObj.commitChanges()

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
