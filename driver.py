from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql


class driver_form:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking")
        self.root.geometry("1100x600+100+25")
        self.root.resizable(0, 0)
        self.root.config(bg="white")
        self.logindriver()
     

        # icon
        icon = PhotoImage(file="icons8-taxi-48.png")
        self.root.iconphoto(True, icon)

    def logindriver(self):

        frame=Frame(self.root,bg="white")
        frame.place(x=(10),y=(50),height=600,width=650)
       
        image_path="cha.jpg"
        self.img=Image.open(image_path)
        self.img=ImageTk.PhotoImage(self.img)

        label=Label(frame,image=self.img,bd=0)
        label.place(x=0,y=0)
        # frame1
        frame1=Frame(self.root,bg="white")
        frame1.place(x=640,y=20,height=600,width=500)

        Label1=Label(frame1,text="Login-Driver",font=("Microsoft Yahel UI Light",20,"bold underline"),fg="firebrick1",bg="white")
        Label1.grid(row=0,column=0,padx=125,pady=(20,0),sticky='w')

        Label2=Label(frame1,text="Driver-Name",font=("Microsoft Yahel UI Light",14),fg="firebrick1",bg='white')
        Label2.grid(row=1,column=0,padx=90,pady=(20,0),sticky='w')

        self.entry=Entry(frame1,font=("Microsoft Yahel UI Light",14),bg='white')
        self.entry.grid(row=2,column=0,padx=90,pady=(20,0),sticky='w',columnspan=8)

        Label3=Label(frame1,text="password",font=("Microsoft Yahel UI Light",14),fg="firebrick1",bg='white')
        Label3.grid(row=3,column=0,padx=90,pady=(20,0),sticky='w')

        self.entry1=Entry(frame1,font=("Microsoft Yahel UI Light",14),bg='white')
        self.entry1.grid(row=4,column=0,padx=90,pady=(20,0),sticky='w',columnspan=8)    
        

        login_button = Button(frame1, text="Login", font=('Open Sans', 10, 'bold'),
                              fg="white",bg="firebrick1", bd=0,
                              width=29, cursor="hand2",
                              activebackground="firebrick1",
                              activeforeground="white" ,command=self.login)
                          
        login_button.grid(row=7,column=0,padx=90,pady=(20,0),sticky='w')

        orLabel = Label(frame1, text="--------------------- OR ---------------------", font=("Open Sans", 10),
                    fg="firebrick1", bg="white")
        orLabel.grid(row=8,column=0,padx=100,pady=(20,0),sticky='w')

    
    # signup
        signup = Label(frame1, text="Don't have an Account ?", font=("Open Sans", 10), 
                       fg="firebrick1", bg="white")
        
        signup.grid(row=9,column=0,padx=130,pady=(20,0),sticky='w')

        new_btn = Button(frame1, text="create new account", bd=0, bg="white", activebackground='white',
                    font=('Microsoft Yahel UI Light ', 10, 'bold underline'),
                    fg="blue",
                    cursor="hand2",
                    command=self.register)
        new_btn.grid(row=10,column=0,padx=140,pady=(20,0),sticky='w')

   

    def login(self):
        username=self.entry.get()
        password=self.entry1.get()
        if username=="" or password=="":
            messagebox.showerror("error","all fields are required")
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="Aryan@123456789")
                mycursor=con.cursor()
            except:
                messagebox.showerror("error","connection is not established")
                return

            query='use db1'
            mycursor.execute(query)
            query="select * from driver where drivername=%s and password=%s"
            mycursor.execute(query,(username,password))
            row=mycursor.fetchone()
            if row==None:

                
                messagebox.showerror("error","invalid username or password")
                return
            else:
                id=row[0]
                messagebox.showinfo("welcome","login sucessfull")

                self.root.destroy()
                root=Tk()
                from driver2 import driver2_form
                driver2_form(root,username,id)
    

