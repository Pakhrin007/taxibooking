import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class customer_form:
    def __init__(self,root,username,id):
        self.root = root
        self.root.title("Taxi Booking")
        self.root.geometry("1100x600+100+25")
        self.root.resizable(0, 0)
        self.root.config(bg="#1F5776")
        self.customerform()
        self.id=id
        
        
        
        self.logged_in_user_id = None
        self.indicator(self.home_indicator,self.home_page) 
        # icon
        icon = tk.PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)
        fr=tk.Label(self.root,text=f"welcome {username}",font=(50), bg="white",fg="firebrick1",bd=2)
        fr.place(x=2,y=2)
        

    def customerform(self):

        options_frame =tk. Frame(self.root, bg='#E9ECEE')
       

        
        home_btn = tk.Button(options_frame, text="Home", font=('bold', 15),
                          fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2",
                          command=lambda: self.indicator(self.home_indicator,self.home_page))

        home_btn.place(x=25, y=130)

        self.home_indicator = tk.Label(options_frame, text="", bg='#E9ECEE')
        self.home_indicator.place(x=18, y=130, width=5, height=35)

        self.home1_btn = tk.Button(options_frame, text="Book taxi", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2",
                           command=lambda: self.indicator(self.home1_indicator,self.book_page))
        self.home1_btn.place(x=25, y=200)
        self.home1_indicator = tk.Label(options_frame, text="", bg='grey')
        self.home1_indicator.place(x=18, y=200, width=5, height=35)




        home2_btn = tk.Button(options_frame, text="Logout", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2",
                           command=lambda: self.indicator(self.home2_indicator,self.logout))
        home2_btn.place(x=25, y=340)
        self.home2_indicator = tk.Label(options_frame, text="", bg='grey')
        self.home2_indicator.place(x=18, y=340, width=5, height=35)

        home3_btn = tk.Button(options_frame, text="profile", font=('bold', 15),
                           fg="firebrick1", bd=0, bg="#E9ECEE", cursor="hand2",
                           command=lambda: self.indicator(self.home3_indicator,self.profile_page))
        home3_btn.place(x=25, y=270)
        self.home3_indicator = tk.Label(options_frame, text="", bg='grey')
        self.home3_indicator.place(x=18, y=270, width=5, height=35)


        options_frame.pack(side=tk.LEFT)
        options_frame.configure(width=200, height=500)

        self.main_frame = tk.Frame(self.root, highlightbackground="black", highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=880)

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
    
    

    def indicator(self, a,page):
        self.hide()
        a.config(bg="aqua")
        self.delete_page()
        page()

    def home_page(self):
        home_frame=tk.Frame(self.main_frame)

        lb=tk.Label(home_frame,text="Welcome!!!",font=('Baskerville Old Face',20,"bold underline"),fg="firebrick1")
        lb.pack()
        lb2 = tk.Label(home_frame, text="Need a taxi?", font=('Baskerville Old Face', 20, "bold underline"),fg='firebrick1')
        lb2.pack(pady=50)
        lb2 = tk.Label(home_frame, text="Running late?\n book your taxi right now easy and comfortable ", font=("Baskerville Old Face", 20, "bold"),fg='firebrick1')
        lb2.pack(pady=60)
       
        home_frame.pack(pady=20)

    def book_page(self):
        mainframe=tk.Frame(self.main_frame,width=500,height=500,relief="ridge")
        mainframe.grid()

        titleframe=tk.Frame(mainframe,bd=5,width=770,height=100,relief="ridge",bg="#1F5776")
        titleframe.grid(row=0,column=0)
        topframe3=tk.Frame(mainframe,bd=5,width=770,height=500,relief="ridge")
        topframe3.grid(row=1,column=0)

        leftframe=tk.Frame(topframe3,bd=5,width=770,height=400,padx=12,relief="ridge",bg="#1F5776")
        leftframe.pack(side="left")
        leftframe1=tk.Frame(leftframe,bd=5,width=600,height=180,padx=12,pady=9,relief="ridge")
        leftframe1.pack(side="top",padx=0,pady=0)

        rightframe1=tk.Frame(topframe3,bd=5,width=100,height=400,relief="ridge",bg="#1F5776",padx=2)
        rightframe1.pack(side="right")
        rightframela=tk.Frame(rightframe1,bd=5,width=90,height=300,relief="ridge",padx=2,pady=2)
        rightframela.pack(side="top")
        #==================================

        self.pickup_address=tk.StringVar()
        self.dropoff_address=tk.StringVar()
        self.time=tk.StringVar()
        self.date=tk.StringVar()

        #==================================
        

        self.lbtitle=tk.Label(titleframe,font=("arial",30,'bold'),text="Book your taxi",bd=7,width=20)
        self.lbtitle.grid()
        #======================================
        self.lblcustomerID=tk.Label(leftframe1,font=('arial',12,'bold'),text="pickup_address",bd=7)
        self.lblcustomerID.grid(row=0,column=0)
        self.encustomerID=tk.Entry(leftframe1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=self.pickup_address)
        self.encustomerID.grid(row=0,column=1,sticky="w",padx=5)

        self.droplblcustomerID=tk.Label(leftframe1,font=('arial',12,'bold'),text="dropoff_address",bd=7)
        self.droplblcustomerID.grid(row=1,column=0)
        self.dropencustomerID=tk.Entry(leftframe1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=self.dropoff_address)
        self.dropencustomerID.grid(row=1,column=1,sticky="w",padx=5)
        
        self.timelblcustomerID=tk.Label(leftframe1,font=('arial',12,'bold'),text="Time",bd=7)
        self.timelblcustomerID.grid(row=2,column=0)
        self.timeencustomerID=tk.Entry(leftframe1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=self.time)
        self.timeencustomerID.grid(row=2,column=1,sticky="w",padx=5)

        self.datelblcustomerID=tk.Label(leftframe1,font=('arial',12,'bold'),text="Date",bd=7)
        self.datelblcustomerID.grid(row=3,column=0)
        self.dateencustomerID=tk.Entry(leftframe1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=self.date)
        self.dateencustomerID.grid(row=3,column=1,sticky="w",padx=5)

        #===================================================


        

        self.customer_records=ttk.Treeview(leftframe,height=14,columns=("Booking_id","pickup_address","dropoff_address","time","date"))
        
        
        self.customer_records.heading("Booking_id",text="Booking_id")
        self.customer_records.heading("pickup_address",text="pickup_address")
        self.customer_records.heading("dropoff_address",text="dropoff_address")
        self.customer_records.heading("time",text="time")
        self.customer_records.heading("date",text="date")
        


        self.customer_records["show"]="headings"

        self.customer_records.column("Booking_id",width=90)
        self.customer_records.column("pickup_address",width=90)
        self.customer_records.column("dropoff_address",width=90)
        self.customer_records.column("time",width=90)
        self.customer_records.column("date",width=90)
       
    

        self.customer_records.pack(fill="both",expand=1)
        self.customer_records.bind("<ButtonRelease-1>", self.on_record_selected)

        


    # buttons

        self.btn=tk.Button(rightframela,font=("arial",16,"bold"),text="Book",bd=4,pady=1,padx=24,width=8,height=2,command=self.book).grid(row=0,column=0,padx=1)
        self.btn1=tk.Button(rightframela,font=("arial",16,"bold"),text="view",bd=4,pady=1,padx=24,width=8,height=2,command=self.display).grid(row=1,column=0,padx=1)
       
        self.btn2=tk.Button(rightframela,font=("arial",16,"bold"),text="Clear",bd=4,pady=1,padx=24,width=8,height=2,command=self.clear).grid(row=3,column=0,padx=1)
        self.btn3=tk.Button(rightframela,font=("arial",16,"bold"),text="cancel booking",bd=4,pady=1,padx=24,width=8,height=2,command=self.delete).grid(row=4,column=0,padx=1)

        
    #=================================================== 
    def clear(self):
        self.encustomerID.delete(0, tk.END)
        self.dropencustomerID.delete(0, tk.END)
        self.timeencustomerID.delete(0, tk.END)
        self.dateencustomerID.delete(0, tk.END)
    
        
    #===================================================
        
    def book(self):
        if self.encustomerID.get()=="" or self.dropencustomerID.get()=="" or self.timeencustomerID.get()=="" or self.dateencustomerID.get()=="":
            messagebox.showerror("error","enter the correct details")

        else:
            
           
            sqlcon = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
            cur = sqlcon.cursor()
            
            # query="CREATE TABLE customer24 (booking_id INT AUTO_INCREMENT PRIMARY KEY,pickup_address VARCHAR(50),dropoff_address VARCHAR(100),time VARCHAR(20),date VARCHAR(50),id int)"
            # cur.execute(query)
            cur.execute("INSERT INTO customer24 (id,pickup_address, dropoff_address, time, date) VALUES (%s, %s, %s, %s,%s)",
            (self.id,self.pickup_address.get(), self.dropoff_address.get(), self.time.get(), self.date.get()))

            sqlcon.commit()
            sqlcon.close()
            messagebox.showinfo("success","booking is successful")
            self.clear()
       
      #===================================================
    
    

     #===================================================
    def delete(self):
        selected_item = self.customer_records.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete")
            return

        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
        if confirmation:
            record_id = int(self.customer_records.item(selected_item, 'values')[0])

            sqlcon = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
            cur = sqlcon.cursor()

            cur.execute("DELETE FROM customer24 WHERE booking_id = %s", (record_id,))

            sqlcon.commit()
            sqlcon.close()

            self.customer_records.delete(selected_item)
            messagebox.showinfo("Success", "Record deleted successfully")



    def display(self):
        # Clear existing records from the Treeview
        self.customer_records.delete(*self.customer_records.get_children())

        # Fetch and insert new records
        sqlcon = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
        cursor = sqlcon.cursor()
        query = f"SELECT booking_id, pickup_address, dropoff_address, time, date FROM customer24 WHERE id={self.id}"

        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            self.customer_records.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

        sqlcon.close()
    #===================================================

    def on_record_selected(self, event):
        selected_item = self.customer_records.selection()
        if selected_item:
            learner_data = self.customer_records.item(selected_item)
            row = learner_data['values']
            
            self.pickup_address.set(row[1])
            self.dropoff_address.set(row[2])
            self.time.set(row[3])
            self.date.set(row[4])
        else:
            messagebox.showinfo("Info", "Please select a record")



   
    #===================================================

    def profile_page(self):
        self.booking_tree = ttk.Treeview(self.main_frame, columns=("ID", "username", "phone_number", "address","e_mail"),
                                         show="headings", height=10)
        self.booking_tree.heading("ID", text="ID")
        self.booking_tree.heading("username", text="username")
        self.booking_tree.heading("phone_number", text="phone_number")
        self.booking_tree.heading("address", text="address")
        self.booking_tree.heading("e_mail", text="e_mail")
        
        

        # Set column widths
        self.booking_tree.column("ID", width=100, anchor="center")
        self.booking_tree.column("username", width=100, anchor="center")
        self.booking_tree.column("phone_number", width=100, anchor="center")
        self.booking_tree.column("address", width=100, anchor="center")
        self.booking_tree.column("e_mail", width=200, anchor="center")
      
        
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
        query=f"select * from used where id={self.id}"
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            self.booking_tree.insert("","end",values=(row[0],row[1],row[2],row[3],row[4]))

    
    #====================================================

    def hide(self):
        self.home_indicator.config(bg="grey")
        self.home1_indicator.config(bg="grey")
        self.home2_indicator.config(bg="grey")
        self.home3_indicator.config(bg="grey")
       

    def logout(self):
       
        self.root.destroy()
        
        root = tk.Tk()
        
        from login import Login_form
        Login_form(root)
       

if __name__ == "__main__":
    root =tk. Tk()
    ob = customer_form(root)
    root.mainloop()
