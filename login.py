from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
class Login_form:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking")
        self.root.geometry("1100x600+100+25")
        self.root.resizable(0, 0)
        self.root.config(bg="white")
        self.loginform()
        # icon
        icon = PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)

    def loginform(self):

        frame=Frame(self.root,bg="white")
        frame.place(x=(10),y=(50),height=600,width=650)
       
        image_path="taxi1.jpg"
        self.img=Image.open(image_path)
        self.img=ImageTk.PhotoImage(self.img)

        label=Label(frame,image=self.img,bd=0)
        label.place(x=0,y=0)
        # frame1
        frame1=Frame(self.root,bg="white")
        frame1.place(x=640,y=20,height=600,width=500)

        Label1=Label(frame1,text="Login-Here",font=("Microsoft Yahel UI Light",20,"bold underline"),fg="firebrick1",bg="white")
        Label1.grid(row=0,column=0,padx=125,pady=(20,0),sticky='w')

        Label2=Label(frame1,text="User-Name",font=("Microsoft Yahel UI Light",14),fg="firebrick1",bg='white')
        Label2.grid(row=1,column=0,padx=90,pady=(20,0),sticky='w')

        self.entry=Entry(frame1,font=("Microsoft Yahel UI Light",14),bg='white')
        self.entry.grid(row=2,column=0,padx=90,pady=(20,0),sticky='w',columnspan=8)

        Label3=Label(frame1,text="password",font=("Microsoft Yahel UI Light",14),fg="firebrick1",bg='white')
        Label3.grid(row=3,column=0,padx=90,pady=(20,0),sticky='w')

        self.entry1=Entry(frame1,font=("Microsoft Yahel UI Light",14),bg='white')
        self.entry1.grid(row=4,column=0,padx=90,pady=(20,0),sticky='w',columnspan=8)

        
            
        forgot_password = Button(frame1, text="forgot password ?",
                             bd=0, bg="white",
                             font=('Microsoft Yahel UI Light ', 10, 'bold'),
                             activebackground="white",
                             activeforeground="firebrick1",
                             cursor="hand2",command=self.forgot_pass)

        forgot_password.grid(row=5,column=0,padx=210,pady=(20,0),sticky='w')

        login_button = Button(frame1, text="Login", font=('Open Sans', 10, 'bold'),
                              fg="white",bg="firebrick1", bd=0,
                              width=29, cursor="hand2",
                              activebackground="firebrick1",
                              activeforeground="white",command=(self.login) )
                          
        login_button.grid(row=6,column=0,padx=90,pady=(20,0),sticky='w')

        orLabel = Label(frame1, text="--------------------- OR ---------------------", font=("Open Sans", 10),
                    fg="firebrick1", bg="white")
        orLabel.grid(row=7,column=0,padx=100,pady=(20,0),sticky='w')
            

    # signup
        signup = Label(frame1, text="Don't have an Account ?", font=("Open Sans", 10), 
                       fg="firebrick1", bg="white")
        
        signup.grid(row=8,column=0,padx=130,pady=(20,0),sticky='w')

        new_btn = Button(frame1, text="create new account", bd=0, bg="white", activebackground='white',
                    font=('Microsoft Yahel UI Light ', 10, 'bold underline'),
                    fg="blue",
                    cursor="hand2",
                    command=self.register)
        new_btn.grid(row=9,column=0,padx=140,pady=(20,0),sticky='w')
 

