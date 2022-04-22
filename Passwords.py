from tkinter import Entry,Label,Button,END,LEFT,RIGHT,Scale,HORIZONTAL,PhotoImage,Tk,messagebox
from sqlite3 import connect
from random import choice
from os import listdir,remove,system
from time import sleep
from pyautogui import size
from rich import print
from filelock import FileLock
#-------Functions------
def Ok():
    global pass1,pass2,pass3,passwh,a,b,d
    pass1 = Ent1.get()
    pass2 = Ent2.get()
    pass3 = Ent3.get()
    spass1 = Ent4.get()
    spass2 = Ent5.get()
    spass3 = Ent6.get()
    if len(asd) <=10000:
        c.execute('''CREATE TABLE IF NOT EXISTS Defultpasswords
                    (Pass1 text,
                    Pass2 text,
                    Pass3 text,
                    a integer,
                    b integer,
                    d real
                                        )''')
        c.execute('''INSERT INTO Defultpasswords VALUES(:Pass1,:Pass2,:Pass3,:a,:b,:d)''' , {'Pass1' : pass1,'Pass2' : pass2,'Pass3' : pass3,'a' : spass1,'b' : spass2,'d' : spass3})
        con.commit()  
        label1.destroy()
        label2.destroy()
        label3.destroy()
        Ent1.destroy()
        Ent2.destroy()
        Ent3.destroy()
        Ent4.destroy()
        Ent5.destroy()
        Ent6.destroy()
        label4.destroy()
        label5.destroy()
        label6.destroy()
        btn.destroy()
        welcome()
    c.execute('SELECT * FROM Defultpasswords')
    passwh = (c.fetchone())
