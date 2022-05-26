from email.mime import image
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk          # pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register") 
        
        
        # ============text variables===============
        self.var_fName=StringVar()
        self.var_lName=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        # bg image
        self.bg=ImageTk.PhotoImage(file=r"college_images\di.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        # bg image
        self.bg_1=ImageTk.PhotoImage(file=r"college_images\iStock-1163542789-945x630.jpg")
        left_lbl=Label(self.root,image=self.bg_1)
        left_lbl.place(x=50,y=105,width=475,height=500)
        
        # main frame
        frame=Frame(self.root,bg="lightgray")
        frame.place(x=475,y=105,width=750,height=500)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="lightgray")
        register_lbl.place(x=20,y=20)
        
        # =====label and entry=======
        
        # first name
        fName=Label(frame,text="First Name",font=("times new roman",18,"bold"),bg="lightgray")
        fName.place(x=40,y=100)
        
        self.fName_entry=ttk.Entry(frame,textvariable=self.var_fName,font=("times new roman",18))
        self.fName_entry.place(x=40,y=140,width=280)
        
        # last name
        lName=Label(frame,text="Last Name",font=("times new roman",18,"bold"),bg="lightgray")
        lName.place(x=400,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lName,font=("times new roman",18))
        self.txt_lname.place(x=400,y=140,width=280)
        
        # contact
        contact=Label(frame,text="Contact No.",font=("times new roman",18,"bold"),bg="lightgray")
        contact.place(x=40,y=190)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",18))
        self.txt_contact.place(x=40,y=230,width=280)
        
        # email
        email=Label(frame,text="Email",font=("times new roman",18,"bold"),bg="lightgray")
        email.place(x=400,y=190)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",18))
        self.txt_email.place(x=400,y=230,width=280)
    
        
        # password
        password=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="lightgray")
        password.place(x=40,y=280)
         
        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",18))
        self.txt_password.place(x=40,y=320,width=280)
        
        # confirm password
        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",18,"bold"),bg="lightgray")
        confirm_password.place(x=400,y=280)
         
        self.confirm_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",18))
        self.confirm_password.place(x=400,y=320,width=280)
        
        
        # check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms & Conditions",font=("times new roman",18,"bold"),bg="lightgray",onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=370)
        
        # buttons
        # img=Image.open("college_images/register-now-button1.jpg")
        # img=img.resize((100,50),Image.ANTIALIAS)
        # self.photoimage=ImageTk.PhotoImage(img)
        
        b1=Button(frame,text="REGISTER NOW",borderwidth=2,command=self.register_data,font=("times new roman",18,"bold"),bg="lightgray",cursor="hand2")
        b1.place(x=270,y=420,width=200)
        
        
        # ==============function declarartion===========
    def register_data(self):
        if self.var_fName.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords must match",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms & Conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Khushi@123",
                    database="face_recognition")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist! Please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(
                                                                                    self.var_fName.get(), 
                                                                                    self.var_lName.get(), 
                                                                                    self.var_contact.get(), 
                                                                                    self.var_email.get(), 
                                                                                    self.var_pass.get()         
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register successfully",parent=self.root)
    
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()  
    obj=Register(root)
    root.mainloop()