#  data of login
        
    def login(self):
        username=self.entry.get()
        password=self.entry1.get()
        if username=="admin" and password=="admin":
            messagebox.showinfo("success","welcome admin")
            self.root.destroy()
            root = Tk()
            from admin import admin_form
            admin_form(root)
            root.mainloop()
        elif username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
                mycursor = con.cursor()
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Connection error: {e}")
                return

            query = "SELECT * FROM used WHERE username=%s AND password=%s"
            mycursor.execute(query, (username, password))
            row = mycursor.fetchone()
            con.close()

            if row == None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                id=row[0]
                messagebox.showinfo("Welcome", "Login successful")
                self.root.destroy()
                root = Tk()
                from customer import customer_form
                customer_form(root,username,id)
                
                root.mainloop()
    # forgot pass
    def forgot_pass(self):
        icon = PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)
        # self.root.destroy()
        window=Tk()
        window.title("change password")
        window.resizable(0, 0)
        window.config(bg="#cc2364")


        # title
        window.title("Taxi Booking System")
        window.geometry('650x580+150+25')


        # create a frame
        frame23 = Frame(window, width=370, height=400, bg="white")
        frame23.place(x=150, y=50)

        # heading
        heading = Label(frame23, text="RESET PASSWORD", font=('Microsoft Yahel UI Light ', 23, 'bold'),
                        background="white",
                        fg='firebrick1')
        heading.place(x=50, y=20)

        # login
        self.usernameEntry1 = Entry(frame23, width=17, font=('Microsoft Yahel UI Light ', 16,), bd=0,
                            fg='firebrick1')
        self.usernameEntry1.place(x=50, y=80)
        self.usernameEntry1.insert(0,"Username")
        self.usernameEntry1.bind("<FocusIn>",lambda event: self.usernameEntry1.delete(0, "end"))

        frame1 = Frame(frame23, width=250, height=2, bg='firebrick1')
        frame1.place(x=50, y=120)


        # password
        self.passwordEntry2 = Entry(frame23, width=17, font=('Microsoft Yahel UI Light ', 16,), bd=0,
                            fg='firebrick1')
        self.passwordEntry2.place(x=50, y=150)
        self.passwordEntry2.insert(0, "New Password")
        self.passwordEntry2.bind("<FocusIn>",lambda event: self.passwordEntry2.delete(0, "end"))

        Frame(frame23, width=250, height=2, bg='firebrick1').place(x=50, y=190)

        self.passwordEntry3 = Entry(frame23, width=17, font=('Microsoft Yahel UI Light ', 16,), bd=0,
                            fg='firebrick1')
        self.passwordEntry3.place(x=50, y=220)
        self.passwordEntry3.insert(0, "Confirm Password")
        self.passwordEntry3.bind("<FocusIn>",lambda event: self.passwordEntry3.delete(0, "end"))

        Frame(frame23, width=250, height=2, bg='firebrick1').place(x=50, y=260)

        submit=Button(frame23,text="submit",fg="white",bg="firebrick1",bd=0,
                      activebackground="firebrick1",
                      width=20,font=('Microsoft Yahel UI Light ', 12),command=self.doit)
        submit.place(x=80,y=285)

    def doit(self):
        
        if self.usernameEntry1.get()=='' or self.passwordEntry2.get()=="" or self.passwordEntry3.get()=="" :
          messagebox.showerror("error","all fields are required")
        elif self.passwordEntry2.get()!=self.passwordEntry3.get():
           messagebox.showerror("error","Enter the same password")
        else:
            con=pymysql.connect(host="localhost",user="root",password="Aryan@123456789",database="db1")
            mycuror=con.cursor()
            query="SELECT * from used where username=%s"
            mycuror.execute(query,(self.usernameEntry1.get()))
            row=mycuror.fetchone()

            if row==None:
                    messagebox.showerror("error","incorrect username")

            else:
                query="update used set password=%s where username=%s"
                mycuror.execute(query,(self.passwordEntry2.get(),self.usernameEntry1.get()))
                con.commit()
                con.close()
                messagebox.showinfo("success","password update sucessfully")
                self.root.destroy()
                root = Tk()
                self.ob = Login_form(root)
                root.mainloop()
    

      # register database  
        
    def connect_mysql(self):
        if (
        self.user_entry.get("1.0", "end-1c") == ""
        or self.user_phone.get("1.0", "end-1c") == ""
        or self.user_address.get("1.0", "end-1c") == ""
        or self.user_mail.get("1.0", "end-1c") == ""
        or self.user_pass.get("1.0", "end-1c") == ""
        or self.user_cpass.get("1.0", "end-1c") == ""
    ):
            messagebox.showerror("Error", "All fields are required")
        elif self.user_pass.get("1.0", "end-1c") != self.user_cpass.get("1.0", "end-1c"):
            messagebox.showerror("Error", "Please enter the same password")
        elif self.check.get() == 0:
            messagebox.showerror("Error", "Please confirm the terms and conditions")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789", database="db1")
                mycursor = con.cursor()
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Database connectivity issue, please try again\nError: {e}")
                return

            try:
                query = "INSERT INTO used (username, number, address, e_mail, password) VALUES (%s, %s, %s, %s, %s)"
                mycursor.execute(query, (
                    self.user_entry.get("1.0", "end-1c"), self.user_phone.get("1.0", "end-1c"),
                    self.user_address.get("1.0", "end-1c"), self.user_mail.get("1.0", "end-1c"),
                    self.user_pass.get("1.0", "end-1c")))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration is successful")
                self.root.destroy()
                root = Tk()
                self.ob = Login_form(root)
                root.mainloop()
            except pymysql.Error as e:
                messagebox.showerror("Error", f"Error in executing query: {e}")

             

