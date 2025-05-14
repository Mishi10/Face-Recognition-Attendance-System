from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # type: ignore
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background

        
         # ================== Title ===================
        title_lbl = Label(self.root, text=" TRAIN DATA SET", font=("times new roman", 32, "bold"), bg="white", fg="red",anchor="center")
        title_lbl.place(x=0, y=0, width=1560, height=45)

        # image
        img_top = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img4.png")
        img_top= img_top.resize((1560,325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top, bg="#f5f5dc")
        f_lbl.place(x=0, y=45, width=1560, height=325)

        # Button

        student_img_btn = Button(self.root,text="TRAIN DATA"  , command= self.train_classifier,cursor="hand2",font=("times new roman", 30, "bold"), bg="blue", fg="white")
        student_img_btn.place(x=0, y=370, width=1560, height=60)

        img_bottom = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\photos.png")
        img_bottom= img_bottom.resize((1560,325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl1 = Label(self.root, image=self.photoimg_bottom, bg="#f5f5dc")
        f_lbl1.place(x=0, y=430, width=1560, height=325)


    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for images in path:
            img=Image.open(images).convert('L')  #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(images)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Training the classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier..xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


         

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
