from email.headerregistry import ContentTransferEncodingHeader
from tkinter import*
from tkinter import ttk
from unicodedata import name
from PIL import Image, ImageTk
# from student import Student
import os
from click import command
import mysql.connector
import cv2
from tkinter import messagebox
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition") 
        
        # title
        face_data_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white", fg="red")
        face_data_lbl.place(x=0,y=1,width=1300,height=45)
        
        # left image
        face_data_img=Image.open(r"college_images\facialrecognition (1).png")
        face_data_img=face_data_img.resize((500,600),Image.ANTIALIAS)
        self.photo_face_data_img=ImageTk.PhotoImage(face_data_img)
        
        face_data_lbl2=Label(self.root,image=self.photo_face_data_img)    
        face_data_lbl2.place(x=0,y=55,width=500,height=600)
        
        # right image
        face_data_img2=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        face_data_img2=face_data_img2.resize((800,600),Image.ANTIALIAS)
        self.photo_face_data_img2=ImageTk.PhotoImage(face_data_img2)
        
        face_data_lbl3=Label(self.root,image=self.photo_face_data_img2)    
        face_data_lbl3.place(x=500,y=55,width=800,height=600)
        
        
        
        #train photo button
        train_photo_btn=Button(face_data_lbl3,text="CLICK HERE",command=self.face_recog,width=70,padx=10,font=("times new roman",18,"bold"),bg="green",fg="white",cursor="hand2")
        train_photo_btn.place(x=0,y=250,width=250,height=60)
     
     
# ========= attendance ======================   
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n")as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
        
        
# ==============face recognition=================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                 confidence=int((100*(1-predict/300)))
                 
                 conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Khushi@123",
                    database="face_recognition")
                 my_cursor=conn.cursor()
                 
                 
                 my_cursor.execute("select Name from student where Student_Id="+str(id))
                 n=my_cursor.fetchone()
                #  n=str(n)
                 n="+".join(n)
 
                 my_cursor.execute("select Roll from student where Student_Id="+str(id))
                 r=my_cursor.fetchone()
                #  r=str(r)
                 r="+".join(r)
 
                 my_cursor.execute("select Dep from student where Student_Id="+str(id))
                 d=my_cursor.fetchone()
                #  d=str(d)
                 d="+".join(d)
 
                 my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                 i=my_cursor.fetchone()
                #  i=str(i)
                 i="+".join(i)
                   
                  
                 if confidence>77:
                     cv2.putText(img,f"ID: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                     cv2.putText(img,f"Roll: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                     cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                     cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                     self.mark_attendance(i,r,n,d)  
                 else:
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                     cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                         
                 
                 coord=[x,y,w,y] 
            return coord
       
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            # if coordinates is not None:
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows() 
        

        self.new_window.destroy() 
if __name__ == "__main__":
    root=Tk()  
    obj=Face_Recognition(root)
    root.mainloop()