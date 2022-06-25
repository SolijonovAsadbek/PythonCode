from tkinter import *
import sqlite3

with sqlite3.connect("database.db") as db:
    cur = db.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users 
(id integer PRIMARY KEY AUTOINCREMENT, 
username text NOT NULL,
password text NOT NULL); """)


def add_new_user():
    newUserName = username.get()
    newPassword = password.get()

    cur.execute("SELECT COUNT(*) from users WHERE username = '" + newUserName + "' ")
    result = cur.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Username already exists"
    else:
        cur.execute("INSERT INTO users(username, password) VALUES (?,?)", (newUserName, newPassword))
        db.commit()
        error["text"] = "Add newUser"


window = Tk()
window.geometry("400x600")


def new_search():
    new_search_ = search.get()
    result = cur.execute("SELECT * FROM users WHERE id=?", (new_search_,)).fetchall()

    class Table:

        def __init__(self, root):

            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='blue',
                                   font=('Arial', 16, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
                    print(i, j)

    # take the data
    lst = result
    print(lst)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    t = Table(window)
    # label3 = Label(bg='lightgreen',text=f"id: {result[0]}\nname: {result[1]}\npassword: {result[2]}")
    # label3.place(x=30, y=180)
    # print(result, type(result))


error = Message(text="", width=160)

error.place(x=30, y=10)
error.config(padx=0)
label1 = Label(text=" Enter username: ")

label1.place(x=30, y=40)
label1.config(bg='lightgreen', padx=0)
username = Entry()
username.place(x=150, y=40, width=200, height=25)
search = Entry()

search.place(x=150, y=120, width=200, height=25)
label2 = Label(text=" Enter password: ")

label2.place(x=30, y=80)
label2.config(bg='lightgreen', padx=0)
password = Entry()
password.place(x=150, y=80, width=200, height=25)
button = Button(text="Add", command=add_new_user)

button1 = Button(text="SearchID", command=new_search)
button1.place(x=250, y=150, width=75, height=35)

label3 = Label(text=" Search: ")
label3.place(x=30, y=120)
label3.config(bg='lightgreen', padx=0)
button.place(x=150, y=150, width=75, height=35)

window.mainloop()
