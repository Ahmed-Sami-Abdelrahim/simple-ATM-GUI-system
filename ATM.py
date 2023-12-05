

from tkinter import *
from customers import *



def Confirm_withdrawal():
    for i,y in customers.items():
        if i == ID_N :
            if (withdraw1.get() <= y[2]):
                if (withdraw1.get() <=5000) and (withdraw1.get() >=100) and (withdraw1.get() %100==0):
                    Label(w7,text="Thank You!",background="darkred",font=("arial",14),fg="white",width=55).place(x=0,y=360)
                    y[2] -=  withdraw1.get()
                    w7.after(3000,main.deiconify)
                elif(withdraw1.get() > 5000) or (withdraw1.get() < 100):
                    Label(w7,text="The maximum amount is 5,000 L.E and the minimum amount is 100 L.E! Try Again.",background="darkred",font=("arial",12),fg="white").place(x=15,y=362)
                    entry7.delete(0,END)
                elif (withdraw1.get() <=5000) and (withdraw1.get() >=100) and not  (withdraw1.get() %100==0):
                    Label(w7,text="Multiples of 100 only! Try Again.",background="darkred",font=("arial",14),fg="white",width=55).place(x=0,y=360)
                    entry7.delete(0,END)
            elif withdraw1.get() > y[2]:
                Label(w7,text="No sufficient balance!",background="darkred",font=("arial",14),fg="white",width=55).place(x=0,y=360)
                w7.after(3000,main.deiconify)


