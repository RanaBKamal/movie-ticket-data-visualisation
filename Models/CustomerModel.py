# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table

class Customer:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to create table on the database
    def createCustomerTable(self):
        try:
            self.connObj.getCursor().execute('''
                CREATE TABLE IF NOT EXISTS Customers(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name VARCHAR(40) NOT NULL,
                    email VARCHAR(40) NOT NULL UNIQUE,
                    gender VARCHAR(10) NOT NULL,
                    age INT(3) NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
            ''')
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to drop the customer table
    def dropCustomerTable(self):
        try:
            self.connObj.getCursor().execute('''
                DROP TABLE IF EXISTS Customers;
            ''')
        except:
            return False
        else:
            return True

    # method to insert into customers table
    def insertData(self, full_name, email, gender, age):
        try:
            self.connObj.getCursor().execute('''
                INSERT INTO Customers(full_name, email, gender,age)
                VALUES
                (?, ?, ?, ?);
            ''', (full_name, email, gender, age))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to delete the model
    def deleteDataById(self, customer_id):
        try:
            self.connObj.getCursor().execute('''
                DELETE FROM Customers
                WHERE
                id = ?;
            ''', (customer_id,))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # function to get the customer by id
    def getDataById(self, customer_id):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Customers
                WHERE
                id = ?;
            ''', (customer_id,))
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    #method to get data by email
    def getDataByEmail(self, email):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Customers
                WHERE
                email = ?;
            ''', (email,))
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # function to get all data
    def getAllData(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Customers
            ''')
            rows = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return rows