import psycopg2
from tkinter import *
from tkinter import ttk


def l():
    w = Tk()
    w.geometry('850x950')
    w.title('List of students')

    conn = psycopg2.connect(database="Eleves", user="postgres", password="250592", host="127.0.0.1", port="5050")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    results = cur.fetchall()
    i = 0
    for a in results:
        for j in range(len(a)):
            e = Entry(w, width=10)
            e.grid(row=i, column=j)
            e.insert(END, a[j])

        i = i + 1