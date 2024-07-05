import tkinter as tk
import assets as asset
from PIL import Image, ImageTk

import tkinter.messagebox as msgbox
import time

import welcomePage
import bookScanPage
import firebaseDB

class ScanBorrowPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()
        self.create_widgets()


    def create_widgets(self):
        self.scan_borrow_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2, bg='#FFFFFF')
        self.scan_borrow_page_fm.pack(pady=0)
        self.scan_borrow_page_fm.configure(width=890, height=780)

        qr_reader_icon = Image.open('images/qr_reader.png')
        resized_image_logo = qr_reader_icon.resize((200, 200), Image.LANCZOS)
        self.qr_reader_logo = ImageTk.PhotoImage(resized_image_logo)

        self.qr_reader_label = tk.Label(self.scan_borrow_page_fm, image=self.qr_reader_logo, bd=0, bg='#FFFFFF')
        self.qr_reader_label.place(x=340, y=85)

        self.code_scan_lb = tk.Label(self.scan_borrow_page_fm, text='QR 코드를 스캔하세요', font=('arial', 31, 'bold'), fg='#119F46', bg='white')
        self.code_scan_lb.place(x=230, y=320)

        self.qr_code_entry = tk.Entry(self.scan_borrow_page_fm, text='', highlightbackground=self.asstes.bg_color, highlightthickness=2, font=('', 25))
        self.qr_code_entry.place(x=245, y=400)
        self.qr_code_entry.focus()

        # self.qr_code_entry.insert(0, 'stud_02_02_008')

        self.qr_code_entry.bind('<Return>', lambda e: self.check_student(code=self.qr_code_entry.get()))
        self.qr_code_entry.focus()

        self.bottom_frame = tk.Frame(self.scan_borrow_page_fm, bg='#F5EBDD')
        self.bottom_frame.place(x=0, y=565)
        self.bottom_frame.configure(width=885, height=210)

        self.forward_welcome_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#FE853E', fg='white', bd=0, command=self.forwad_to_welcome_page)
        self.forward_welcome_btn.place(x=350, y=65)


    def check_student(self, code):
        result = firebaseDB.verify_student(code)

        if result is None:
            # print('등록되지 않은 회원입니다.')
            msgbox.showwarning('회원', '등록되지 않은 회원입니다')

            self.qr_code_entry.delete(0, tk.END)
            self.qr_code_entry.focus()
        else:
            if result['id'] == code:
                print('있는회원')
                self.forwad_to_bookSacn_page(code)
            else:
                # print('등록되지 않은 회원입니다.')
                msgbox.showwarning('회원', '등록되지 않은 회원입니다')

                self.qr_code_entry.delete(0, tk.END)
                self.qr_code_entry.focus()

    def forwad_to_welcome_page(self):
        self.scan_borrow_page_fm.destroy()
        self.update()

        welcome_page_fm = welcomePage.WelcomePage(self)
        welcome_page_fm.pack()

    def forwad_to_bookSacn_page(self, code):
        self.scan_borrow_page_fm.destroy()
        self.update()

        bookSacn_page = bookScanPage.BookScanPage(self, code)
        bookSacn_page.pack()

