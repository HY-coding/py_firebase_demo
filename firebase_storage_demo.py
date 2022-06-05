import Constants
import pyrebase

print("Firebase demo")

config = Constants.FIREBASE_CONFIG

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

email = Constants.EMAIL
password = Constants.PASSWORD

try:
    user = auth.sign_in_with_email_and_password(email, password)
    
except:
    print("auth fail, please check email and passowrd")
    exit()        

storage= firebase.storage()

#featur1: upload a file to storage
print("Upload file1.txt to cloud")
local_file = "file1.txt"
cloud_file = "file1_cloud.txt"
storage.child(cloud_file).put(local_file, user['idToken'])

#featur2: download a file from storage
print("Download file1_cloud.txt to local")
downloaded_file = "file1_cloud_downloaded.txt"
storage.child(cloud_file).download(downloaded_file,user['idToken'])

