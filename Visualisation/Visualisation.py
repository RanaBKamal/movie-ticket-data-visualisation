# class to get required data from database for visualisation
import matplotlib.pyplot as plt
import numpy as np


class Visualisation:
    connObj = None

    def __init__(self, connObj):
        self.connObj = connObj

    # method to get movies based on category
    def getMoviesByCategory(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT movie_type, count(*) FROM Movies GROUP BY movie_type;
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # method to visualize data
    def visualizeByMovieCategory(self):
        movies_by_type = self.getMoviesByCategory()
        mov_x_array = []
        mov_y_array = []

        for item in movies_by_type:
            mov_x_array.append(item[0])
            mov_y_array.append(item[1])
        mov_x_np = np.array(mov_x_array)
        mov_y_np = np.array(mov_y_array)
        plt.title("Movie Type(Python II, W22 By: Chiranjibi, Kamal, Sandip)", fontsize=10)
        plt.bar(mov_x_np, mov_y_np)
        plt.xlabel('Movie Type')
        plt.ylabel('Number of movies')
        plt.xticks(rotation=25)
        plt.subplots_adjust(bottom=0.2)
        plt.show()

    # method to get customers based on age group
    def getCustomersByAgeGroup(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT SUM(CASE WHEN age < 18 THEN 1 ELSE 0 END) AS [Under 18],
                    SUM(CASE WHEN age BETWEEN 18 AND 28 THEN 1 ELSE 0 END) AS [18-28],
                    SUM(CASE WHEN age BETWEEN 29 AND 38 THEN 1 ELSE 0 END) AS [29-38],
                    SUM(CASE WHEN age BETWEEN 39 AND 48 THEN 1 ELSE 0 END) AS [39-48],
                    SUM(CASE WHEN age BETWEEN 49 AND 58 THEN 1 ELSE 0 END) AS [49-58],
                    SUM(CASE WHEN age BETWEEN 59 AND 100 THEN 1 ELSE 0 END) AS [59-100]
                FROM Customers
                ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # method to visualize data
    def visualizeCustomersByAgeGroup(self):
        customers_by_age_group = self.getCustomersByAgeGroup()
        mov_x_array = ["Under 18", "18-28", "29-38", "39-48", "49-58", "59-100"]
        mov_y_array = []

        for item in customers_by_age_group[0]:
            mov_y_array.append(item)
        mov_x_np = np.array(mov_x_array)
        mov_y_np = np.array(mov_y_array)
        plt.title("Age Group(Python II, W22 By: Chiranjibi, Kamal, Sandip)", fontsize=10)
        plt.bar(mov_x_np, mov_y_np)
        plt.xlabel('Age Group')
        plt.ylabel('Number of People')
        plt.xticks(rotation=25)
        plt.subplots_adjust(bottom=0.2)
        plt.show()

    # method to visualise number of tickets based on date
    def getTicketsByDate(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT strftime('%Y-%m', created_at) year_month, COUNT(*)
                FROM Tickets
                GROUP BY year_month
                ORDER BY year_month ASC
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # method to get line chart based on date
    def visualiseTicketsByDate(self):
        tick_by_date = self.getTicketsByDate()
        tick_y_array = []
        tick_x_array = []
        for item in tick_by_date:
            tick_x_array.append(item[0])
            tick_y_array.append(item[1])
        y_points = np.array(tick_y_array)
        x_points = np.array(tick_x_array)

        plt.plot(x_points, y_points, linestyle='solid')
        plt.title("Ticket sold by Date(Python II, W22 By: Chiranjibi, Kamal, Sandip)", fontsize=10)
        plt.xlabel('Year and Month')
        plt.ylabel('Number of Tickets')
        plt.xticks(rotation=25)
        plt.subplots_adjust(bottom=0.2)
        plt.show()

    #method to get gender based data
    def getCustomersByGender(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT gender, COUNT(*)
                FROM Customers
                GROUP BY gender
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    #method to visualise gender based data
    def visualiseCustomersByGender(self):
        customers_by_gender = self.getCustomersByGender()
        cust_x_array = []
        cust_y_array = []
        for item in customers_by_gender:
            cust_y_array.append(item[0])
            cust_x_array.append(item[1])
        my_labels = cust_y_array
        np_x_array = np.array(cust_x_array)
        plt.pie(np_x_array, labels=my_labels)
        plt.title("Gender Based (Python II, W22 By: Chiranjibi, Kamal, Sandip)", fontsize=10)
        plt.show()

    # method to get tickets by its type
    def getTicketsByType(self):
        try:
            self.connObj.getCursor().execute('''
                SELECT ticket_type, count(*) FROM Tickets GROUP BY ticket_type;
            ''')
            row = self.connObj.getCursor().fetchall();
        except:
            return False
        else:
            return row

    # method to visualise by ticket type
    def visualizeTicketsByType(self):
        tickets_by_type = self.getTicketsByType()
        tick_x_array = []
        tick_y_array = []

        for item in tickets_by_type:
            tick_x_array.append(item[0])
            tick_y_array.append(item[1])
        tick_x_np = np.array(tick_x_array)
        tick_y_np = np.array(tick_y_array)
        plt.title("Ticket Type(Python II, W22 By: Chiranjibi, Kamal, Sandip)", fontsize=10)
        plt.bar(tick_x_np, tick_y_np)
        plt.xlabel('Ticket Type')
        plt.ylabel('Number of Tickets')
        plt.xticks(rotation=25)
        plt.subplots_adjust(bottom=0.2)
        plt.show()