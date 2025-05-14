from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # type: ignore
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background

         
         # ================== Title ===================
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 32, "bold"), bg="white", fg="blue",anchor="center")
        title_lbl.place(x=0, y=0, width=1560, height=45)

        # image
        img_top = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img7.png")
        img_top= img_top.resize((1560,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top, bg="#f5f5dc")
        f_lbl.place(x=0, y=45, width=1560, height=720)

         #frame

        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=590)

          
        dev_label = Label(main_frame, text="Hello!! This is Manisha", font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="I am full stack developer", font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()