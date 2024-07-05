import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, storage

cred = credentials.Certificate('firebase2.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://water-7f5cb.firebaseio.com/',
    'storageBucket' : 'water-7f5cb.appspot.com'
})

def verify_student(code):
    ref = db.reference('library/member/' + code)
    return ref.get()

def get_student_id():
    ref = db.reference('library/member')
    users_id = list(ref.get().keys())

    return users_id

def download_image():
    ref = db.reference('library/member')
    users_id = list(ref.get().keys())

    bucket = storage.bucket()
    local_path = 'download_image'

    for remote_path in users_id:
        print(remote_path)
        get_blob = bucket.blob(remote_path + '.jpg')
        get_blob.download_to_filename(local_path + '/' + remote_path + '.jpg')
        # print(remote_path + '.jpg', '다운로드')



def get_student_password(student_id):
    student_id = 'stud_02_02_008'
    ref = db.reference('library/member/' + student_id)
    return ref.get()['pw']

# download_image()

