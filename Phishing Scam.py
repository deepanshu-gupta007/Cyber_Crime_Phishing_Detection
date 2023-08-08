from tkinter import *
import csv
import webbrowser
import smtplib
import ssl
import random
otp=0
fname=''
phno=''
def FORM_PAGE5():
    global email_screen
    email_screen = Toplevel(email_screen)
    email_screen.title("Phishing Scam")
    email_screen.geometry("300x250")
    global  link
    global message
    link = StringVar()
    message=StringVar()
    Label(email_screen, text="Thank You for visiting our site!!", bg="green",fg="yellow").place(x=70,y=110)
    email_screen.mainloop()

def login():
    link=link.get()
    if link=='':
        message.set("Fill the empty field!!!")
    elif link=="abc123":
       message.set("Link is secured")
    else:
       message.set("Link is not secured!!!")

def FORM_PAGE4():
    global email_screen
    email_screen = Toplevel(form_page3)
    email_screen.title("Phishing Scam")
    email_screen.geometry("300x250")
    llfname=fname
    llphno=phno
    Label(email_screen,width="300", text="Your Dashboard", bg="green",fg="yellow").pack()
    Label(email_screen, text="Name").place(x=20,y=40)
    Label(email_screen, textvariable=llfname).place(x=160,y=40)
    Label(email_screen, text="Phone Number * ").place(x=20,y=70)
    Label(email_screen, textvariable=llphno).place(x=160,y=70)
    email_screen.mainloop()

def login_page4():
    entered_otp=eotp.get()
    llotp=otp
    if entered_otp == llotp:
        print("OTP verified successfully.")
        FORM_PAGE4()
    else:
        print("Invalid OTP.")
        
def sent_otp():
    global otp
    lotp=eotp.get()
    lemail=email.get()
    otp = str(random.randint(1000, 9999))
    sender_email = "testingboss341@gmail.com"
    receiver_email = lemail
    password = "eitprkyyhrumqmip"
    message = "Your OTP is " + otp
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("OTP sent successfully!")
    server.quit()

def FORM_PAGE3():
    global form_page3
    form_page3 = Toplevel()
    form_page3.title("Phishing Scam")
    form_page3.geometry("300x250")
    global eotp
    global email  
    eotp = StringVar()
    email = StringVar()
    Label(form_page3,width="300", text="Login Site", bg="green",fg="yellow").pack()
    Label(form_page3, text="Enter Email").place(x=15,y=40)
    Entry(form_page3, textvariable=email).place(x=80,y=40)
    Button(form_page3, text="Send OTP", width=10, height=1, bg="green",fg="yellow",command=sent_otp).place(x=215,y=38)
    Label(form_page3, text="Enter OTP").place(x=15,y=70)
    Entry(form_page3, textvariable=eotp).place(x=80,y=70)
    Button(form_page3, text="Submit", width=10, height=1, bg="green",fg="yellow",command=login_page4).place(x=90,y=110)
    form_page3.mainloop()

def login_PAGE2():
    lfname=fname.get()
    lemail=email.get()
    lphno=phno.get()
    if lfname=='' or lemail=='' or lphno=='':
        message.set("Fill the empty field!!!")
    else:
        f=open("Database.csv","w")
        wr=csv.writer(f)
        l=[lfname,lemail,lphno]
        wr.writerow(l)
        f.close()
        FORM_PAGE3()

def urlopen():
    new = 1
    url = link.get()
    if url=='https://www.testing.com':
        FORM_PAGE()
    else:
        webbrowser.open(url,new=new)

def FORM_PAGE():
    global form_page
    form_page = Toplevel(email_screen)
    form_page.title("Phishing Scam")
    form_page.geometry("300x250")
    global fname
    global phno
    global email
    global message
    fname = StringVar()
    phno = StringVar()
    email = StringVar()
    phno = StringVar()
    message = StringVar()
    Label(form_page,width="300", text="Create your account here", bg="green", fg="yellow").pack()
    Label(form_page, text="Full Name").place(x=25,y=40)
    Entry(form_page, textvariable=fname).place(x=120,y=40)
    Label(form_page, text="Email").place(x=25,y=70)
    Entry(form_page, textvariable=email).place(x=120,y=70)
    Label(form_page, text="Phone Number").place(x=25,y=100)
    Entry(form_page, textvariable=phno).place(x=120,y=100)
    Label(form_page, text="",textvariable=message).place(x=25,y=150)
    Button(form_page, text="Submit", width=10, height=1, bg="green", fg="yellow",command=login_PAGE2).place(x=100,y=150)
    form_page.mainloop()

def login():
    url=link.get()
    if "https://" in url:
       message.set("The '"+ url+ "', is secured")
    elif "http://" in url:
        message.set("The '"+ url+ "', is might be secured")
    else:
        message.set("The '"+ url+ "', is not secured")

def LinkForm():
    global email_screen
    email_screen = Tk()
    email_screen.title("Phishing Scam")
    email_screen.geometry("300x250")
    global  link
    global message
    link = StringVar()
    message = StringVar()
    Label(email_screen,width="300", text="Please enter details below", bg="green",fg="yellow").pack()
    Label(email_screen, text="Enter Link").place(x=50,y=40)
    Entry(email_screen, textvariable=link).place(x=120,y=40)
    Label(email_screen, text="",textvariable=message).place(x=30,y=100)
    Button(email_screen, text="Generate", width=10, height=1, bg="green",fg="yellow",command=login).place(x=100,y=70)
    Label(email_screen, text="Do you want to open it? ").place(x=78,y=120)
    Button(email_screen, text="Yes", width=5, height=1, bg="green",fg="yellow",command=urlopen).place(x=85,y=150)
    Button(email_screen, text="No", width=5, height=1, bg="green",fg="yellow",command=FORM_PAGE5).place(x=155,y=150)
    email_screen.mainloop()
LinkForm()
