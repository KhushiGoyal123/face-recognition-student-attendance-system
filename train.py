from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
# from student import Student
import os
import mysql.connector
import cv2
from tkinter import messagebox
import numpy as np


class Train:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("500x100+0+0")
        self.root.title("Training Photos") 
        
        #train photo button
        train_photo_btn=Button(self.root,text="Click Here",command=self.train_classifier,width=60,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        train_photo_btn.grid(row=0,column=0)
        
        
         # train function
    def train_classifier(self):
          data_dir=("data")
          path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
          
          faces=[]
          ids=[]
          
          for image in path:
              img=Image.open(image).convert('L')    #gray scale image
              imageNp=np.array(img,'uint8')
              id=int(os.path.split(image)[1].split('.')[1])
              
              faces.append(imageNp)
              ids.append(id)
              cv2.imshow("Training",imageNp)
              cv2.waitKey(1)==13
          ids=np.array(ids)
          
          
          # =====================training the classifier and saving===========
          clf=cv2.face.LBPHFaceRecognizer_create()
        #   clf=cv2.face.EigenFaceRecognizer_create()
          clf.train(faces,ids)
          
          clf.write("classifier.xml")
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Thank you for adding the photo!")
        
        
        
        
        

        
        
        
 
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()