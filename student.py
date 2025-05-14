from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # type: ignore
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background

        #=========== variables=========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_Father = StringVar()
        


                # Top frame for images
        top_frame = Frame(self.root, bg="#f5f5dc")
        top_frame.place(x=0, y=0, width=1920, height=190)



          # Image 1
        image1 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img2.png")
        image1 = image1.resize((600, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(image1)
        f_lbl1 = Label(top_frame, image=self.photoimg1, bg="#f5f5dc")
        f_lbl1.place(x=0, y=0, width=500, height=140)

        # Image 2
        image2 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img3.png")
        image2 = image2.resize((600, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)
        f_lbl2 = Label(top_frame, image=self.photoimg2, bg="#f5f5dc")
        f_lbl2.place(x=500, y=0, width=500, height=140)

        # Image 3
        image3 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        image3 = image3.resize((600, 140), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(image3)
        f_lbl3 = Label(top_frame, image=self.photoimg3, bg="#f5f5dc")
        f_lbl3.place(x=1000, y=0, width=550, height=140)

         # ================== Title ===================
        title_lbl = Label(self.root, text=" STUDENT MANAGEMENT SYSTEM", font=("times new roman", 32, "bold"), bg="white", fg="green",anchor="center")
        title_lbl.place(x=0, y=140, width=1560, height=45)
    

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=25, y=190, width=1480, height=590)

# ========== Left Frame ==========
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                        text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=570)

        img_left = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=130)

# ========== Current Course Sub-Frame inside Left Frame ==========
        course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                          text="Current Course Information", font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=140, width=710, height=110)
      # Department
        dep_lbl = Label(course_frame, text="Department:", font=("times new roman", 12, "bold"),bg="white")
        dep_lbl.grid(row=0, column=0,padx=10)

        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","ECE","ECE-AI","CSE-AI")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Courses
        course_label = Label(course_frame, text="Course:",font=("times new roman",13,"bold"), bg="white")
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course,font =("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]= ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year 
        year_label = Label(course_frame, text=" Year:" ,font=("times new roman", 13,"bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year,font =("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]= (" Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025","2025-2026","2026-2027",)
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester 
        semester_label = Label(course_frame, text="Semester:", font=("times new roman", 13,"bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=2, pady=10,sticky=W)
        
        semester_combo = ttk.Combobox(course_frame,textvariable=self.var_sem,font =("times new roman",13,"bold"),state="readonly",width=15)
        semester_combo["values"]= ("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                          text="Class Student information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=710, height=290)
         

         # student Id
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 13,"bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0,column=1, padx=10, pady=5,sticky=W)
       
       # student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2, padx=10, pady=5,sticky=W)
 
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0,column=3, padx=10, pady=5,sticky=W)

        # class division
         
        classdiv_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13,"bold"), bg="white")
        classdiv_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font =("times new roman",13,"bold"),state="readonly",width=18)
        division_combo["values"]= (" A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        # Enrollment number

        Rollno_label = Label(class_student_frame, text="Enrollment No.:", font=("times new roman",13,"bold"),bg="white")
        Rollno_label.grid(row=1,column=2, padx=10, pady=5,sticky=W)
 
        Rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20, font=("times new roman", 13, "bold"))
        Rollno_entry.grid(row=1,column=3, padx=10, pady=5,sticky=W)

        # Gender
         
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13,"bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font =("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]= (" Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
         
        Dob_label = Label(class_student_frame, text="Date of Birth:", font=("times new roman",13,"bold"),bg="white")
        Dob_label.grid(row=2,column=2, padx=10, pady=5,sticky=W)
 
        Dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20, font=("times new roman", 13, "bold"))
        Dob_entry.grid(row=2,column=3, padx=10, pady=5,sticky=W)


        # email
          
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13,"bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3,column=1, padx=10, pady=5,sticky=W)


        # phone number

        phone_label = Label(class_student_frame, text="Phone No.:", font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2, padx=10, pady=5,sticky=W)
 
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3,column=3, padx=10, pady=5,sticky=W)

        # address
        
        add_label = Label(class_student_frame, text="Address:", font=("times new roman",13,"bold"),bg="white")
        add_label.grid(row=4,column=0, padx=10, pady=5,sticky=W)
 
        add_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address, font=("times new roman", 13, "bold"))
        add_entry.grid(row=4,column=1, padx=10, pady=5,sticky=W)
 
        # Father name

        Fname_label = Label(class_student_frame, text="Father's Name:", font=("times new roman",13,"bold"),bg="white")
        Fname_label.grid(row=4,column=2, padx=10, pady=5,sticky=W)
 
        Fname_entry=ttk.Entry(class_student_frame,textvariable=self.var_Father,width=20, font=("times new roman", 13, "bold"))
        Fname_entry.grid(row=4,column=3, padx=10, pady=5,sticky=W)
         
         # radio button
     
        self.var_radio1 = StringVar()
        self.var_radio1.set("No")  # Default selection

        radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=6, column=1)

        #button framel

        button_frame=Frame(class_student_frame,bg="white")
        button_frame.place(x=0,y=200,width=715, height=35)
        
        save_btn=Button(button_frame,text="Save",command=self.add_data, width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,text="Update",command=self.update_data, width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(button_frame,text="Delete",command=self.delete_data, width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,text="Reset", command=self.reset_data,width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        button_frame1=Frame(class_student_frame,bg="white")
        button_frame1.place(x=0,y=235,width=715, height=35)
        

        takePhoto_btn=Button(button_frame1,text="Take Photo sample",command=self.generate_dataset, width=35,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(button_frame1,text="Update Photo Sample", width=35,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=2)

# ========== Right Frame ==========
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                         text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=740, y=10, width=720, height=570)

        
        img_right = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)

# ========== Search System ==========

        search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",font= ("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        searchBy_label = Label(search_frame, text="Search By:", font=("times new roman",13,"bold"),bg="red",fg="white")
        searchBy_label.grid(row=0,column=0, padx=10, pady=5,sticky=W)
 
        search_combo = ttk.Combobox(search_frame,font =("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]= ("Select","Enrollment_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=20, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn=Button(search_frame,text="Search", width=9,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All", width=9,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


 
              # ========== Table Frame ==========
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, 
                                          columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "father"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Enrollment No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("father", text="Father's Name")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("father", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


# ========== Function declaration===========


    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Mishi1010", database="face_recognizer")
                cur = conn.cursor()
                cur.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_Father.get(),
                    self.var_radio1.get(),
                    
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

#========== Fetcch data==============

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Mishi1010", database="face_recognizer")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")
        data=cur.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()


#============ get cursor============

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        if not data:
            return

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_Father.set(data[13]),
        self.var_radio1.set(data[14])

# ============= update function======

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root )
                if Update>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Mishi1010",database="face_recognizer")
                    cur=conn.cursor()
                    cur.execute("UPDATE student SET" \
                    " Dep=%s,Course=%s,Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s,Gender=%s, Dob=%s, Email=%s,Phone=%s, Address=%s, Father=%s,PhotoSample=%s where Student_id=%s",(

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_Father.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    

                    ))
            
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                        
#=============== Delete Function========

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Mishi1010",database="face_recognizer")
                    cur=conn.cursor()
                    cur.execute("DELETE FROM student WHERE Student_id=%s", (self.var_std_id.get(),))

                   
                else:
                    if not Delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

#reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_Father.set("")
        self.var_radio1.set("")

#=========ganerate data set============

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Mishi1010",database="face_recognizer")
                cur=conn.cursor()
                cur.execute("Select * from student")
                mylist=cur.fetchall()
                id=0
                for row in mylist:
                     id+=1
                cur.execute("UPDATE student SET" \
                    " Dep=%s,Course=%s,Year=%s, Semester=%s,Name=%s, Division=%s, Roll=%s,Gender=%s, Dob=%s, Email=%s,Phone=%s, Address=%s, Father=%s,PhotoSample=%s where Student_id=%s",(

                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_Father.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                    

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

# ============= Load predefined data on face frontals from opencv===

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbours=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h ,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                       break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
