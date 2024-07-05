import tkinter as tk
from PIL import Image, ImageTk
import cv2
import face_recognition as fr
import os
import os.path

import firebaseDB

import assets as asset
import welcomePage
import bookScanPage

class VerifyPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()

        firebaseDB.download_image()

        self.face_path = 'download_image'
        self.face_encodings, self.face_names = self.get_face_encodings()

        self.create_widgets()

    def create_widgets(self):
        self.verify_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2, bg='#FFFFFF')
        self.verify_page_fm.pack(pady=0)
        self.verify_page_fm.configure(width=890, height=780)

        self.title_frame = tk.Frame(self.verify_page_fm, bg=self.asstes.bg_color)
        self.title_frame.place(x=0, y=0)
        self.title_frame.configure(width=890, height=45)

        self.bottom_frame = tk.Frame(self.verify_page_fm, bg='#F5EBDD')
        self.bottom_frame.place(x=0, y=565)
        self.bottom_frame.configure(width=885, height=210)

        verify_check = self.verify_check()
        print(verify_check)

        if verify_check[0] == 'yes':
            user_id = verify_check[1]

            # user_id = 'abcde'
            self.verify_member_lb = tk.Label(self.verify_page_fm, text='비빌번호를 입력해주세요.', font=('arial', 31, 'bold'), fg='#119F46', bg='white')
            self.verify_member_lb.place(x=200, y=250)

            self.password_entry = tk.Entry(self.verify_page_fm, text='', highlightbackground=self.asstes.bg_color, highlightthickness=2, font=('', 25))
            self.password_entry.config(show='*')
            self.password_entry.focus()
            self.password_entry.place(x=280, y=340, width=320)
            self.password_entry.bind('<Return>', lambda e: self.check_password(user_id=user_id, password=self.password_entry))

            # self.password_check_btn = tk.Button(self.bottom_frame, text='확인', font='arial 30 bold', bg='#4285F4', fg='white', bd=0, command=lambda : self.check_password(user_id=user_id, password=self.password_entry))
            # self.password_check_btn.place(x=380, y=64)

            self.password_check_btn = tk.Button(self.bottom_frame, text='입력 완료', font='arial 30 bold', bg='#4285F4', fg='white', bd=0, command=lambda : self.check_password(user_id=user_id, password=self.password_entry))
            self.password_check_btn.place(x=230, y=50)

            self.forward_welcome_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#FE853E', fg='white', bd=0, command=self.forwad_to_welcome_page)
            self.forward_welcome_btn.place(x=470, y=50)


        else:
            self.verify_member_lb = tk.Label(self.verify_page_fm, text='등록되지 않은 회원입니다.', font=('arial', 31, 'bold'), fg='#119F46', bg='white')
            self.verify_member_lb.place(x=200, y=250)

            self.verify_member_resister_lb = tk.Label(self.verify_page_fm, text='회원등록 후 이용해주세요.', font=('arial', 25, 'bold'),
                                             fg='#FE2E2E', bg='white')
            self.verify_member_resister_lb.place(x=240, y=320)

            self.recogntion_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#4285F4', fg='white', bd=0, command=self.forwad_to_welcome_page)
            self.recogntion_btn.place(x=335, y=64)




    def get_face_encodings(self):
        face_names = os.listdir(f'{self.face_path}')
        face_encodings = []

        for i, name in enumerate(face_names):
            # 사진에서 얼굴 영역을 알아내고, 얼굴 특징의 위치를 분석한 데이터를 face_encodings 리스트에 저장합니다.
            face = fr.load_image_file(f'{self.face_path}//{name}')  # img/02-20011100(kang).jpg
            face_encodings.append(fr.face_encodings(face)[0])

            face_names[i] = name.split('.')[0]

        return face_encodings, face_names


    def verify_check(self):
        image = cv2.imread('image/photo.jpg')  # 읽어온 이미지
        return_value = 'no'
        name = 'no'

        scl = 2  # 이미지 크기를 조정하는 데 사용할 변수 설정

        # image에서 frame을 읽어서 1/2 크기로 줄입니다. 계산양을 줄이기 위해서 입니다.
        resized_image = cv2.resize(image, (int(image.shape[1] / scl), int(image.shape[0] / scl)))

        # resized_image를 RGB로 변환
        rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        #  RGB로 바꾼 현재 프레임의 얼굴 위치 좌표를 검색
        face_locations = fr.face_locations(rgb_image)


        # RGB로 변경한 현재 프레임에서 얼굴 영역과 특징을 추출합니다.
        # 현재 프레임의 얼굴 위치 좌표(face_locations) 사용
        unknown_encodings = fr.face_encodings(rgb_image, face_locations)

        # Iterating through each encoding, as well as the face's location
        # unknown_encodings(얼굴영역의 특징),  face_locations(RGB로 바꾼 현재 프레임의 얼굴 위치 좌표)
        for face_encoding, face_location in zip(unknown_encodings, face_locations):

            # Comparing known faces with unknown faces
            result = fr.compare_faces(self.face_encodings, face_encoding, 0.4)
            print(result)

            # [False, False, False, False, False, False, True]

            if True in result:  # result 리스트에 True 가 있으면 찾은 사람이 있다
                name = self.face_names[result.index(True)]
                return_value = 'yes'

        return return_value, name


    def forwad_to_welcome_page(self):
        self.verify_page_fm.destroy()
        self.update()

        welcome_page_fm = welcomePage.WelcomePage(self)
        welcome_page_fm.pack()


    def check_password(self, user_id, password):
        get_password = firebaseDB.get_student_password(user_id)      # 데이터베이스에서 가져와야 된다.
        # get_password = '1234'

        if str(password.get()) == str(get_password):
            # print('비밀번호 일치')
            self.verify_page_fm.destroy()
            self.update()

            book_scan_page_fm = bookScanPage.BookScanPage(self, user_id)
            book_scan_page_fm.pack()

        else:
            print('비밀번호 잘못입력')