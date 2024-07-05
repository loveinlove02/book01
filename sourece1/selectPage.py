import tkinter as tk
import assets as asset
from PIL import Image, ImageTk

import welcomePage
import borrowPage
import scanBorrowPage


class SelectPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()
        self.create_widgets()

    def create_widgets(self):
        self.select_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2,
                                       bg='#FFFFFF')
        self.select_page_fm.pack(pady=0)
        self.select_page_fm.configure(width=890, height=780)

        self.title_frame = tk.Frame(self.select_page_fm, bg=self.asstes.bg_color)
        self.title_frame.place(x=0, y=0)
        self.title_frame.configure(width=890, height=45)

        face_icon = Image.open('images/face.png')
        resized_image_logo = face_icon.resize((200, 200), Image.LANCZOS)
        self.face_logo = ImageTk.PhotoImage(resized_image_logo)

        self.face_button = tk.Button(self.select_page_fm, image=self.face_logo, bd=0, bg='#FFFFFF',
                                     command=self.forwad_to_borrow_page)
        self.face_button.place(x=150, y=190)

        scan_icon = Image.open('images/scan.png')
        resized_image_logo = scan_icon.resize((220, 200), Image.LANCZOS)
        self.scan_logo = ImageTk.PhotoImage(resized_image_logo)

        self.scan_button = tk.Button(self.select_page_fm, image=self.scan_logo, bd=0, bg='#FFFFFF',
                                     command=self.forwad_to_scan_borrow_page)
        self.scan_button.place(x=520, y=190)

        self.face_label = tk.Label(self.select_page_fm, text='얼굴 인식', font='arial 25', bg='#FFFFFF')
        self.face_label.place(x=180, y=430)

        self.scan_label = tk.Label(self.select_page_fm, text='QR 스캔', font='arial 25', bg='#FFFFFF')
        self.scan_label.place(x=565, y=430)

        self.bottom_frame = tk.Frame(self.select_page_fm, bg='#F5EBDD')
        self.bottom_frame.place(x=0, y=565)
        self.bottom_frame.configure(width=885, height=210)

        self.forward_welcome_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#FE853E',
                                             fg='white', bd=0, command=self.forwad_to_welcome_page)
        self.forward_welcome_btn.place(x=350, y=65)

    def forwad_to_scan_borrow_page(self):
        self.select_page_fm.destroy()
        self.update()

        scan_borrow_page_fm = scanBorrowPage.ScanBorrowPage(self)
        scan_borrow_page_fm.pack()

    def forwad_to_borrow_page(self):
        self.select_page_fm.destroy()
        self.update()

        borrow_page_fm = borrowPage.BorrowPage(self)
        borrow_page_fm.pack()

    def forwad_to_welcome_page(self):
        self.select_page_fm.destroy()
        self.update()

        welcome_page_fm = welcomePage.WelcomePage(self)
        welcome_page_fm.pack()





