from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from attendance import Attendance
from student import Student
import os
from face_recognition import Face_Recognition
from train import Train


class Face_Recognition_System_Student:
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
        
        title_lbl=Label(bg_img,text="STUDENT PANEL", font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=1,width=1300,height=45)
        
        
        # -------------Functions buttons-----------------
        def student_details():
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
            


       
        def face_data():
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)
            

               
        
        
        
        # # 1. student button
        img4=Image.open(r"college_images\gettyimages-1022573162.jpg")
        img4=img4.resize((280,260),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        # command=self.student_details
        b1=Button(bg_img,command=student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=300,y=150,width=260,height=230)
        
        b1_1=Button(bg_img,text="Student Details",command=student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=300,y=380,width=260,height=60)
        
        
        
        
        # detect face button
        img5=Image.open(r"college_images\face_detector1.jpg")
        img5=img5.resize((280,260),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img, image=self.photoimg5,cursor="hand2",command=face_data)
        b1.place(x=700,y=150,width=260,height=230)
        
        b1_1=Button(bg_img,text="Mark Your Attendance",cursor="hand2",command=face_data, font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=700,y=380,width=260,height=60)
       
       
      
            
       
            

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System_Student(root)
    root.mainloop()