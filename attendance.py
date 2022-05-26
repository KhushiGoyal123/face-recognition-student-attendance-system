from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from certifi import contents
import cv2
import mysql.connector
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")
        
        
        # text variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar( )
        self.var_atten_date=StringVar( )
        self.var_atten_attendance=StringVar( )
        
        
        # first image
        img1=Image.open(r"college_images\smart-attendance.jpg")
        img1=img1.resize((800,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)    
        f_lbl.place(x=0,y=0,width=600,height=180)
        
        
        # second image
        img2=Image.open(r"college_images\teaser.png")
        img2=img2.resize((800,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)    
        f_lbl.place(x=600,y=0,width=800,height=180)
     
        # bg image
        img3=Image.open(r"college_images\bg_face.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)    
        bg_img.place(x=0,y=180,width=1300,height=700)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("segoe print",30,"bold"),bg="red", fg="white")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=52,width=1250,height=500) 
     
         #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("segoe print",18,"bold"))
        Left_frame.place(x=10,y=0,width=600,height=385)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=0,width=590,height=335)
        
        # label and entry
        
        # attendance id
        attendanceId_label=Label(left_inside_frame,text="Employee Id :",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        # Roll No
        attendance_roll_label=Label(left_inside_frame,text="Roll No. :",font=("times new roman",11,"bold"),bg="white")
        attendance_roll_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        
        attendance_roll_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_roll,font=("times new roman",11,"bold"))
        attendance_roll_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        # name
        attendanceName_label=Label(left_inside_frame,text="Name :",font=("times new roman",11,"bold"),bg="white")
        attendanceName_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        
        attendanceName_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_name,font=("times new roman",11,"bold"))
        attendanceName_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        # department
        attendanceDep_label=Label(left_inside_frame,text="Department :",font=("times new roman",11,"bold"),bg="white")
        attendanceDep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        
        attendanceDep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=17,font=("times new roman",11,"bold"))
        attendanceDep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        # time
        attendanceTime_label=Label(left_inside_frame,text="Time :",font=("times new roman",11,"bold"),bg="white")
        attendanceTime_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        
        attendanceTime_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=17,font=("times new roman",11,"bold"))
        attendanceTime_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        # date
        attendanceDate_label=Label(left_inside_frame,text="Date :",font=("times new roman",11,"bold"),bg="white")
        attendanceDate_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        
        attendanceDate_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_date,font=("times new roman",11,"bold"))
        attendanceDate_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        # attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status :",font=("times new roman",11,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        
        self.attendance_status=ttk.Combobox(left_inside_frame,font=("times new roman",11,"bold"),width=15,state="readonly")
        self.attendance_status["values"]=("Status","Present","Absent")
        self.attendance_status.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        self.attendance_status.current(0)
        
        
        # =================fetch data==========
        def fetchData(rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)
                
        def import_csv():
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvRead=csv.reader(myfile,delimiter=",")
                for i in csvRead:
                    mydata.append(i)
                fetchData(mydata)
        
        def export_csv():
            try:
                if len(mydata)<1:
                    messagebox.showerror("Error","No data found to export",parent=self.root)
                    return False
                fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                with open(fln,mode="w",newline="") as myfile:
                    csvWrite=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        csvWrite.writerow(i)
                    messagebox.showinfo("Data Export","Your data is exported to "+ os.path.basename(fln)+" successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
                
        def get_cursor(event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
            
            
        def resetData():
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
            
            
            


        
        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=5,y=180,width=585,height=30)
        
        #import csv button
        import_csv_btn=Button(btn_frame,text="Import csv",command=import_csv,width=15,font=("times new roman",11,"bold"),bg="green",fg="white",cursor="hand2")
        import_csv_btn.grid(row=0,column=0)
        
        #export csv button
        export_csv_btn=Button(btn_frame,text="Export csv",command=export_csv,width=16,font=("times new roman",11,"bold"),bg="blue",fg="white",cursor="hand2")
        export_csv_btn.grid(row=0,column=1)
        
        #update button
        update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",11,"bold"),bg="purple",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=2)
        
        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=resetData,width=15,font=("times new roman",11,"bold"),bg="red",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)    
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("segoe print",18,"bold"))
        Right_frame.place(x=620,y=0,width=600,height=385)
        
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=0,width=585,height=335)
          
            
        # ============ scroll bar table =============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview) 
        
        self.AttendanceReportTable.heading("id",text="AttendanceId")
        self.AttendanceReportTable.heading("roll",text="RollNo")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",get_cursor)
        
        
     
     
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()