# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: this is the model/class to access the Users table
class Ticket:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to create table on the database
    def createTicketTable(self):
        try:
            self.connObj.getCursor().execute('''
                    CREATE TABLE IF NOT EXISTS Tickets(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_id INT NOT NULL,
                    ticket_type VARCHAR(10) NOT NULL,
                    price FLOAT NOT NULL,
                    seat_position VARCHAR(10) NOT NULL,
                    customer_id INT NOT NULL,
                    user_id INT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (movie_id) 	REFERENCES Movies(id),
                    FOREIGN KEY (customer_id) REFERENCES Customers(id),
                    FOREIGN KEY (user_id) REFERENCES Users(id));
                ''')
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to drop the customer table
    def dropTicketTable(self):
        try:
            self.connObj.getCursor().execute('''
                    DROP TABLE IF EXISTS Tickets;
                ''')
        except:
            return False
        else:
            return True

    # method to insert into customers table
    def insertData(self, movie_id, ticket_type, price, seat_position, customer_id, user_id):
        try:
            self.connObj.getCursor().execute('''
                    INSERT INTO Tickets(movie_id, ticket_type, price, seat_position, customer_id, user_id)
                    VALUES
                    (?, ?, ?, ?, ?, ?);
                ''', (movie_id, ticket_type, price, seat_position, customer_id, user_id))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # method to delete the model
    def deleteDataById(self, ticket_id):
        try:
            self.connObj.getCursor().execute('''
                DELETE FROM Tickets
                WHERE
                id = ?;
            ''', (ticket_id,))
            self.connObj.commitChanges()
        except:
            return False
        else:
            return True

    # function to get the ticket by id
    def getDataById(self, ticket_id):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Tickets
                WHERE
                id = ?;
            ''', (ticket_id,))
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # function to get all data
    def getAllData(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT * FROM Tickets
            ''')
            rows = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return rows
