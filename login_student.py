from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from attendance import Attendance
from student import Student
import os
from main import Face_Recognition_System
from main_student import Face_Recognition_System_Student
from register import Register


# def main():
#     main_win=Tk()
#     app=Login(main_win)
#     main_win.mainloop()

class Login_student:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login") 
        
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
        left_lbl.place(x=450,y=105,width=450,height=500)
        
        # frame
        frame=Frame(self.root,bg="white")
        frame.place(x=475,y=130,width=400,height=450)
        
        img1=Image.open(r"college_images/LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lblimg1=Label(self.root,image=self.photoimage1,borderwidth=0)
        lblimg1.place(x=640,y=150,width=80,height=80)
        
        get_start=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_start.place(x=135,y=110)
        
        
        # Email
        user_email=Label(frame,text="Email",font=("times new roman",18,"bold"),bg="white")
        user_email.place(x=40,y=170)
        
        self.txt_user_email=ttk.Entry(frame,font=("times new roman",18))
        self.txt_user_email.place(x=40,y=200,width=280)
    
        
        # password
        user_password=Label(frame,text="Password",font=("times new roman",18,"bold"),bg="white")
        user_password.place(x=40,y=250)
         
        self.txt_user_password=ttk.Entry(frame,font=("times new roman",18))
        self.txt_user_password.place(x=40,y=280,width=280)
        
        
        # forgot password
        forgot_password=Button(frame,command=self.forgot_password_window,text="Forgot Password ?",borderwidth=0,font=("times new roman",12,"bold"),bg="white",cursor="hand2",activebackground="white")
        forgot_password.place(x=30,y=315,width=150,height=35)
       
        # Create New User
        create_new_user=Button(frame,text="Create New User",command=self.register_window,borderwidth=0,font=("times new roman",12,"bold"),bg="white",cursor="hand2",activebackground="white")
        create_new_user.place(x=25,y=342,width=150,height=35)
        
        
        # buttons
        b1=Button(frame,relief=RIDGE,text="LOG IN",command=self.login_student,borderwidth=2,font=("times new roman",18,"bold"),bg="red",fg="white",cursor="hand2",activebackground="white")
        b1.place(x=145,y=385,width=125)
    
        
        # function descriptions
            
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
    def login_student(self):
        if self.txt_user_email.get()=="" or self.txt_user_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user_email.get()=="khushi@gmail.com" and self.txt_user_password.get()=="1234":
            messagebox.showinfo("Success","You are now signed in",parent=self.root)
        else:
            conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Khushi@123",
                    database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where Email=%s and Password=%s",(
                                                                                         self.var_email.get(),
                                                                                         self.var_pass.get()
                                                                                        
                                                                                      ))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Ask","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System_Student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    # reset password
    def reset_password(self):
        if self.user_new_password.get()=="":
            messagebox.showerror("Error","Please enter the password",parent=self.root)
        else:
            conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Khushi@123",
                    database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txt_user_email.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter password",parent=self.root)
            else:
                query=("update register set Password=%s where Email=%s")
                value=(self.user_new_password.get(),self.txt_user_email.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password reset successfully",parent=self.root)
                self.new_window.destroy()
                
               
            
    # forget password window  
    def forgot_password_window(self):
        if self.txt_user_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Khushi@123",
                    database="face_recognition")
            my_cursor=conn.cursor()
            query=("Select * from register where Email=%s")
            value=(self.txt_user_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter valid email",parent=self.root)
            else:
                conn.close()
                self.root_window=Toplevel()
                self.root_window.title("Forgot Password")
                self.root_window.geometry("400x450+475+150") 
                
                l=Label(self.root_window,text="Forgot Password ?",font=("times new roman",20,"bold"),bg="red",fg="white")
                l.place(x=0,y=10,relwidth=1)
                
                # new password
                new_password=Label(self.root_window,text="New Password",font=("times new roman",17,"bold"),bg="white",fg="black")
                new_password.place(x=10,y=100,relwidth=1)
                
                self.user_new_password=ttk.Entry(self.root_window,font=("times new roman",18))
                self.user_new_password.place(x=60,y=150,width=280)
                
                # confirm new password
                confirm_new_password=Label(self.root_window,text="Confirm New Password",font=("times new roman",17,"bold"),bg="white",fg="black")
                confirm_new_password.place(x=10,y=230,relwidth=1)
                
                self.user_confirm_new_password=ttk.Entry(self.root_window,font=("times new roman",18))
                self.user_confirm_new_password.place(x=60,y=280,width=280)
            
            
                # buttons
                b2=Button(self.root_window,relief=RIDGE,text="RESET",command=self.login_student,borderwidth=2,font=("times new roman",18,"bold"),bg="red",fg="white",cursor="hand2",activebackground="white")
                b2.place(x=150,y=350,width=100)    
                    
            

        
if __name__ == "__main__":
    root=Tk()
    obj=Login_student(root)
    root.mainloop()
