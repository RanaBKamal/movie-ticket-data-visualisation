# Author(Team) : Kamal_Sandip_Chiranjibi
# Written For : Term Project Python II, W22
# Description: model for creaing connection
import sqlite3


class Connection:
    connObj = None
    cursorObj = None
    database = ""

    # constructor
    def __init__(self, database):
        self.database = database
        self.connObj = sqlite3.connect(self.database)
        self.cursorObj = self.connObj.cursor()

    # method to get the connection object
    def getConnection(self):
        if self.connObj is None:
            return None
        else:
            return self.connObj

    # method to get the cursor object
    def getCursor(self):
        if self.cursorObj is None:
            return None
        else:
            return self.cursorObj

    # method to commit changes
    def commitChanges(self):
        self.connObj.commit()

    # method to execute the query directly passing wuery string
    def executeQuery(self, query):
        self.cursorObj.execute(query)

    # method to close the connection
    def closeConnection(self):
        self.connObj.close()
