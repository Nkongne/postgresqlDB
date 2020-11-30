from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from model import record
import psycopg2


def reg():

    w.title('register a student')
    cr = Canvas(w, bg='blue', height=415, width=700)
    fileName = PhotoImage(file='a6.png')
    background_label = Label(w, image=fileName)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    cr.pack()
    lf=ttk.LabelFrame(w,text='Add a new student')
    ttk.Label(lf,text='First Name:').grid(column=0,row=0,padx=10,pady=10)
    nom=ttk.Entry(lf)
    nom.focus()
    nom.grid(column=1,row=0,padx=10,pady=10)
    ttk.Label(lf, text='Last Name:').grid(column=0, row=1, padx=10, pady=10)
    prenom = ttk.Entry(lf)
    prenom.focus()
    prenom.grid(column=1, row=1, padx=10, pady=10)




    def insertion():
        n=nom.get()
        p=prenom.get()
        datas = [(n),(p)]
        try:
            conn = psycopg2.connect(database="Eleves", user="postgres", password="250592", host="127.0.0.1", port="5050")

        except:
            print('connection to the dabase failed')

        cur = conn.cursor()
        cur.execute('insert into student(nom_student,prenom_student) VALUES (%s,%s)',datas)

        conn.commit()
        conn.close()
    ttk.Button(lf, text='register student', command=insertion).grid(column=0, row=2, padx=10, pady=10)
    ttk.Button(lf, text='Cancel', command='exit').grid(column=1, row=2, padx=10, pady=10)
    lf.place(x=70, y=40)
def create_class():
    w.title('Create a new class')
    cr = Canvas(w, bg='blue', height=415, width=700)
    fileName = PhotoImage(file='a4.png')
    background_label = Label(w, image=fileName)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    cr.pack()
    lf=ttk.LabelFrame(w,text='Add a new class')
    ttk.Label(lf,text='Name of the class:').grid(column=0,row=0,padx=10,pady=10)
    name_class=ttk.Entry(lf)
    name_class.grid(column=1,row=0)
    ttk.Label(lf,text='Number of places:').grid(column=0,row=1,padx=10,pady=10)
    number_plc=ttk.Entry(lf)
    number_plc.grid(column=1,row=1)
    ttk.Button(lf,text='Create the class',command='').grid(column=0,row=2,padx=10,pady=10)
    ttk.Button(lf, text='Cancel', command='exit').grid(column=1, row=2, padx=10, pady=10)
    lf.place(x=70,y=40)


w = Tk()

w.geometry('1250x1000')
w.title('School management')
menu_bar = Menu(w)
w.config(menu=menu_bar)
file_menu = Menu(menu_bar)
file_menu.add_command(label='File')
file_menu.add_separator()
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='quit')
menu_bar.add_cascade(label='File', menu=file_menu)
register_menu = Menu(menu_bar)
register_menu.add_command(label='register new student',command=reg)
register_menu.add_separator()
register_menu.add_command(label='register old student')
register_menu.add_separator()
register_menu.add_command(label='list of students',command=record.l)
register_menu.add_command(label='register a student for GCE O/L')
register_menu.add_separator()
register_menu.add_command(label='register a sutudent for GCE A/L')

menu_bar.add_cascade(label='Registration', menu=register_menu)
classes_menu = Menu(menu_bar)
classes_menu.add_command(label='open a class')
classes_menu.add_separator()
classes_menu.add_command(label='list of classes')
classes_menu.add_separator()
classes_menu.add_command(label='add a class',command=create_class)
menu_bar.add_cascade(label='Classes', menu=classes_menu)
help_menu = Menu(menu_bar)
help_menu.add_command(label='about')
help_menu.add_separator()
help_menu.add_command(label='contact us')
menu_bar.add_cascade(label='Help?', menu=help_menu)
c = Canvas(w, bg='blue', height=966, width=910)
fileName = PhotoImage(file='a8.png')
background_label = Label(w, image=fileName)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()

tabControl = ttk.Notebook(w)
t1 = ttk.Frame(tabControl)
t2 = ttk.Frame(tabControl)
t3 = ttk.Frame(tabControl)
tabControl.add(t1, text='Registration')
tabControl.add(t2, text='Classes')
tabControl.add(t3, text='Exams')
tabControl.place(x=1000,y=30)
ttk.Button(t1,text='Registrer a new student',command=reg).grid(column=0,row=0,padx=15,pady=15)
ttk.Button(t1,text='Registrer an old student').grid(column=0,row=1,padx=15,pady=15)
ttk.Button(t1,text='list of students',command=record.l).grid(column=0,row=2,padx=15,pady=15)
ttk.Button(t2,text='create new class',command=create_class).grid(column=0,row=0,padx=10,pady=10)
ttk.Button(t2,text='list classes').grid(column=0,row=1,padx=10,pady=10)
ttk.Button(t3,text='Registrer for GCE O/L').grid(column=0,row=0,padx=10,pady=10)
ttk.Button(t3,text='Registrer for GCE A/L').grid(column=0,row=1,padx=10,pady=10)
mainloop()

