from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # type: ignore
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background
        
         #=========== variables=========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep= StringVar()
        self.var_atten_time= StringVar()
        self.var_atten_date= StringVar()
        self.var_atten_attendance = StringVar()
      
        

        image1 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        image1 = image1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(image1)
        f_lbl1 = Label(self.root, image=self.photoimg1, bg="#f5f5dc")
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # Image 2
        image2 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img3.png")
        image2 = image2.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)
        f_lbl2 = Label(self.root, image=self.photoimg2, bg="#f5f5dc")
        f_lbl2.place(x=800, y=0, width=800, height=200)

           # ================== Title ===================
        title_lbl = Label(self.root, text=" ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 32, "bold"), bg="white", fg="green",anchor="center")
        title_lbl.place(x=0, y=200, width=1560, height=45)


        
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=25, y=250, width=1480, height=550)

        # ======= Left Frame ==========
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                        text="Student Attendnce Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=540)

        img_left = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        img_left = img_left.resize((710, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=130)

          
        left_inside_frame = Frame(Left_frame, bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0, y=135, width=710, height=370)


         
         #labelled entry
        
          
        AttendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13,"bold"), bg="white")
        AttendanceId_label.grid(row=0, column=0, padx=4, pady=8, sticky=W)
        
        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        AttendanceId_entry.grid(row=0,column=1, padx=4, pady=8,sticky=W)

        # Roll no.
        Roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13,"bold"), bg="white")
        Roll_label.grid(row=0, column=2, padx=4, pady=8, sticky=W)
        
        Roll_entry=ttk.Entry(left_inside_frame,width=20, textvariable=self.var_atten_roll,font=("times new roman", 13, "bold"))
        Roll_entry.grid(row=0,column=3, padx=4, pady=8,sticky=W)


        # Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13,"bold"), bg="white")
        Name_label.grid(row=1, column=0, padx=4, pady=8, sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1, padx=4, pady=8,sticky=W)

        # department
        depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        depLabel.grid(row=1,column=2,padx=4,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3, padx=4, pady=8,sticky=W)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=4,pady=8,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20, textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1, padx=4, pady=8,sticky=W)

        #date

        dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=4,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3, padx=4, pady=8,sticky=W)

         # attendance
        
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=4, pady=8,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status['values']=("Status",'Present','Absent')
        self.atten_status.grid(row=3,column=1,padx=4,pady=8,sticky=W)
        self.atten_status.current(0)

          #button framel

        button_frame=Frame(left_inside_frame,bg="white")
        button_frame.place(x=0,y=300,width=715, height=35)
        
        import_btn=Button(button_frame,text="Import csv", command=self.importCsv ,width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(button_frame,text="Export csv",command=self.exportCsv,width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(button_frame,text="Update",command=self.update_data,width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(button_frame,text="Reset",command=self.reset_data, width=17,font= ("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

# ========== Right Frame ==========
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                         text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=740, y=10, width=720, height=570)

        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReport_Table= ttk.Treeview(table_frame, 
                                          columns=("id", "roll", "name", "department", "time", "date", "attendance"),xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReport_Table.xview)
        scroll_y.config(command=self.AttendanceReport_Table.yview)

        self.AttendanceReport_Table.heading("id", text="Attendance ID")
        self.AttendanceReport_Table.heading("roll", text="Roll")
        self.AttendanceReport_Table.heading("name", text="Name")
        self.AttendanceReport_Table.heading("department", text="Department")
        self.AttendanceReport_Table.heading("time", text="Time")
        self.AttendanceReport_Table.heading("date", text="Date")
        self.AttendanceReport_Table.heading("attendance", text="Attendance")
      
        self.AttendanceReport_Table["show"] = "headings"

        self.AttendanceReport_Table.column("id",width=100)
        self.AttendanceReport_Table.column("roll",width=100)
        self.AttendanceReport_Table.column("name",width=100)
        self.AttendanceReport_Table.column("department",width=100)
        self.AttendanceReport_Table.column("time",width=100)
        self.AttendanceReport_Table.column("date",width=100)
        self.AttendanceReport_Table.column("attendance",width=100)

        self.AttendanceReport_Table.pack(fill=BOTH, expand=1)
        self.AttendanceReport_Table.bind("<ButtonRelease>",self.get_cursor)
      #   self.fetch_data()

        # ============ fetch data==========
    def fetchData(self,rows):
        self.AttendanceReport_Table.delete(*self.AttendanceReport_Table.get_children())
        for i in rows:
          self.AttendanceReport_Table.insert("",END,values=i)

# import Csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                     filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        try:
            with open(fln) as myfile:
                csvread = csv.reader(myfile)
                next(csvread)  # Skip header row
            for row in csvread:
                mydata.append(row)
            self.fetchData(mydata)
        except Exception as e:
            print(f"Error: {e}")  # Print the full exception
            messagebox.showerror("Error", f"Error while importing CSV file:\n{str(e)}")


                    
  # export csv

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                           filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                           defaultextension=".csv")
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
            # Write header
            exp_write.writerow(["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"])
            for row in mydata:
                exp_write.writerow(row)
            messagebox.showinfo("Data Exported", f"Your data has been exported to {os.path.basename(fln)} successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error while exporting CSV:\n{str(e)}")

          


    def get_cursor(self,event=""):
        cur_item = self.AttendanceReport_Table.focus()  # Get the current item
        content = self.AttendanceReport_Table.item(cur_item)  # Get the content of the item
        selected_data = content['values']  # Extract the values from the item
        self.var_atten_id.set(selected_data[0])
        self.var_atten_roll.set(selected_data[1])
        self.var_atten_name.set(selected_data[2])
        self.var_atten_dep.set(selected_data[3])
        self.var_atten_time.set(selected_data[4])
        self.var_atten_date.set(selected_data[5])
        self.var_atten_attendance.set(selected_data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def update_data(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return

        updated = False
        updated_row = [
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]

        for i, row in enumerate(mydata):
            if len(row) == 0:
                continue  # Skip empty rows
            if row[0] == updated_row[0]:  # Match by Attendance ID
                mydata[i] = updated_row
                updated = True
                break

        if updated:
            # Save updated data to CSV
            with open("attendance.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"])  # Header
                writer.writerows(mydata)

            self.fetchData(mydata)
            messagebox.showinfo("Success", "Record updated and saved successfully", parent=self.root)
        else:
            messagebox.showerror("Error", "Record not found in the data list", parent=self.root)




         
            
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
