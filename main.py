from flask import Flask, render_template, request
import requests
import smtplib
import re

app = Flask(__name__)

my_email = "bollywoodmelodysongs123@gmail.com"
password = "eusfitlkkxrftdzl"

@app.route('/')

def form_submit():
    return render_template('index.html')

@app.route('/login',methods=['POST'])

def login():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    if len(name)<3:
        return "Please enter your full name"
    if len(subject)<4:
        return "Please enter the subject "
    if len(message)<10:
        return "Please enter the message "
    if check(email)!=0:
        return 'Please enter valid email'
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user= my_email, password=password)
    #     response = connection.sendmail(from_addr= email, to_addrs= my_email, msg=f"Subject:{subject}\n\n Hello I am {name}\n Email:{email} \n Message:{message}")
    #     print(response)

    # create SMTP object
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    smtp_obj.starttls()

    # login with sender email and password
    smtp_obj.login(my_email, password)

    # send mail

    msg = f"Subject:{subject}\n\n Hello I am {name}\n Email:{email} \n Message:{message}"

    response = smtp_obj.sendmail(email, my_email, msg)

    # print response codes

    data = {'status':'200', 'message':'Message sent successfully.'}
    return data

def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return 0



if __name__ == '__main__':
    app.run(debug=True)