def Cash_Withdraw():
    global withdraw1
    withdraw1 = IntVar()
    global entry7
    global w7
    
    w7 = Toplevel(main)
    w7.geometry("600x500+200+200")
    w7.resizable(False,False)
    w7.configure(background="darkred")
    w7.title("ATM")
    
    Frame(w7,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w7,width=600,height=30,background="black").place(x=0,y=0)
    
    Label(w7,text="Cash Withdraw",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    Label(w7,text="Please enter the amount you want to withdrew",background="darkred",font=("arial",14),fg="white").place(x=120,y=240)
    
    entry7=Entry(w7,width=50,textvariable=withdraw1)
    entry7.place(x=150,y=280)
    entry7.delete(0,END)
    
    Button(w7,text="Enter",bg="black",fg="white",font=("arial",12),command=Confirm_withdrawal).place(x=280,y=320)
    Button(w7,text="Back",font=("arial",14),bg="black", fg="white",width=5,command=w7.withdraw).place(x=500,y=45)
    

def Balance_Inquiry ():
    global w3
    global Id_number
   
    w3 = Toplevel(main)
    w3.geometry("600x500+200+200")
    w3.resizable(False,False)
    w3.configure(background="darkred")
    w3.title("ATM")
    
    Frame(w3,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w3,width=600,height=30,background="black").place(x=0,y=0)
    
    Label(w3,text="",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    Label(w3,text="Balance",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    
    Button(w3,text="Ok",font=("arial",12),bg="black",fg="white",command=main.deiconify).place(x=280,y=360)

    for i,y in customers.items():
        if i == ID_N:
            Label(w3,text=f"Hello, {y[0]}!",background="darkred",font=("arial",22),fg="white").place(x=100,y=200)
            Label(w3,text=f"Your Balance is {y[2]} L.E",background="darkred",font=("arial",22),fg="white").place(x=100,y=250)

    Button(w3,text="Back",font=("arial",14),bg="black", fg="white",width=5,command=w3.withdraw).place(x=500,y=45)
            

def Confirm_Password():
    
    count=0
    for i,y in customers.items():
        if i == ID_N:
            if Confirm_pass.get() == New_pass.get():
                for i in New_pass.get() :
                    if (i >= '0' and i <= '9'):
                        count +=1
                if count ==4:
                    y[1] = New_pass.get()
                    Label(w4,text="Password has been changed successfully.",background="darkred",font=("arial",14),fg="white").place(x=130,y=400)
                    Button(w4,text="Go to Home",font=("arial",12),bg="black",fg="white",command=main.deiconify).place(x=250,y=430)

                elif count !=4: 
                    Label(w4,text="4 numbers only!",background="darkred",font=("arial",14),fg="white",width=45).place(x=50,y=400)
            elif Confirm_pass.get() != New_pass.get():
                Label(w4,text="Password does not match!",background="darkred",font=("arial",14),fg="white",width=45).place(x=50,y=400)




def Password_Change():
    global New_pass
    global Confirm_pass
    New_pass = StringVar()
    Confirm_pass = StringVar()
    global w4
    w4 = Toplevel(main)
    w4.geometry("600x500+200+200")
    w4.resizable(False,False)
    w4.configure(background="darkred")
    w4.title("ATM")
    
    Frame(w4,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w4,width=600,height=30,background="black").place(x=0,y=0)
    
    Label(w4,text="Password Change",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    Label(w4,text="Please enter new password",background="darkred",font=("arial",14),fg="white").place(x=180,y=240)
    Label(w4,text="Please confirm new password",background="darkred",font=("arial",14),fg="white").place(x=180,y=300)
    
    entry3=Entry(w4,width=50,textvariable=New_pass,show ="*")
    entry4=Entry(w4,width=50,textvariable=Confirm_pass,show ="*")
    
    entry3.place(x=150,y=270)
    entry4.place(x=150,y=330)
    

    Button(w4,text="Change password",font=("arial",12),bg="black",fg="white",command=Confirm_Password).place(x=230,y=370)
    Button(w4,text="Back",font=("arial",14),bg="black", fg="white",width=5,command=w4.withdraw).place(x=500,y=45)
    


def Confirm_Recharge():
    count=0
    for i in Number_send.get() :
        if (i >= '0' and i <= '9'):
            count +=1
    if count ==11:
        for z,y in customers.items():
            if z == ID_N :
                if Amount_send.get() <= (y[2]):

                    Label(w6,text=f"{Amount_send.get()} L.E has been sent to {Number_send.get()}",background="darkred",font=("arial",14),fg="white").place(x=120,y=390)
                    y[2] -=  Amount_send.get()
                elif Amount_send.get() > (y[2]):
                    Label(w6,text=f"No sufficient balance!",background="darkred",font=("arial",14),fg="white",width=40).place(x=80,y=390)
                
                Button(w6,text="Go to Home",font=("arial",12),bg="black",fg="white",command=main.deiconify).place(x=250,y=430)
                
    elif count != 11:
        Label(w6,text=f"number must be 11",background="darkred",font=("arial",14),fg="white",width=40).place(x=80,y=390)
            
        


def Recharge():
    global w6
    global Number_send
    global Amount_send
    Number_send = StringVar()
    Amount_send = IntVar()
    
    w6 = Toplevel(main)
    w6.geometry("600x500+200+200")
    w6.resizable(False,False)
    w6.configure(background="darkred")
    w6.title("ATM")
    
    Frame(w6,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w6,width=600,height=30,background="black").place(x=0,y=0)

    Label(w6,text="Recharge",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    Label(w6,text="Please enter the number to send to",background="darkred",font=("arial",14),fg="white").place(x=150,y=240)
    Label(w6,text="Please enter amount of recharge",background="darkred",font=("arial",14),fg="white").place(x=160,y=300)

    
    entry5=Entry(w6,width=50,textvariable=Number_send)
    entry6=Entry(w6,width=50,textvariable=Amount_send)
    entry5.place(x=150,y=270)
    entry6.place(x=150,y=330)
    
    entry6.delete(0,END)
    
    Button(w6,text="Send",font=("arial",12),bg="black",fg="white",command=Confirm_Recharge).place(x=270,y=360)
    Button(w6,text="Back",font=("arial",14),bg="black", fg="white",width=5,command=w6.withdraw).place(x=500,y=45)
    
   

def Fawry_Service():

    global w5
    w5 = Toplevel(main)
    w5.geometry("600x500+200+200")
    w5.resizable(False,False)
    w5.configure(background="darkred")
    w5.title("ATM")
    
    Label(w5,text="Fawry Service",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    Frame(w5,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w5,width=600,height=30,background="black").place(x=0,y=0)

    Button(w5,text="Orange Recharge",font=("arial",20),width=15,bg="black", fg="white",command=Recharge).place(x=30,y=150)
    Button(w5,text=" Etisalat Recharge",font=("arial",20),width=15,bg="black", fg="white",command=Recharge).place(x=320,y=150)
    Button(w5,text="Vodafone Recharge",font=("arial",20),width=15,bg="black", fg="white",command=Recharge).place(x=320,y=300)
    Button(w5,text="We Recharge",font=("arial",20),width=15,bg="black", fg="white",command=Recharge).place(x=30,y=300)
    Button(w5,text="Back",font=("arial",14),bg="black", fg="white",width=5,command=w5.withdraw).place(x=500,y=45)



def options():
    global w2
    w2 = Toplevel(main)
    w2.geometry("600x500+200+200")
    w2.resizable(False,False)
    w2.configure(background="darkred")
    w2.title("ATM")
    
    Label(w2,text="Options",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
    
    Frame(w2,width=600,height=30,background="black").place(x=0,y=470)
    Frame(w2,width=600,height=30,background="black").place(x=0,y=0)

    Button(w2,text="Cash Withdraw",font=("arial",20),width=15,bg="black", fg="white",command=Cash_Withdraw).place(x=30,y=150)
    Button(w2,text="Balance Inquiry",font=("arial",20),width=15,bg="black", fg="white",command=Balance_Inquiry).place(x=320,y=150)
    Button(w2,text="Password Change",font=("arial",20),width=15,bg="black", fg="white",command=Password_Change).place(x=320,y=300)
    Button(w2,text="Fawry Service",font=("arial",20),width=15,bg="black", fg="white",command=Fawry_Service).place(x=30,y=300)
    Button(w2,text="Exit",font=("arial",14),bg="black", fg="white",width=5,command=main.deiconify).place(x=500,y=45)


def password():
    global flag
    global ID_N
    PASS_N = id_password.get()
    for i in customers:
        if i  ==ID_N:
            if PASS_N == customers[i][1]  :
                options() 
                break
            else:
                flag-=1
                Label(w1,text=f"Incorrect password! {flag} left",background="darkred",font=("arial",13),fg="white",width=40).place(x=120,y=400)
        
    if flag == 0: 
            Label(w1,text=f"Account is locked! Please go to the branch.",background="darkred",font=("arial",13),fg="white").place(x=140,y=400)
            w1.after(2000,main.deiconify)

            for j in customers:
                if j == ID_N:
                    customers[j][3] = "Blocked"
                    flag=3
                    break



def ID():
    global ID_N
    ID_N = Id_number.get()
    if ID_N not in customers:
        Label(main,text="Invalid ID number! ",background="darkred",font=("arial",12),fg="white",width=40).place(x=120,y=400)
        entry1.delete(0,END)
    else:
        for i in customers:
            if i == ID_N:
                if customers[i][3] == "Blocked":
                    Label(main,text=f"Account is locked! Please go to the branch.",background="darkred",font=("arial",13),fg="white").place(x=140,y=400)
                    break
                else:
                    global w1
                    w1 = Toplevel(main)
                    w1.geometry("600x500+200+200")
                    w1.resizable(False,False)
                    w1.configure(background="darkred")
                    w1.title("ATM")

                    Label(w1,text="Password",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
                    Frame(w1,width=600,height=30,background="black").place(x=0,y=470)
                    Frame(w1,width=600,height=30,background="black").place(x=0,y=0)

                    Label(w1,text="Please enter your password",background="darkred",font=("arial",14),fg="white").place(x=180,y=300)
                    entry2=Entry(w1,width=50,textvariable=id_password,show ="*")
                    entry2.place(x=150,y=330)
                    
                    Button(w1,text="Enter",font=("arial",12),bg="black",fg="white",command=password).place(x=275,y=360)
                    
                    entry1.delete(0,END)
                    entry2.delete(0,END)
       
                    break


                


main = Tk()

main.geometry("600x500+200+200")
main.resizable(False,False)
main.configure(background="darkred")
main.title("ATM")

Id_number=StringVar()
id_password= StringVar()
flag =3

Label(main,text="Home",background="darkred",font=("arial",24),fg="white").place(x=20,y=40)
Label(main,text="Welcome to ASB",background="darkred",font=("arial",40),fg="white").place(x=100,y=180)
Label(main,text="Please enter your account number",background="darkred",font=("arial",14),fg="white").place(x=155,y=300)

Frame(main,width=600,height=30,background="black").place(x=0,y=470)
Frame(main,width=600,height=30,background="black").place(x=0,y=0)

entry1=Entry(main,width=50,textvariable=Id_number)
entry1.place(x=150,y=330)

Button(main,text="Enter",bg="black",fg="white",font=("arial",12),command=ID).place(x=275,y=360)




main.mainloop()