def Input():
    global label1,label2,label3,Ent1,Ent2,Ent3,btn,con,c,pass1,pass2,pass3,label6,label5,label4,Ent4,Ent5,Ent6
    window.configure(bg='paleturquoise')
    con = connect('Passwordsd.db')
    c = con.cursor()
    label1 = Label(window,text='Enter First Password : ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label1.pack()
    Ent1 = Entry(window,bd=4,font='italic 12')
    Ent1.pack()
    label2 = Label(window,text='Enter Second Password : ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label2.pack()
    Ent2 = Entry(window,bd=4,font='italic 12')
    Ent2.pack()
    label3 = Label(window,text='Enter Third Password : ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label3.pack()
    Ent3 = Entry(window,bd=4,font='italic 12')
    Ent3.pack()
    label4 = Label(window,text='Enter First scale Password between 0.0~1.0 : ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label4.pack()
    Ent4 = Entry(window,bd=4,font='italic 12')
    Ent4.pack()
    label5 = Label(window,text='Enter Second scale Password between 0~10: ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label5.pack()
    Ent5 = Entry(window,bd=4,font='italic 12')
    Ent5.pack()
    label6 = Label(window,text='Enter Third scale Password between 0~100: ',bg='paleturquoise',fg='firebrick',font='italic 12 bold')
    label6.pack()
    Ent6 = Entry(window,bd=4,font='italic 12')
    Ent6.pack()
    btn = Button(window, text='Ready',command=Ok,bd=12,bg='lightgreen')
    btn.pack() 
def init():
    global c,con
    'initioilizing a new database'
    con = connect('Passwordsd.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Privacy
                (site text,
                Fullname text,
                username text,
                Password text,
                email text,
                Number text,
                counterd text
                                )''')
    con.commit()
init()
poi = 0
def add():
    global LBL5,lst,poi
    if poi == 1:
        print('for your security you can not add two sites togather!!!')
        sleep(4)
        window.destroy()
    con = connect('Passwordsd.db')
    c = con.cursor()
    c.execute('INSERT INTO Privacy VALUES(:site,:Fullname,:username,:Password,:emial,:Number,:counterd)', {'site' : En1.get(), 'Fullname':En2.get(), 'username':En3.get(),'Password':En4.get(),'emial': En5.get(),'Number' : En6.get(),'counterd' : '1'}) 
    con.commit()
    #----------------
    poi+=1
    En1.delete(0,END)
    En2.delete(0,END)
    En3.delete(0,END)
    En4.delete(0,END)
    En5.delete(0,END)
    En6.delete(0,END)
    LBL5 = Label(window,text='Item Added',fg='red',font=('italic 18 bold'),bg='lightgreen')
    LBL5.pack()
Colors = ['red','skyblue','blue','brown','black']
def Showp():  
    c.execute('SELECT * FROM privacy')
    b = c.fetchall()

    for i in b:   
        lsttt = ['black', 'purple', 'red','black' ,'cyan' , 'magenta','firebrick','crimson','teal']
        Label(window, text=f'Sitename : {i[0]} | Fullname : {i[1]} | Username : {i[2]} | Password : {i[3]} | Email : {i[4]} | Number : {i[5]}',fg=choice(lsttt),font='italic 14 bold',bg='khaki').pack()
    window.config(bg='khaki')
    con.close()
def Show_Site():
    global LBL5
    LBL.destroy()
    Btn2.destroy()
    Btn3.destroy()
    lbls = Label(window,text=Showp())
    lbls.pack()

def Show_site():
    try:
        lb1.destroy()
        lb2.destroy()
        lb3.destroy()
        lb4.destroy()
        lb5.destroy()
        lb6.destroy()
        En1.destroy()
        En2.destroy()
        En3.destroy()
        En4.destroy()
        En5.destroy()
        En6.destroy()
        Btn5.destroy()
        Btn4.destroy()
        lbls = Label(window,text=Showp())
        lbls.pack()  
        LBL5.destroy()
    except NameError:
        print('')
def add_Site():
    global lb1,lb2,lb3,lb4,lb5,lb6,lb1,En1,En2,En3,En4,En5,En6,Btn4,Btn5
    LBL.destroy()
    Btn2.destroy()
    Btn3.destroy()
    lb1 = Label(window,text='Enter Sitename',bg='lightgreen',font='italic 14 bold',bd=10)
    lb1.pack()
    En1 = Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En1.pack()
    lb2 = Label(window,text='Enter Fullname',bd=10,font='italic 14 bold',bg='lightgreen')
    lb2.pack()
    En2 = Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En2.pack()
    lb3 = Label(window,text='Enter Username',bd=10,font='italic 14 bold',bg='lightgreen')
    lb3.pack()
    En3 = Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En3.pack()
    lb4 = Label(window,text='Enter Password',bd=10,font='italic 14 bold',bg='lightgreen')
    lb4.pack()
    En4 = Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En4.pack()
    lb5 = Label(window,text='Enter email',bd=10,font='italic 14 bold',bg='lightgreen')
    lb5.pack()
    En5 = Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En5.pack()
    lb6 = Label(window,text='Enter number',bd=10,font='italic 14 bold',bg='lightgreen')
    lb6.pack()
    En6= Entry(window,selectbackground='cornflowerblue',selectforeground='black',bd=10)
    En6.pack()
    Btn4 = Button(window,text='confirm',command=add,cursor='hand2',bd=12)
    Btn4.pack()
    Btn5 = Button(window,text='Show sites',command=Show_site,bd=12,cursor='hand2')
    Btn5.pack()
def Qus():
    global LBL,Btn2,Btn3
    window.configure(bg='lightgreen')
    LBL = Label(window,text='Do you want to add or show site?',fg='red',bg='lightgreen',font='italic 14 bold',cursor='target',bd=size().height//7)
    LBL.pack()
    Btn2 = Button(window,text='Add Site',command=add_Site,fg='green',bg='lightcyan',cursor='hand2',bd=size().height//40)
    Btn2.pack(side=LEFT,padx=size().height//3.5)
    Btn3 = Button(window,text='Show Site',command=Show_Site,fg='green',bg='lightcyan',cursor='hand2',bd=size().height//40)
    Btn3.pack(side=RIGHT,padx=size().height//3.5)
def Checksc():
    if sc1.get() == float(passwh[3]) and sc2.get() == int(passwh[4]) and sc3.get() == int(passwh[5]):
        print('[bold green]User Loged In!!! Good Luck[/bold green]')
        lbl1.destroy()
        sc1.destroy()
        sc2.destroy()
        sc3.destroy()
        Btn1.destroy()
        Qus()
def Number2():
    global sc1,sc2,sc3,lbl1,Btn1
    lbl1 = Label(window,text='Enter the correct answer',bg='tomato',fg='black',font='italic 14 bold')
    lbl1.pack()
    sc1 = Scale(window,from_=0,to=1,orient=HORIZONTAL,resolution=0.1,background='darksalmon',bd=10,cursor='hand2')
    sc1.pack()
    sc2 = Scale(window,from_=0,to=10,orient=HORIZONTAL,background='darksalmon',bd=10,cursor='hand2')
    sc2.pack()    
    sc3 = Scale(window,from_=0,to=100,orient=HORIZONTAL,resolution=1,background='darksalmon',bd=10,cursor='hand2')
    sc3.pack()
    Btn1 = Button(window,text='Confirm',command=Checksc,cursor='hand2',bd=14,bg='darksalmon',fg='black')
    Btn1.pack()
def Number1():
    global Lbln,Lbl,co,label1,label2,label3,c,passwh
    Btn8.destroy()
    c.execute('SELECT * FROM Defultpasswords')
    passwh = (c.fetchone())
    if En1.get() == passwh[0] and En2.get() == passwh[1] and En3.get() == passwh[2]:
        Welcomelbl.destroy()
        Passlbl1.destroy()
        En1.destroy()
        Passlbl2.destroy()
        En2.destroy()
        Passlbl3.destroy()
        En3.destroy()
        Btn1.destroy()
        l.destroy()
        Number2()
def reset():
    msg = messagebox.askyesnocancel("Warning!!!", '''if you clicked yes program will close!!!
for your reset passwords --> Run it again :)
All of your data will delete!!!Are you sure? ''')
    if msg == True:
        con.close()
        remove('Passwordsd.db')
        remove('README.txt')
        window.destroy()
    elif msg == False or msg == None:
        print("[italic red]Resetting Passwords Canceled![/italic red]")
window = Tk()
window.title('Passwords')
print("[italic yellow]Made by MostafaSh5[/italic yellow]")

print('[italic red]---------------------[/italic red]')
print('Running...')
width = size().width-100
height = size().height-150
window.geometry(f'{width}x{height}')
window.title('Passwords')
Welcomelbl = Label(window, text='--Welcome to Passwords--',bg='tomato', fg='black',font='italic 16 bold')
Welcomelbl.pack()
p1 = PhotoImage(file = '102649.png')
window.iconphoto(False,p1)
def welcome():
    global Passlbl1,En1,Passlbl2,En2,Passlbl3,En3,Btn1,l,Btn8
    window.configure(bg='tomato')
    Passlbl1 = Label(window, text='First Password',bg='tomato',fg='black',font='italic 12 bold')
    Passlbl1.pack()
    En1 = Entry(window, show='*',font='italic 14',selectbackground='burlywood',selectforeground='black',bd=10)
    En1.pack()
    Passlbl2 = Label(window, text='Second Password',bg='tomato',fg='black',font='italic 12 bold')
    Passlbl2.pack()
    En2 = Entry(window, show='*',font='italic 14',selectbackground='burlywood',selectforeground='black',bd=10)
    En2.pack()
    Passlbl3 = Label(window, text='Third Password',bg='tomato',fg='black',font='italic 12 bold')
    Passlbl3.pack()
    En3 = Entry(window, show='*',font='italic 14',selectbackground='burlywood',selectforeground='black',bd=10)
    En3.pack()
    l = Label(window,text='',bg='tomato',fg='black',font='italic 12 bold')
    l.pack()
    Btn1 = Button(window,text='Confirm',command=Number1,bg='darksalmon',fg='black',cursor='hand2',bd=12)
    Btn1.pack() 
    Btn8 = Button(window,text='Reset Passwords',command=reset,bg='darksalmon',fg='black',cursor='hand2',bd=12)
    Btn8.pack(side=RIGHT)
asd = listdir()
if len(asd) >= 4:
    welcome()  
else:
    Input()
    with open('README.txt','w') as f:
        f.write('''Remember!!!\ndo not delete any files from this folder!!!\nif you forget your login passwords, all of your data will delete!!!\nhope you enjoy from this program :)''')
        system('attrib +h Passwordsd.db')
window.mainloop()