# register
        
    def register(self):
        icon = PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)

        frame=Frame(self.root,bg="white")
        frame.place(x=(10),y=(50),height=540,width=650)
       
        image_path="oop.jpg"
        self.img=Image.open(image_path)
        self.img=ImageTk.PhotoImage(self.img)

        label2=Label(frame,image=self.img,bd=0)
        label2.place(x=0,y=0)
        
        frame2=Frame(self.root,bg="white")
        frame2.place(x=640,y=20,height=540,width=500)

        head=Label(frame2,text="Sign-up",font=('Microsoft Yahel UI Light ', 20, 'bold underline'),
                    fg="firebrick1",bg="white")
        head.grid(row=0,column=0,padx=165,pady=(10,0))

        user=Label(frame2,text="User-Name",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user.place(x=10,y=70)
        self.user_entry=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_entry.place(x=10,y=110)

        user2=Label(frame2,text="Phone No.",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user2.place(x=260,y=70)
        self.user_phone=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_phone.place(x=260,y=110)

        user3=Label(frame2,text="Address",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user3.place(x=10,y=150)
        self.user_address=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_address.place(x=10,y=190)

        user4=Label(frame2,text="E-mail",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user4.place(x=260,y=150)
        self.user_mail=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_mail.place(x=260,y=190)

        user5=Label(frame2,text="Password",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user5.place(x=10,y=230)
        self.user_pass=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_pass.place(x=10,y=270)

        user6=Label(frame2,text="Confirm-Password",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user6.place(x=260,y=230)
        self.user_cpass=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_cpass.place(x=260,y=270)


       
        pay_label=Label(frame2,text="Payment",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        pay_label.place(x=260,y=310)
        option=["online","cash"]
        self.click=StringVar()
        self.click.set(option[0])

        drop=OptionMenu(frame2,self.click,*option)
        drop.place(x=260,y=350)
       
        self.check=IntVar()
        termscondition=Checkbutton(frame2,text=" I agree the terms & Condition",
                                        font=("Microsoft Yahel UI",9,'bold'),
                                        bg="white",
                                        activebackground="white",
                                        activeforeground="firebrick1",
                                        cursor="hand2",
                                        variable=self.check)
        termscondition.place(x=20,y=390)
        signbtn=Button(frame2,text="signin-User",font=('MIcrosoft Yahel UI',14),
                            bd=0,bg="firebrick1",
                            fg="white",cursor="hand2",
                            width=10,command=self.connect_mysql)
        signbtn.place(x=69,y=420)

        signbtn=Button(frame2,text="signin-driver",font=('MIcrosoft Yahel UI',14),
                            bd=0,bg="firebrick1",
                            fg="white",cursor="hand2",command=self.drive,
                            width=10)
        signbtn.place(x=260,y=420)

        lab=Label(frame2,text="---------------------OR---------------------",bg="white",fg="firebrick1")
        lab.place(x=110,y=475)
        
        alreadyaccount=Label(frame2,text="Already have an accout?",
                                    font=("Open Sans",9,'bold'),
                                    bg='white',
                                    fg="firebrick1")
        alreadyaccount.place(x=30,y=520)
        new2btn=Button(frame2,text="login",bd=0,bg="white",
                                    font=('Microsoft Yahel UI Light ',10,'bold underline'),
                                    fg="blue",
                                    activeforeground="firebrick1",
                                    cursor="hand2",
                                    command=(self.loginform)
                                    )
        new2btn.place(x=205,y=520)

    def drive(self):
        
        self.root.destroy()
        root = Tk()
        from driver import driver_form
        driver_form(root)
       

        
if __name__=="__main__":   
    root = Tk()
    ob = Login_form(root)
    root.mainloop()