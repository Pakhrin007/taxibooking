from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql

class driver2_form:
    def __init__(self, root,username,id):
        self.root = root
        self.root.title("Taxi Booking")
        self.root.geometry("1100x600+100+25")
        self.root.resizable(0, 0)
        self.root.config(bg="#1F5776")
        self.id=id
        

        self.customerform()

        # icon
        icon = PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)
        fr=Label(self.root,text=f"welcome {username}",font=(50), bg="white",fg="firebrick1",bd=2)
        fr.place(x=2,y=2)
        

        self.show_home()

        # List to store completed trips
        self.completed_trips = []

        

    def customerform(self):
        options_frame = Frame(self.root, bg="#E9ECEE")

        home4_btn = Button(options_frame, text="Home", font=('bold', 15),
                           fg="firebrick1", bd=0,bg="#E9ECEE", cursor="hand2", command=self.show_home)
        home4_btn.place(x=25, y=150)

        home3_btn = Button(options_frame, text="Dashboard", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2", command=self.dashboard)
        home3_btn.place(x=25, y=230)

        home2_btn = Button(options_frame, text="profile", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2",command=self.profile_page)
        home2_btn.place(x=25, y=300)


    

        home_btn = Button(options_frame, text="logout", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2", command=self.logout)
        home_btn.place(x=25, y=370)

        options_frame.pack(side=LEFT)
        options_frame.configure(width=200, height=500)

        self.main_frame = Frame(self.root, highlightbackground="black", highlightthickness=2)
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=880)
    def profile_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.booking_tree = ttk.Treeview(self.main_frame, columns=("ID", "drivername", "password", "license_plate"),
                                         show="headings", height=10)
        self.booking_tree.heading("ID", text="ID")
        self.booking_tree.heading("drivername", text="drivername")
        self.booking_tree.heading("password", text="password")
        self.booking_tree.heading("license_plate", text="license_plate")
        
        

        # Set column widths
        self.booking_tree.column("ID", width=100, anchor="center")
        self.booking_tree.column("drivername", width=100, anchor="center")
        self.booking_tree.column("password", width=100, anchor="center")
        self.booking_tree.column("license_plate", width=100, anchor="center")
        
        self.fetch()
        self.booking_tree.pack()
    def fetch(self):
     

        db=pymysql.connect(
            host="localhost",
            user="root",
            password="Aryan@123456789",
            database="db1"


        )
        cursor=db.cursor()
        query=f"select * from driver where id={self.id}"
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            self.booking_tree.insert("","end",values=(row[0],row[1],row[2],row[3]))


    def show_home(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        lab = Label(self.main_frame, text=f"---------------------------------------Welcome!!!!------------------------------------ ", font=("arial", 20), fg="firebrick1")
        lab.place(x=20, y=90)

        lab1 = Label(self.main_frame, text=f"--------------------------------------Driver !!-------------------------- ", font=("arial", 20), fg="firebrick1")
        lab1.place(x=50, y=160)



    def dashboard(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        self.booking_tree = ttk.Treeview(self.main_frame, columns=("ID", "pickup_address", "dropoff_address", "time", "date","user_id"),
                                         show="headings", height=10)

        self.booking_tree.heading("ID", text="ID")
        self.booking_tree.heading("pickup_address", text="pickup_address")
        self.booking_tree.heading("dropoff_address", text="dropoff_address")
        self.booking_tree.heading("time", text="time")
        self.booking_tree.heading("date", text="date")
        self.booking_tree.heading("user_id", text="user_id")
        

        
        self.booking_tree.column("ID", width=100, anchor="center")
        self.booking_tree.column("pickup_address", width=100, anchor="center")
        self.booking_tree.column("dropoff_address", width=100, anchor="center")
        self.booking_tree.column("time", width=100, anchor="center")
        self.booking_tree.column("date", width=100, anchor="center")
        self.booking_tree.column("user_id", width=100, anchor="center")

        
        booking_details = self.booking_details()
        for bookings in booking_details:
            self.booking_tree.insert("", "end", values=bookings)

        self.booking_tree.pack(side=TOP, expand=YES, fill=BOTH)

        
        complete_trip_button = Button(self.main_frame, text="Complete Trip", font=('bold', 15),
                                      fg="firebrick1", bd=0, bg="grey", cursor="hand2", command=self.complete_trip)
        complete_trip_button.pack(pady=10)

    def booking_details(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
            mycursor = con.cursor()
            mycursor.execute("SELECT booking_id, pickup_address, dropoff_address, time, date, id FROM customer24")
            booking_details = mycursor.fetchall()
            con.close()
            return booking_details
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database connectivity problem: {e}")
            return []

    def complete_trip(self):
        selected_item = self.booking_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a booking to complete.")
            return

        confirmation = messagebox.askyesno("Complete Trip", "Are you sure you want to complete this trip?")
        if confirmation:
            item_values = self.booking_tree.item(selected_item, 'values')

            self.booking_tree.delete(selected_item)

            messagebox.showinfo("Success", "Trip Completed!")

        
            self.completed_trips.append(item_values)


    def logout(self):
        self.root.destroy()
        new_root = Tk()
        from login import Login_form
        Login_form(new_root)

if __name__ == "__main__":
    root = Tk()
    ob = driver2_form(root)
    root.mainloop()
