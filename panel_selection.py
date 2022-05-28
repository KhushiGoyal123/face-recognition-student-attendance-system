from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from login import Login
from login_student import Login_student

class Panel_Selection:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("WELCOME TO FACE RECOGNITION ATTENDANCE SYSTEM")
        
        
        
        # bg image
        img3=Image.open(r"college_images\Student_portal_bg.jpg")
        img3=img3.resize((1300,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)    
        bg_img.place(x=0,y=0,width=1300,height=700)
        
        
         # -------------Functions buttons-----------------
        def admin_portal():
            self.new_window=Toplevel(self.root)
            self.app=Login(self.new_window)
        
        def student_portal():
            self.new_win=Toplevel(self.root)
            self.app=Login_student(self.new_win)
            
        
        
        # Admin Panel
        img=Image.open(r"college_images/ADMIN.png")
        img=img.resize((280,260),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        b1=Button(bg_img,image=self.photoimg,command=admin_portal,cursor="hand2")
        b1.place(x=300,y=150,width=260,height=230)
        
        b1_1=Button(bg_img,text="Login as Admin",cursor="hand2",command=admin_portal,font=("times new roman",18,"bold"),bg="white", fg="dark red")
        b1_1.place(x=300,y=380,width=260,height=60)
        
        
        # Student Panel
        img1=Image.open(r"college_images/STUDENT.png")
        img1=img1.resize((280,260),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        b1=Button(bg_img,image=self.photoimg1,command=student_portal,cursor="hand2")
        b1.place(x=700,y=150,width=260,height=230)
        
        b1_1=Button(bg_img,text="Login as Student",cursor="hand2",command=student_portal,font=("times new roman",18,"bold"),bg="white", fg="dark red")
        b1_1.place(x=700,y=380,width=260,height=60)
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Panel_Selection(root)
    root.mainloop()