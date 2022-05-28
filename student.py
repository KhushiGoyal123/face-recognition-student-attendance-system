from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from train import Train


        

class Student:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        
         
        
      # ------------------variables-------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_name=StringVar()
        self.var_std_id=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
      
      
      # first image
        img=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\hqdefault.jpg")
        img=img.resize((500,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)    
        f_lbl.place(x=0,y=0,width=500,height=150)
        
        
        # second image
        img1=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\facial-recognition_0.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)    
        f_lbl.place(x=500,y=0,width=500,height=150)
       
       
        # third image
        img2=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\face-recognition.png")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)    
        f_lbl.place(x=1000,y=0,width=500,height=150)
        
          
        
        # bg image
        img3=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\bg_face.jpg")
        # img3=img3.resize((100,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)    
        bg_img.place(x=0,y=100,width=1300,height=700)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("segoe print",35,"bold"),bg="red", fg="white")
        title_lbl.place(x=0,y=1,width=1350,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=52,width=1250,height=500)
        

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("segoe print",18,"bold"))
        Left_frame.place(x=10,y=5,width=600,height=475)
        
        # img_left=Image.open(r"C:\Users\Admin\Desktop\Face Recognition System\college_images\facial-recognition_0.jpg")
        # img_left=img_left.resize((600,150),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        # f_lbl=Label(Left_frame,image=self.photoimg_left)    
        # f_lbl.place(x=5,y=0,width=585,height=150)
        
        
        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        current_course_frame.place(x=5,y=0,width=585,height=100)
        
        
        # department
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",11,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science", "IT", "Civil", "Mechanical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        
        # course
        course_label=Label(current_course_frame,text="Course :",font=("times new roman",11,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.Tech.","M.Tech.")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)
       
       
        # year
        year_label=Label(current_course_frame,text="Year :",font=("times new roman",11,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        
        # semester
        semester_label=Label(current_course_frame,text="Semester :",font=("times new roman",11,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        
        # class student information frame
        Class_Student_frame=LabelFrame(Left_frame,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
        Class_Student_frame.place(x=5,y=110,width=585,height=220)
        
        
        # student id
        studentId_label=Label(Class_Student_frame,text="Student Id :",font=("times new roman",11,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",11,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
       
        # student name
        studentName_label=Label(Class_Student_frame,text="Student Name :",font=("times new roman",11,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",11,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # class division
        class_div_label=Label(Class_Student_frame,text="Class Division :",font=("times new roman",11,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman",11,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        class_div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),width=13,state="readonly")
        class_div_combo["values"]=("A","B","C","D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        # Roll No
        roll_no_label=Label(Class_Student_frame,text="Roll No. :",font=("times new roman",11,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        gender_label=Label(Class_Student_frame,text="Gender :",font=("times new roman",11,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=15,font=("times new roman",11,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),width=13,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # DOB
        dob_label=Label(Class_Student_frame,text="DOB :",font=("times new roman",11,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",11,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # Email
        email_label=Label(Class_Student_frame,text="Email :",font=("times new roman",11,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(Class_Student_frame,width=15,textvariable=self.var_email,font=("times new roman",11,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # Phone no
        phone_label=Label(Class_Student_frame,text="Phone No. :",font=("times new roman",11,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman",11,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        address_label=Label(Class_Student_frame,text="Address :",font=("times new roman",11,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=15,font=("times new roman",11,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher Name
        teacher_label=Label(Class_Student_frame,text="Teacher Name :",font=("times new roman",11,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",11,"bold"))     
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5)
        
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5)
        
        
        #buttons frame
        btn_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=5,y=335,width=585,height=30)
        
        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)
        
        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",11,"bold"),bg="purple",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)
        
        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",11,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)
        
        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",11,"bold"),bg="red",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)
        
        #buttons frame
        btn_frame1=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=5,y=365,width=585,height=30)
        
        #take photo button
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=32,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        take_photo_btn.grid(row=0,column=0)
        
        #update photo button
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1)
        
        
         # training photo data sets
        
        
        #train frame
        train_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        train_frame.place(x=5,y=395,width=585,height=30)
        
        #train photo button
        train_photo_btn=Button(train_frame,text="Click only after photo sample is added",command=self.train_classifier,width=70,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        train_photo_btn.grid(row=0,column=0)
        
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("segoe print",18,"bold"))
        Right_frame.place(x=625,y=5,width=600,height=475)
        
        
        # ---------Search System------------
        Search_frame=LabelFrame(Right_frame,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        Search_frame.place(x=5,y=0,width=585,height=70)
        
        search_label=Label(Search_frame,text="Search By :",font=("times new roman",12,"bold"),bg="light pink",fg="blue")
        search_label.grid(row=0,column=0,padx=8,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",11,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=12,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)
        
        #search button
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",11,"bold"),bg="light blue",fg="black",cursor="hand2")
        search_btn.grid(row=0,column=3,padx=2)
        
        #show all button
        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",11,"bold"),bg="light blue",fg="black",cursor="hand2")
        showAll_btn.grid(row=0,column=4,padx=2)
        
        # -----------table frame------------
        table_frame=LabelFrame(Right_frame,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=75,width=585,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=90)
        self.student_table.column("course",width=90)
        self.student_table.column("year",width=90)
        self.student_table.column("sem",width=90)
        self.student_table.column("id",width=90)
        self.student_table.column("name",width=90)
        self.student_table.column("div",width=90)
        self.student_table.column("roll",width=90)
        self.student_table.column("gender",width=90)
        self.student_table.column("dob",width=90)
        self.student_table.column("email",width=90)
        self.student_table.column("phone",width=90)
        self.student_table.column("address",width=90)
        self.student_table.column("teacher",width=90)
        self.student_table.column("photo",width=115)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
      
                    
      # ------------function declaration--------------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
              conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="#Khushi@123",
                database="face_recognition")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()

                                                                                                              ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            
            except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
          
     # Fetch data
    def fetch_data(self):
          conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Khushi@123",
            database="face_recognition")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from student")
          data=my_cursor.fetchall()
          
          if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                      self.student_table.insert("",END,values=i)
                conn.commit() 
          conn.close()
      
      
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
        
          
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
              Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
              if Update>0:
                    conn=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="#Khushi@123",
                        database="face_recognition")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      
                                                                                                                                                                                              self.var_dep.get(),
                                                                                                                                                                                              self.var_course.get(),
                                                                                                                                                                                              self.var_year.get(),
                                                                                                                                                                                              self.var_semester.get(),
                                                                                                                                                                                              self.var_std_name.get(),
                                                                                                                                                                                              self.var_div.get(),
                                                                                                                                                                                              self.var_roll.get(),
                                                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                                                              self.var_dob.get(),
                                                                                                                                                                                              self.var_email.get(),
                                                                                                                                                                                              self.var_phone.get(),
                                                                                                                                                                                              self.var_address.get(),
                                                                                                                                                                                              self.var_teacher.get(),
                                                                                                                                                                                              self.var_radio1.get(),
                                                                                                                                                                                              self.var_std_id.get(),
                                                                                                                                                                                           
                                                                                                                                                                                          ))
              else:
                  if not Update:
                        return
              messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
              conn.commit()
              self.fetch_data()
              conn.close()
         
            except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
              
              
              
     # delete function
    def delete_data(self):
          if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student Id is required",parent=self.root)
          else:
                try:
                  delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)    
                  if delete>0:
                        conn=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="#Khushi@123",
                        database="face_recognition")
                        my_cursor=conn.cursor()
                        sql="delete from student where Student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                  else:
                        if not delete:
                              return
                  messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root) 
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  
                except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                        
          
        
        # reset function
    def reset_data(self):
          self.var_dep.set("Select Department"),
          self.var_course.set("Select Course"),
          self.var_year.set("Select Year"),
          self.var_semester.set("Select Semester"),
          self.var_std_name.set(""),
          self.var_div.set("A"),
          self.var_roll.set(""),
          self.var_gender.set("Male"),
          self.var_dob.set(""),
          self.var_email.set(""),
          self.var_phone.set(""),
          self.var_address.set(""),
          self.var_teacher.set(""),
          self.var_radio1.set(""),
          self.var_std_id.set(""),
              
            
        
        
        # ===================Generate data set or Take Photo Sample===================
    def generate_dataset(self):
          if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
          else:
                try:
                    conn=mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="#Khushi@123",
                      database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                          id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      
                                                                                                                                                                                              self.var_dep.get(),
                                                                                                                                                                                              self.var_course.get(),
                                                                                                                                                                                              self.var_year.get(),
                                                                                                                                                                                              self.var_semester.get(),
                                                                                                                                                                                              self.var_std_name.get(),
                                                                                                                                                                                              self.var_div.get(),
                                                                                                                                                                                              self.var_roll.get(),
                                                                                                                                                                                              self.var_gender.get(),
                                                                                                                                                                                              self.var_dob.get(),
                                                                                                                                                                                              self.var_email.get(),
                                                                                                                                                                                              self.var_phone.get(),
                                                                                                                                                                                              self.var_address.get(),
                                                                                                                                                                                              self.var_teacher.get(),
                                                                                                                                                                                              self.var_radio1.get(),
                                                                                                                                                                                              self.var_std_id.get()==id+1
                                                                                                                                                                                          ))  
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close() 
                    
                    # ==============Load pre Defined data on face frontals from opencv =======
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        # 1.3 - scaling factor
                        # 5 - minimum neighbour
                        
                        for (x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                          ret,my_frame=cap.read()
                          if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))      
                            face1=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped face",face1)

                            if cv2.waitKey(1)==13 or int(img_id)==100:
                              break
                    cap.release()
                    cv2.destroyAllWindows()
                          
                    messagebox.showinfo("Result","Photo Added",parent=self.root)  
                   
                      
                except Exception as es:
                  messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                                                                                                                                                                                           
   
   
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
          messagebox.showinfo("Result","Thank you for adding the photo!",parent=self.root)   
   
                    
                    
                    
                    
        
          
            
 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
