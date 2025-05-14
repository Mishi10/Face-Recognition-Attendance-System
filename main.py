from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background

        # Top frame for images
        top_frame = Frame(self.root, bg="#f5f5dc")
        top_frame.place(x=0, y=0, width=1920, height=190)
        image1 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\college.png")
        image1 = image1.resize((1560, 190), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(image1)

        f_lbl1 = Label(top_frame, image=self.photoimg1, bg="#f5f5dc")
        f_lbl1.place(x=0, y=0, width=1560, height=190)

        # Title
        title_lbl = Label(self.root, text=" STUDENT ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 32, "bold"), bg="white", fg="red", anchor="center")
        title_lbl.place(x=0, y=190, width=1560, height=45)

        # Common button size
        btn_w, btn_h = 220, 180

        # Student Button
        image2 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\student.png")
        image2.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(image2)

        student_img_btn = Button(self.root, image=self.photoimg2, command=self.student_details , cursor="hand2")
        student_img_btn.place(x=200, y=280, width=btn_w, height=btn_h)

        student_text_btn = Button(self.root, text="Student Details",command=self.student_details, cursor="hand2",
                                  font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        student_text_btn.place(x=200, y=430, width=btn_w, height=30)

        # Face Detector Button
        image3 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\faceDetect.png")
        image3.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(image3)

        face_img_btn = Button(self.root, image=self.photoimg3, cursor="hand2",command=self.face_recognition)
        face_img_btn.place(x=500, y=280, width=btn_w, height=btn_h)

        face_text_btn = Button(self.root, text="Face Detector", cursor="hand2",command=self.face_recognition,
                               font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        face_text_btn.place(x=500, y=430, width=btn_w, height=30)

        # Attendance Button
        image4 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img1.png")
        image4.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(image4)

        att_img_btn = Button(self.root, image=self.photoimg4, cursor="hand2",command=self.attendance_data)
        att_img_btn.place(x=800, y=280, width=btn_w, height=btn_h)

        att_text_btn = Button(self.root, text="Attendance", cursor="hand2",command=self.attendance_data,
                              font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        att_text_btn.place(x=800, y=430, width=btn_w, height=30)

        # Help Button
        image5 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\help.png")
        image5.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(image5)

        help_img_btn = Button(self.root, image=self.photoimg5, cursor="hand2",command=self.help_data)
        help_img_btn.place(x=1100, y=280, width=btn_w, height=btn_h)

        help_text_btn = Button(self.root, text="Help Desk", cursor="hand2",command=self.help_data,
                               font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        help_text_btn.place(x=1100, y=430, width=btn_w, height=30)


         # train Button
        image6 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\train.png")
        image6.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(image6)

        train_img_btn = Button(self.root, image=self.photoimg6, cursor="hand2",command=self.train_data)
        train_img_btn.place(x=200, y=530, width=btn_w, height=btn_h)

        train_img_btn_text_btn = Button(self.root, text="Train Data", cursor="hand2",command=self.train_data,
                                font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        train_img_btn_text_btn.place(x=200, y=680, width=btn_w, height=30)

          # photos Button
        image7 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\photos.png")
        image7.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(image7)

        ph_img_btn = Button(self.root, image=self.photoimg7, cursor="hand2",command=self.open_img)
        ph_img_btn.place(x=500, y=530, width=btn_w, height=btn_h)

        ph_img_btn_text_btn = Button(self.root, text="Photos", cursor="hand2",command=self.open_img,
                                font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        ph_img_btn_text_btn.place(x=500, y=680, width=btn_w, height=30)


          # developer Button
        image8 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\dev.png")
        image8.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(image8)

        dev_img_btn = Button(self.root, image=self.photoimg8, cursor="hand2",command=self.developer_data)
        dev_img_btn.place(x=800, y=530, width=btn_w, height=btn_h)

        dev_img_btn_text_btn = Button(self.root, text="Developer", cursor="hand2",command=self.developer_data,
                                font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        dev_img_btn_text_btn.place(x=800, y=680, width=btn_w, height=30)

          # exit Button
        image9 = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\exit.png")
        image9.thumbnail((btn_w, btn_h), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(image9)

        ex_img_btn = Button(self.root, image=self.photoimg9, cursor="hand2",command=self.iExit)
        ex_img_btn.place(x=1100, y=530, width=btn_w, height=btn_h)

        ex_img_btn_text_btn = Button(self.root, text="Exit", cursor="hand2",command=self.iExit,
                                font=("times new roman", 15, "bold"), bg="dark blue", fg="white")
        ex_img_btn_text_btn.place(x=1100, y=680, width=btn_w, height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?")
        if self.iExit > 0:
            self.root.destroy()
        else:
            return


        # ================Function Buttons ================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
 
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

  




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
