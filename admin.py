from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import pymysql

class admin_form:
    def __init__(self, root,):
        self.root = root
        self.root.title("Taxi Booking")
        self.root.geometry("1100x600+100+25")
        self.root.resizable(0, 0)
        self.root.config(bg="#1F5776")
        self.adminform()
        self.selected_driver_id = StringVar()
        self.driver_combobox = None
        self.show_home()
        self.id=id
        


    def adminform(self):
        options_frame = Frame(self.root, bg="#E9ECEE")

        home_btn = Button(options_frame, text="Home", font=('bold', 15),
                          fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2", command=self.show_home)
        home_btn.place(x=25, y=130)

        home1_btn = Button(options_frame, text="customer details", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2", command=self.show_customer_details)
        home1_btn.place(x=25, y=200)

        home2_btn = Button(options_frame, text="driver details", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2", command=self.show_driver_details)
        home2_btn.place(x=25, y=270)

        home3_btn = Button(options_frame, text="Logout", font=('bold', 15),
                           fg="firebrick1", bd=0,bg="#E9ECEE", cursor="hand2", command=self.logout)
        home3_btn.place(x=25, y=340)

        options_frame.pack(side=LEFT)
        options_frame.configure(width=200, height=500)

        self.main_frame = Frame(self.root, highlightbackground="black", highlightthickness=2)
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=880)
        
    

    def show_home(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        driver_ids = [str(driver[0]) for driver in self.fetch_registered_driver_details()]

        
        if self.driver_combobox:
            self.driver_combobox.destroy()

        self.driver_combobox = ttk.Combobox(self.main_frame, textvariable=self.selected_driver_id, values=[], state="readonly")
        self.driver_combobox.set("Select Driver ID")
        self.driver_combobox.pack(side=TOP, pady=10)

     
        self.driver_combobox['values'] = driver_ids
        self.driver_combobox.set("Select Driver ID")

        self.selected_driver_label = Label(self.main_frame, text="", font=('bold', 15))
        self.selected_driver_label.pack(pady=10)

        
        self.booking_tree = ttk.Treeview(self.main_frame, columns=("booking_ID", "pickup_address", "dropoff_address", "time", "date","user_id"),
                                         show="headings", height=10)

     
        self.booking_tree.heading("booking_ID", text="booking_ID")
        self.booking_tree.heading("pickup_address", text="pickup_address")
        self.booking_tree.heading("dropoff_address", text="dropoff_address")
        self.booking_tree.heading("time", text="time")
        self.booking_tree.heading("date", text="date")
        self.booking_tree.heading("user_id", text="user_id")
        

      
        self.booking_tree.column("booking_ID", width=100, anchor="center")
        self.booking_tree.column("pickup_address", width=100, anchor="center")
        self.booking_tree.column("dropoff_address", width=100, anchor="center")
        self.booking_tree.column("time", width=100, anchor="center")
        self.booking_tree.column("date", width=100, anchor="center")
        self.booking_tree.column("user_id", width=100, anchor="center")
        
        self.fn1()

        self.booking_tree.pack(side=TOP, expand=YES, fill=BOTH)
        home_page_button = Button(self.main_frame, text="Assign-driver", font=('bold', 15),
                                  fg="firebrick1", bd=0, bg="grey", cursor="hand2", command=self.home_page_button_click)
        home_page_button.pack(pady=10)
    def fn1(self):
        booking_details = self.booking_details()
        for bookings in booking_details:
            self.booking_tree.insert("", "end", values=bookings)

    def home_page_button_click(self):
        selected_driver_id = self.selected_driver_id.get()
        if not selected_driver_id or selected_driver_id == "Select Driver ID":
            messagebox.showinfo("Information", "Please select a driver ID.")
            return

        self.assign_driver(selected_driver_id)

    def assign_driver(self, driver_id):
        selected_item = self.booking_tree.selection()
    
    
        if not selected_item:
            messagebox.showinfo("Information", "Please select a booking.")
            return

        selected_values = self.booking_tree.item(selected_item, "values")

    
        if selected_values:
            selected_id = selected_values[0]
            print(selected_id, driver_id)
            messagebox.showinfo("success", "Successfully assigned driver")
            self.booking_tree.delete(selected_item)
        else:
            messagebox.showerror("error", "Select a valid booking.")

    
        

    def clear_booking_tree(self):
        self.booking_tree.delete(*self.booking_tree.get_children())

    def open_driver2_form(self, driver_id, selected_data):
        from driver2 import driver2_form
         
        driver2_form(root, driver_id, selected_data)

    def get_selected_booking(self):
        selected_item = self.booking_tree.selection()
        if selected_item:
            selected_booking = self.booking_tree.item(selected_item, 'values')
            return selected_booking

        return None

    def view_driver_details(self, driver_id):
        if not driver_id or driver_id == "Select Driver ID":
            messagebox.showinfo("Information", "Please select a driver ID.")
            return
        self.display_selected_driver_id(driver_id)

    def display_selected_driver_id(self, driver_id):
        self.selected_driver_label.config(text=f"Selected Driver ID: {driver_id}")

    def booking_details(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789")
            mycursor = con.cursor()
            mycursor.execute('use db1')
            query = "SELECT booking_id, pickup_address, dropoff_address, time, date,id FROM customer24"
            mycursor.execute(query)
            booking_details = mycursor.fetchall()
            con.close()
            return booking_details
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database connectivity problem: {e}")
            return []

    def show_driver_details(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "License Plate"), show="headings", height=20)

        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("License Plate", text="License Plate")

        tree.column("ID", width=100, anchor="center")
        tree.column("Name", width=300, anchor="center")
        tree.column("License Plate", width=200, anchor="center")

        registered_driver_details = self.fetch_registered_driver_details()

        for driver in registered_driver_details:
            tree.insert("", "end", values=driver)

        tree.pack(expand=YES, fill=BOTH)

    def fetch_registered_driver_details(self, driver_id=None):
        try:
            con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789")
            mycursor = con.cursor()
            mycursor.execute('use db1')

            if driver_id:
                query = f"SELECT id, drivername, license_plate FROM driver WHERE id = {driver_id}"
            else:
                query = "SELECT id, drivername, license_plate FROM driver"

            mycursor.execute(query)
            registered_driver_details = mycursor.fetchall()
            con.close()
            return registered_driver_details
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database connectivity problem: {e}")
            return []

    def logout(self):
        self.root.destroy()
        root = Tk()
        from login import Login_form
        Login_form(root)

    def show_customer_details(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "number", "address", "e_mail"), show="headings",
                            height=20)

        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("number", text="number", anchor="center")
        tree.heading("address", text="address", anchor="center")
        tree.heading("e_mail", text="e_mail", anchor="center")

        tree.column("ID", width=50, anchor="center")
        tree.column("Name", width=100, anchor="center")
        tree.column("number", width=80, anchor="center")
        tree.column("address", width=120, anchor="center")
        tree.column("e_mail", width=100, anchor="center")

        registered_customer_details = self.fetch_registered_customer_details()

        for customer in registered_customer_details:
            tree.insert("", "end", values=customer)

        tree.pack(expand=YES, fill=BOTH)

    def fetch_registered_customer_details(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789")
            mycursor = con.cursor()
            mycursor.execute('use db1')
            query = "SELECT id, username, number, address, e_mail FROM used"
            mycursor.execute(query)
            registered_customer_details = mycursor.fetchall()
            con.close()
            return registered_customer_details
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Database connectivity problem: {e}")
            return []

if __name__ == "__main__":
    root = Tk()
    ob = admin_form(root)
    root.mainloop()
