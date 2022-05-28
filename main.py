from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from attendance import Attendance
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train


class Face_Recognition_System:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # first image
        img=Image.open(r"college_images\smart-attendance.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)    
        f_lbl.place(x=0,y=0,width=500,height=150)
        
        
        # second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)    
        f_lbl.place(x=500,y=0,width=500,height=150)
       
       
        # third image
        img2=Image.open(r"college_images\facial-recognition_0.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)    
        f_lbl.place(x=1000,y=0,width=550,height=150)
        
        
        # bg image
        img3=Image.open(r"college_images\bg_face.jpg")
        img3=img3.resize((1300,780),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)    
        bg_img.place(x=0,y=100,width=1300,height=780)
        
        title_lbl=Label(bg_img,text="ADMIN PANEL", font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=1,width=1300,height=45)
        
        
        # -------------Functions buttons-----------------
            
        def attendance_data():
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)
            
               
        
        img6=Image.open(r"college_images\smart-attendance.jpg")
        img6=img6.resize((280,260),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=attendance_data)
        b1.place(x=500,y=130,width=260,height=230)
        
        b1_1=Button(bg_img,text="Attendance Data",cursor="hand2",command=attendance_data,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500,y=350,width=260,height=60)
       
            
       
            

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()