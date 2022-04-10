from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter import filedialog
from PIL import Image, ImageTk
from Models.UserModel import User
from Models.ConnectionModel import Connection

connectionObject = Connection("../Database/database.db")

def main():
    root = Tk()
    LoginWindow(root)

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Ticket Booking System")
        # self.master.configure(bg='grey')
        self.master.resizable(False, False)
        self.master.state('zoomed')
        self.open_login_window()
        self.master.mainloop()

    def open_login_window(self):
        # login frame
        self.login_frame = Frame(self.master, height=500, width=400, bg='white')
        self.login_frame.place(relx=.5, rely=.5, anchor=CENTER)
        # login header label
        self.header_label = Label(self.login_frame, fg='#095e79', bg='white', text='Please Login')
        self.header_label.grid(row=0, column=0, pady=10, sticky="ns,ew")
        # login username label and entry
        self.username_label = Label(self.login_frame, fg='#095e79', bg='white', text='Username')
        self.username_label.grid(row=1, column=0, sticky="w", padx=10)
        self.login_username = StringVar()
        self.username_entry = Entry(self.login_frame, width=40, textvariable=self.login_username)
        self.username_entry.grid(row=2, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # login password label and entry
        self.password_label = Label(self.login_frame, fg='#095e79', bg='white', text='Password')
        self.password_label.grid(row=3, column=0, sticky="w", padx=10)
        self.login_password = StringVar()
        self.password_entry = Entry(self.login_frame, width=40, show='*', textvariable=self.login_password)
        self.password_entry.grid(row=4, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # login button
        self.login_btn = Button(self.login_frame, text='LOGIN', command=self.app_window,bg='#095e79', fg='white', width=20)
        self.login_btn.grid(row=5, column=0, padx=10, pady=10, sticky="ew,ns")
        # signup label and button
        self.signup_label = Label(self.login_frame, text="Don't have an account?", bg='white', fg='#095e79')
        self.signup_label.grid(row=6, column=0, sticky="sw", padx=10)
        self.signup_btn = Button(self.login_frame, text='Sign Up',command=self.open_signup_window,fg='#095e79',bg='white', width=10,border=0)
        self.signup_btn.grid(row=6, column=0, sticky="se")

    def open_signup_window(self):
        def show_login():
            self.signup_frame.destroy()
            self.open_login_window()

        self.login_frame.destroy()
        # signup frame
        self.signup_frame = Frame(self.master, height=500, width=400, bg='white')
        self.signup_frame.place(relx=.5, rely=.5, anchor=CENTER)
        # signup header label
        self.signupheader_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Please Sign Up')
        self.signupheader_label.grid(row=0, column=0, pady=10, sticky="ns,ew")
        # signup fullname label and entry
        self.fullname_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Full Name')
        self.fullname_label.grid(row=1, column=0, sticky="w", padx=10)
        self.signup_fullname = StringVar()
        self.fullname_entry = Entry(self.signup_frame, width=40, textvariable=self.signup_fullname)
        self.fullname_entry.grid(row=2, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # signup email label and entry
        self.email_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Email')
        self.email_label.grid(row=3, column=0, sticky="w", padx=10)
        self.signup_email = StringVar()
        self.email_entry = Entry(self.signup_frame, width=40, textvariable=self.signup_email)
        self.email_entry.grid(row=4, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # signup username label and entry
        self.username_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Username')
        self.username_label.grid(row=5, column=0, sticky="w", padx=10)
        self.signup_username = StringVar()
        self.username_entry = Entry(self.signup_frame, width=40, textvariable=self.signup_username)
        self.username_entry.grid(row=6, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # signup password label and entry
        self.password_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Password')
        self.password_label.grid(row=7, column=0, sticky="w", padx=10)
        self.signup_password = StringVar()
        self.password_entry = Entry(self.signup_frame, width=40, show='*', textvariable=self.signup_password)
        self.password_entry.grid(row=8, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # signup confirm password label and entry
        self.confirm_password_label = Label(self.signup_frame, fg='#095e79', bg='white', text='Confirm Password')
        self.confirm_password_label.grid(row=9, column=0, sticky="w", padx=10)
        self.signup_confirm_password = StringVar()
        self.confirm_password_entry = Entry(self.signup_frame, width=40, show='*', textvariable=self.signup_confirm_password)
        self.confirm_password_entry.grid(row=10, column=0, padx=10, pady=10, ipadx=5, ipady=3)
        # signup button
        self.signup_btn = Button(self.signup_frame, command=self.sign_up,text='SIGN UP', bg='#095e79', fg='white', width=20)
        self.signup_btn.grid(row=11, column=0, padx=10, pady=10, sticky="ew,ns")
        # back button
        self.back_btn = Button(self.signup_frame, command=show_login, text='BACK', bg='green', fg='white', width=20)
        self.back_btn.grid(row=12, column=0, padx=10, pady=10, sticky="ew,ns")

    def app_window(self):
        # login validation goes here
        # self.loginUsername = self.login_username.get()
        # self.loginPassword = self.login_password.get()
        # if(self.loginUsername =='' or self.loginPassword==''):
        #     messagebox.showerror('Error!', 'Please enter username and password to login!')
        # elif(self.loginUsername=='chiran' and self.loginPassword=='11'):
        #     self.main_app_window = Frame(self.master)
        #     self.main_app_window.grid(row=0, column=0)
        #     self.login_frame.destroy()
        #     AppWindow(self.main_app_window)
        # else:
        #     messagebox.showerror('Error!', 'Username and Password does not match!')

        self.main_app_window = Frame(self.master)
        self.main_app_window.grid(row=0, column=0)
        self.login_frame.destroy()
        AppWindow(self.main_app_window)

    def sign_up(self):
        user = User(connectionObject)
        fullname = self.signup_fullname.get()
        username=self.signup_username.get()
        email=self.signup_email.get()
        password=self.signup_password.get()
        re_password=self.signup_confirm_password.get()
        if user.insertData(fullname,username,email,password,"ADMIN"):
            messagebox.showinfo('Signup Successfull!','Congrats! You are now signed in. Please go back to login page for login.')
            self.fullname_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.confirm_password_entry.delete(0, END)
        else:
            messagebox.showerror("Signup Failed!","User not created.")


class AppWindow:
    def __init__(self,master):
        self.master = master
        self.open_main_window()

    def open_main_window(self):
        # movie frame
        self.movie_frame = Frame(self.master, bg="white")
        self.movie_frame.grid(row=0, column=0, padx=20, pady=20,sticky="nw")

        # movie seat frame
        self.seat_frame = Frame(self.master, bg="white")
        self.seat_frame.grid(row=0, column=1, padx=20, pady=20,sticky="e")

        self.add_movie_btn = Button(self.movie_frame, command=self.add_movie_screen,width=25, text="Add Movie", bg="#095e79", fg="white")
        self.add_movie_btn.grid(row=0, column=0, padx=10, pady=10)

        self.book_movie_label = Label(self.seat_frame,text="Click on movie seat below to book movie ticket!", fg="#095e79", bg="white")
        self.book_movie_label.grid(row=0, column=0, padx=10, pady=10,columnspan=10)

        seat_status = [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

        current_state = 0
        for i in range(6):
            for j in range(10):
                if seat_status[current_state] == 0:
                    self.movie_seat_btn = Button(self.seat_frame,state=NORMAL,command=self.book_movie_screen,width=8,height=2,text=(i*10)+1 +j,bg="green",fg="white")
                    self.movie_seat_btn.grid(row=i+1, column=j, padx=5, pady=5)
                else:
                    self.movie_seat_btn = Button(self.seat_frame, state=NORMAL, command=self.book_movie_screen, width=8,
                                                 height=2, text=(i * 10) + 1 + j, bg="red", fg="white")
                    self.movie_seat_btn['state']=DISABLED
                    self.movie_seat_btn.grid(row=i + 1, column=j, padx=5, pady=5)

                current_state += 1

    def add_movie_screen(self):
        def add_movie():
            messagebox.showinfo('Movie Added!','A movie is added successfully!')

        def upload_movie_image():
            global img
            image_path = filedialog.askopenfilename(parent=self.add_movie_window)
            img = Image.open(image_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.image_label = Label(self.add_movie_window, image=img, bg="white")
            self.image_label.grid(row=6, column=0,sticky="ns,ew",padx=10, pady=5)

        self.add_movie_window= Toplevel(self.movie_frame)
        self.add_movie_window.title("Add a Movie")
        self.add_movie_window.configure(bg="white")
        self.add_movie_window.resizable(False, False)

        self.movie_header_label= Label(self.add_movie_window, text="Add a Movie",fg="#095e79",bg="white")
        self.movie_header_label.grid(row=0, column=0, sticky="ns,ew",padx=5, pady=5)

        self.movie_name_label = Label(self.add_movie_window, text="Movie Name",fg="#095e79",bg="white")
        self.movie_name_label.grid(row=1, column=0, sticky="w",padx=10, pady=5)
        self.movie_name = StringVar()
        self.movie_name_entry = Entry(self.add_movie_window, textvariable=self.movie_name)
        self.movie_name_entry.grid(row=2, column=0, padx=10, pady=5, sticky="ns,ew",ipady=5)
        self.movie_type_label = Label(self.add_movie_window, text="Movie Type",fg="#095e79",bg="white")
        self.movie_type_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.movie_type= StringVar()
        self.movie_type_box = ttk.Combobox(self.add_movie_window, textvariable=self.movie_type, width=45)
        self.movie_type_box['values'] = ('Comedy','Sci-Fi','Horror','Mystery','Thriller')
        self.movie_type_box['state']  = 'readonly'
        self.movie_type_box.grid(row=4, column=0, padx=10, pady=5, sticky="w",ipady=3)
        self.movie_image_label = Label(self.add_movie_window, text="Upload Image",fg="#095e79",bg="white")
        self.movie_image_label.grid(row=5,column=0,padx=10, pady=5, sticky="w")
        self.movie_img_upload_btn = Button(self.add_movie_window, width=10,command=upload_movie_image,text="Browse",bg="green",fg="white")
        self.movie_img_upload_btn.grid(row=5,column=0,padx=10, pady=5, sticky="e")
        self.release_date_label = Label(self.add_movie_window, text="Release Date",fg="#095e79",bg="white")
        self.release_date_label.grid(row=7, column=0, sticky="w",padx=10, pady=5)
        self.release_date_entry = DateEntry(self.add_movie_window,width=45)
        self.release_date_entry.grid(row=8, column=0, sticky="w",padx=10, pady=5,ipady=3)
        self.add_movie_btn = Button(self.add_movie_window, command=add_movie,text="Add Movie",bg="#095e79",fg="white")
        self.add_movie_btn.grid(row=9, column=0, sticky="ns,ew",padx=10, pady=10)

    def book_movie_screen(self):
        def book_movie():
            print("")

        self.book_movie_window = Toplevel(self.seat_frame)
        self.book_movie_window.title("Book Movie Ticket")
        self.book_movie_window.configure(bg="white")
        self.book_movie_window.resizable(False, False)

        self.book_movie_header_label = Label(self.book_movie_window, text="Book Movie Ticket", fg="#095e79", bg="white")
        self.book_movie_header_label.grid(row=0, column=0, sticky="ns,ew", padx=5, pady=5)

        self.book_movie_name_label = Label(self.book_movie_window, text="Full Name", fg="#095e79", bg="white")
        self.book_movie_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.book_movie_name = StringVar()
        self.book_movie_name_entry = Entry(self.book_movie_window,width=40, textvariable=self.book_movie_name)
        self.book_movie_name_entry.grid(row=2, column=0, padx=10, pady=5, sticky="ns,ew", ipady=5)
        self.book_movie_email_label = Label(self.book_movie_window, text="Email", fg="#095e79", bg="white")
        self.book_movie_email_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.book_movie_email = StringVar()
        self.book_movie_email_entry = Entry(self.book_movie_window, width=40, textvariable=self.book_movie_email)
        self.book_movie_email_entry.grid(row=4, column=0, padx=10, pady=5, sticky="ns,ew", ipady=5)
        self.book_movie_gender_label = Label(self.book_movie_window, text="Gender", fg="#095e79", bg="white")
        self.book_movie_gender_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.book_movie_gender = StringVar()
        self.book_movie_gender_box = ttk.Combobox(self.book_movie_window, textvariable=self.book_movie_gender, width=45)
        self.book_movie_gender_box['values'] = ('Male','Female','Others')
        self.book_movie_gender_box['state'] = 'readonly'
        self.book_movie_gender_box.grid(row=6, column=0, padx=10, pady=5, sticky="w", ipady=3)
        self.book_movie_age_label = Label(self.book_movie_window, text="Age", fg="#095e79", bg="white")
        self.book_movie_age_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.book_movie_age = StringVar()
        self.book_movie_age_entry = Entry(self.book_movie_window, width=40, textvariable=self.book_movie_age)
        self.book_movie_age_entry.grid(row=8, column=0, padx=10, pady=5, sticky="ns,ew", ipady=5)
        self.book_movie_tickettype_label = Label(self.book_movie_window, text="Ticket Type", fg="#095e79", bg="white")
        self.book_movie_tickettype_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.book_movie_tickettype = StringVar()
        self.book_movie_tickettype_box = ttk.Combobox(self.book_movie_window, textvariable=self.book_movie_tickettype, width=45)
        self.book_movie_tickettype_box['values'] = ('Gold', 'Silver', 'Platinum')
        self.book_movie_tickettype_box['state'] = 'readonly'
        self.book_movie_tickettype_box.grid(row=10, column=0, padx=10, pady=5, sticky="w", ipady=3)
        self.book_movie_ticketprice_label = Label(self.book_movie_window, text="Price", fg="#095e79", bg="white")
        self.book_movie_ticketprice_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.book_movie_ticketprice = StringVar()
        self.book_movie_ticketprice_entry = Entry(self.book_movie_window, width=40, textvariable=self.book_movie_ticketprice)
        self.book_movie_ticketprice_entry.grid(row=12, column=0, padx=10, pady=5, sticky="ns,ew", ipady=5)
        self.book_movie_btn = Button(self.book_movie_window, command=book_movie, text="Add Movie", bg="#095e79",fg="white")
        self.book_movie_btn.grid(row=13, column=0, sticky="ns,ew", padx=10, pady=10)


if __name__ == "__main__":
    main()

