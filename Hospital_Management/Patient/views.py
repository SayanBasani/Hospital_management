from django.shortcuts import render, redirect
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

from fpdf import FPDF
import datetime



# Pyrebase Authentication
firebaseConfig = {
  "apiKey": "AIzaSyA81y_aBfgggpkJBLvLWZjr9NqAQMg0d_U",
  "authDomain": "hospital-management-13dbb.firebaseapp.com",
  "databaseURL": "https://hospital-management-13dbb-default-rtdb.firebaseio.com",
  "projectId": "hospital-management-13dbb",
  "storageBucket": "hospital-management-13dbb.appspot.com",
  "messagingSenderId": "884809096216",
  "appId": "1:884809096216:web:9e37288095f205c499b76d",
  "measurementId": "G-ZPQQ1FCFP9",
  "databaseURL" : "https://hospital-management-13dbb-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)     
auth = firebase.auth()



#  For Firestore
storejson={
  "type": "service_account",
  "project_id": "hospital-management-13dbb",
  "private_key_id": "84cb1ef4134ad5bec6ef80ffe42a05565c7d18d5",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCubOPaCCQRWSf/\n/gZvSEZe4zL/63aq0+zkLJkxRxUIxhf1WjE+K19rGEQlbOAdwevNfwr2rFeImX3h\noWNI6l3wVptd7kCzH9P9gk2624HciP8wfKwUsywUKJhSIWh6tivlIGZLgxWXEu3x\n/3qGCmKn5Psq/Be55Uby/ONT8XJxE9l3y2BHdvO/mNxPdPmCMj7yrTSZtbS9M5hR\nFnKicFdJ3y5NUB/7yv/jf9lwfdCDFcZ0PUfCNIM4KBDwtjNhFmiNB/GVwQ1MHqGQ\noBqTKOWVE6iXKdJVPcz6iyp5aQpJb6Rdl6BDK0nXuAY8Th0LJLK6vzsZFapCrHGL\nKELC2+eFAgMBAAECggEAFZfQW0ZaZLVoq3BrToJ1h7tRAyKcsF2HpuBTNKkBPx1Q\nNk+ske7fo0vqlRwrNd6IY7ULCpTfnz7/45tNmxIR1WDQtL+meHuuYY9XMmnd4+B9\nKvz8IUc5uTh5/DeQ427C9LIJR+bZ7je/Mjq3lHlw/ipC4m7j5wpYZANk3G2jBmwY\n0e6tNTBHLCa3HI4Ni7GbxGhehA00pgXSWXxLU7j5VWHZ0g1+eA11ExDUjsZrFUy6\nqprMyMYXJy/fK4JUMVQ+yVPAHz8yJUEFXT8kwUBzh6zTswdAw/o0nnKZIo7+8svh\nOSdvk7ADglh/ew07ZJId232LDIjp+ePUOflerl3dvwKBgQDXQ/PJDPnHluiv/x/W\npQ0VoJVHl/E3TFwC9bF0tArYAFFtZ8wxeakrPo+k7aP80V8Z3q4yxfgEn3z9YUK3\nklnvoN3arjYvbU6nvT2gofzG+wDsLlivvyf5xxCCmGuTlIuLKm0tQuVmxaX4Ew1C\n6qALJ0np3g0TT6/zR+VqE6s8BwKBgQDPbogz3XK+PnlooW5GqLAHvehwoqxzSKjU\niJMlIX+l7eZ8ieJYQkfJIbm39dag8vTnfq7/KeNLbxMTlHPQVw4hKg5EGZI84/dX\nMJVYlSkg+uvNgBQoAvDkyDtgqaAFybTAZs24twdjh6kEycPpcSiSowRxg0WDnkQB\ngX4NTD81EwKBgANbXevete503gAQnHB+dmvF604Igox4Nl8dcbz+KcUgjCSGn9qN\nqSOxgA/0XMBOi4sdu92y1KFN02coIyA1ug1QluUYHmQy8i0PeGyO2iBIPcVxG5Ty\nCC+O+STwN40/ncV3zegMyQMHRgVOVsCaZBCIdlCdU9rfPUEv99XlpJ/1AoGAZ9wi\nGkXw48yIIZlii8J+kQHHVk49JmPlFLVlZ5wEO+KIGyc2y5Y0N0LJqJBQ7Ll5YkeN\n+3jPs79jv9P+wPw1uOlDx1k+XXqPJ3rN7FKTC05XrsdIUFhYoVSYVmfYFc3O0N8o\ndio+atlMCXe0vjfIZtN0sBlYPvSJfG+H28SniT0CgYBw0JlJgNeEj11IBfcvMSV9\niG2ossqSPOPgNS7qaRsDQXMR8tK2C6ioJApqT/zzMwhpy4OrJjH1YnzLv1rhZw93\n8wwogbaGnq8PiyI5OZnoUpHnCMDyuZoGAv/ey1QSop65i75I7kUvzmN9RnJhAY3w\nlk1L9E8UyzvDAnAXQcW13g==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ibcz3@hospital-management-13dbb.iam.gserviceaccount.com",
  "client_id": "104889979991036959017",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ibcz3%40hospital-management-13dbb.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(storejson)
if not firebase_admin._apps:
  firebase_admin.initialize_app(cred)

database = firestore.client()





# Create your views here.

def Registration(request):
    first_Name = request.POST.get("firstName")
    last_Name = request.POST.get("lastName")
    dob = request.POST.get("dob")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    password = request.POST.get("password")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    blood_Group = request.POST.get("bloodGroup")
    medical_History = request.POST.get("medicalHistory")

    full_Name = str(first_Name) +' '+ str(last_Name)

    patients_data= {"Full_Name":full_Name, "Gender":gender, "Date_of_Birth":dob, "Phone_Number":phone, "Address":address, "Blood_Group":blood_Group, "Medical_History":medical_History, "Email": email, "Password": password}

    try:
        auth.create_user_with_email_and_password(email, password)

        database.collection('Patients Database').document(email).set(patients_data)

        print(patients_data)
        print("Success!!")
        
    except:
       print("Something Went Wrong!!!")


    return render(request, "P_registration.html")
  

  
  
def prescription_login(request):
  
    pat_id = request.POST.get("patient_id")
    data = database.collection('Prescription Database').document(pat_id).get().to_dict()
    print("hello World")

    if data:
        return render(request, "prescription.html", {"prescription_data": data})

    return render(request, "patient_login.html")
  
  
  