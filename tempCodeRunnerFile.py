from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector  # type: ignore
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="#f5f5dc")  # Beige background

             # ================== Title ===================
        title_lbl = Label(self.root, text=" FACE RECOGNITION", font=("times new roman", 32, "bold"), bg="white", fg="blue",anchor="center")
        title_lbl.place(x=0, y=0, width=1560, height=45)

        # image
        img_l = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img5.png")
        img_l= img_l.resize((650,700), Image.Resampling.LANCZOS)
        self.photoimg_l = ImageTk.PhotoImage(img_l)
        f_lbl = Label(self.root, image=self.photoimg_l, bg="#f5f5dc")
        f_lbl.place(x=0, y=45, width=650, height=700)


        img_r = Image.open(r"C:\Users\manisha\OneDrive\Desktop\Face recognition\college images\img6.png")
        img_r= img_r.resize((950,700), Image.Resampling.LANCZOS)
        self.photoimg_r = ImageTk.PhotoImage(img_r)
        f_lbl = Label(self.root, image=self.photoimg_r, bg="#f5f5dc")
        f_lbl.place(x=650, y=45, width=950, height=700)


         # Button

        btn1 = Button(f_lbl,text="Face Recognition"  ,cursor="hand2",command=self.face_recog,font=("times new roman", 18, "bold"), bg="red", fg="white")
        btn1.place(x=465, y=650, width=200, height=40)

        BOTTOM_lbl = Label(self.root, text=" Frontal Face Detector", font=("times new roman", 25, "bold"), bg="white", fg="blue",anchor="center")
        BOTTOM_lbl.place(x=0, y=750, width=1560, height=40)


#==========face recognition========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            coordinates = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int((100) * (1 - (predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Mishi1010",
                                            database="face_recognizer")
                cur = conn.cursor()
                cur.execute("SELECT Name FROM student WHERE StudentId = %s", (id,))
                n = "+".join(cur.fetchone())

                cur.execute("SELECT Roll FROM student WHERE StudentId = %s", (id,))
                r = "+".join(cur.fetchone())

                cur.execute("SELECT Dep FROM student WHERE StudentId = %s", (id,))
                d = "+".join(cur.fetchone())

                if confidence > 77:
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coordinates = [x, y, w, h]
            return coordinates

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