# Register
        
    def register(self):
        
        frame=Frame(self.root,bg="white")
        frame.place(x=(10),y=(50),height=540,width=650)
       
        image_path="cha.jpg"
        self.img=Image.open(image_path)
        self.img=ImageTk.PhotoImage(self.img)

        label2=Label(frame,image=self.img,bd=0)
        label2.place(x=0,y=40)
        
        frame2=Frame(self.root,bg="white")
        frame2.place(x=640,y=20,height=540,width=500)

        head=Label(frame2,text="Sign-up",font=('Microsoft Yahel UI Light ', 20, 'bold underline'),
                    fg="firebrick1",bg="white")
        head.grid(row=0,column=0,padx=165,pady=(10,0))

        user=Label(frame2,text="User-Name",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user.place(x=60,y=70)
        self.user_entry=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_entry.place(x=60,y=110,width=240,height=30)

        
     


        user1=Label(frame2,text="Password",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user1.place(x=60,y=150)
        self.user_pass=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_pass.place(x=60,y=190,width=240,height=30)

        user2=Label(frame2,text="Confirm-Password",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user2.place(x=60,y=230)
        self.user_cpass=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_cpass.place(x=60,y=270,width=240,height=30)

        user3=Label(frame2,text="License-plate",font=('Microsoft Yahel UI Light ', 14, 'bold'),
                    fg="firebrick1",bg="white")
        user3.place(x=60,y=310)
        self.user_lplate=Text(frame2,bg="white",width=19,height=1,wrap='none')
        self.user_lplate.place(x=60,y=350,width=240,height=30)



        
        self.check=IntVar()
        termscondition=Checkbutton(frame2,text=" I agree the terms & Condition",
                                        font=("Microsoft Yahel UI",9,'bold'),
                                        bg="white",
                                        activebackground="white",
                                        activeforeground="firebrick1",
                                        cursor="hand2",
                                        variable=self.check)
        termscondition.place(x=60,y=390)
        signbtn=Button(frame2,text="sign-in",font=('MIcrosoft Yahel UI',14),
                            bd=0,bg="firebrick1",
                            fg="white",cursor="hand2",
                            width=10,
                            command=self.conmysql)
        signbtn.place(x=165,y=420)

        

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
                                    cursor="hand2" ,command=self.driverlogin
                                    
                                    )
        new2btn.place(x=205,y=520)

    def driverlogin(self):
        self.root.destroy()
        root=Tk()
        from driver import driver_form
        driver_form(root)
    
    def conmysql(self):
     if (
        self.user_entry.get("1.0", "end-1c") == ""
        or self.user_pass.get("1.0", "end-1c") == ""
        or self.user_cpass.get("1.0", "end-1c") == ""
        or self.user_lplate.get("1.0", "end-1c") == ""
    ):
        messagebox.showerror("error", "All fields are required")
     elif self.user_pass.get("1.0", "end-1c") != self.user_cpass.get("1.0", "end-1c"):
        messagebox.showerror("Error", "Please enter the same password")
     elif self.check.get() == 0:
        messagebox.showerror("Error", "Please confirm the terms and conditions")
     else:
        
        self.con = pymysql.connect(host="localhost", user="root", password="Aryan@123456789")
        self.mycursor = self.con.cursor()

        
       
        self.mycursor.execute('use db1')
        query="select * from driver where drivername=%s"
        self.mycursor.execute(query,(self.user_entry.get("1.0","end-1c")))
        row=self.mycursor.fetchone()
        if row!=None:
            messagebox.showerror("error","username exists")
        else:
            query="insert into driver(drivername,password,license_plate) values(%s,%s,%s)"
            self.mycursor.execute(query,(self.user_entry.get("1.0","end-1c"),self.user_pass.get("1.0","end-1c"),self.user_lplate.get("1.0","end-1c")))
            self.con.commit()
            self.con.close()
            messagebox.showinfo("success","registration is sucessfull")
                
            self.root.destroy()
            root = Tk()
            self.ob1= driver_form(root)
            root.mainloop()
               

if __name__=="__main__":   
    root = Tk()
    ob = driver_form(root)
    root.mainloop()