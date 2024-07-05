import tkinter as tk
from PIL import Image, ImageTk
import cv2

import assets as asset
import welcomePage
import verifyPage

import time

class BorrowPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()
        self.create_widgets()

    def create_widgets(self):
        self.borrow_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2, bg='#FFFFFF')
        self.borrow_page_fm.pack(pady=0)
        self.borrow_page_fm.configure(width=890, height=780)

        self.title_frame = tk.Frame(self.borrow_page_fm, bg=self.asstes.bg_color)
        self.title_frame.place(x=0, y=0)
        self.title_frame.configure(width=890, height=45)

        self.add_pic_section_fm = tk.Frame(self.borrow_page_fm, highlightbackground=self.asstes.bg_color, highlightthickness=2)
        self.add_pic_section_fm.place(x=230, y=100, width=450, height=380)

        self.select = None
        self.current_image = None

        self.video_capture = cv2.VideoCapture(0)
        self.canvas = tk.Canvas(self.add_pic_section_fm, width=420, height=420)
        self.canvas.pack(pady=15)

        self.update_webcam()


        self.bottom_frame = tk.Frame(self.borrow_page_fm, bg='#F5EBDD')
        self.bottom_frame.place(x=0, y=565)
        self.bottom_frame.configure(width=885, height=210)

        self.recogntion_btn = tk.Button(self.bottom_frame, text='본인 인증', font='arial 30 bold', bg='#4285F4', fg='white',
                                        bd=0, command=self.recognize_image)
        self.recogntion_btn.place(x=230, y=50)

        self.forward_welcome_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#FE853E',
                                             fg='white', bd=0, command=self.forwad_to_welcome_page)
        self.forward_welcome_btn.place(x=470, y=50)



    def update_webcam(self):
        self.ret, self.frame = self.video_capture.read()
        self.current_image = Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        self.photo = ImageTk.PhotoImage(image=self.current_image)
        self.canvas.create_image(110, 110, image=self.photo)
        self.after_id = self.borrow_page_fm.after(15, self.update_webcam)


    def recognize_image(self):
        cv2.imwrite('image/photo.jpg', self.frame)  # 웹 캠에서 사진을 찍어서 저장
        self.video_capture.release()  # 자원 반납
        cv2.destroyAllWindows()  # 윈도우 닫기

        time.sleep(0.5)

        self.borrow_page_fm.destroy()
        self.update()

        verify_page_fm = verifyPage.VerifyPage(self)
        verify_page_fm.pack()




    def forwad_to_welcome_page(self):
        self.borrow_page_fm.destroy()
        self.update()

        welcome_page_fm = welcomePage.WelcomePage(self)
        welcome_page_fm.pack()