from tkinter import messagebox
from tkinter import *
import numpy as np
b = []
h = []
j = []
k = []


root = Tk()
root.title(" Solving simultaneous linear equations ")
root.geometry('650x1900')
root.configure(bg='teal')

dg = Label(root, text='enter names of variables in the equations ')
dg.grid(column=0, row=0, columnspan=3, padx=20, pady=20)

gg = Entry(root, width=35, borderwidth=5)
gg.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

dd = Label(root, text="considering the equations in general form, like for a 3 variable linear equation ax+by+cz=d \n"
           "enter the values of co efficient of each variable in order ")
dd.grid(column=0, row=2, columnspan=3, padx=20, pady=30)

e = Entry(root, width=35, borderwidth=5)
e.grid(column=0, row=3,  columnspan=2, padx=20, pady=30)

con = Label(root, text=" similarly enter the constants in order ")
con.grid(column=0, row=5, columnspan=3, padx=20, pady=30)

cons = Entry(root, width=35, borderwidth=5)
cons.grid(column=0, row=6, columnspan=2, padx=20, pady=30)


def enter1():
    f_m = gg.get()
    if f_m not in k:
        if f_m.isalpha():
            k.append(f_m)
        else:
            messagebox.showerror(
                'INVALID ENTRY', 'YOU HAVE ENTERED NOTHING OR A NUMBER. PLEASE INSERT A VARIABLE NAME')
        global ll
        ll = Listbox(root, height=8, width=15)
        for i in k:
            ll.insert(END, i)
        ll.grid(row=1, column=3, columnspan=3, padx=3, pady=3)
        gg.delete(0, END)
    else:
        messagebox.showerror(
            'INVALID ENTRY', 'YOU HAVE ENTERED THE SAME NAME OF VARIABLE AGAIN. PLEASE ENTER PROPER NAME OF VARIABLE')


def enter2():
    f_m = e.get()
    u = f_m.split()
    if f_m.isnumeric() and (len(k) == 0 or len(k) == 1):
        f_n = float(f_m)
        b.append(f_n)
    else:
        try:
            f_n = float(f_m)
        except:
            messagebox.showerror(
                'INVALID ENTRY', 'YOU HAVE ENTERED NOTHING OR A STRING. PLEASE ENTER A NUMBER')
        else:
            b.append(f_n)
    global lb
    lb = Listbox(root, height=9, width=15)
    for i in b:
        lb.insert(END, i)
    lb.grid(row=3, column=3, columnspan=3, padx=3, pady=2)
    e.delete(0, END)


def enter3():
    f_m = cons.get()
    if f_m.isnumeric() and (len(k) == 0 or len(k) == 1):
        f_n = float(f_m)
        h.append(f_n)
    else:
        try:
            f_n = float(f_m)
        except:
            messagebox.showerror(
                'INVALID ENTRY', 'YOU HAVE ENTERED NOTHING OR A STRING. PLEASE ENTER A NUMBER')
        else:
            h.append(f_n)
    global ld
    ld = Listbox(root, height=4)
    for i in h:
        ld.insert(0, i)
    ld.grid(row=6, column=3, columnspan=3)
    cons.delete(0, END)


def clear():
    gg.delete(0, END)
    e.delete(0, END)
    cons.delete(0, END)


def done():
    root.destroy()


btenter1 = Button(root, text='Enter', padx=40, pady=20, command=enter1)
btenter2 = Button(root, text='Enter', padx=40, pady=20, command=enter2)
btenter3 = Button(root, text='Enter', padx=40, pady=20, command=enter3)
btdone = Button(root, text='Done', padx=40, pady=20, command=done)
btclear = Button(root, text='clear', padx=40, pady=20, command=clear)

btenter1.grid(row=1, column=2)
btenter2.grid(row=3, column=2)
btenter3.grid(row=6, column=2)
btdone.grid(row=7, column=2)
btclear.grid(row=7, column=1)

root.mainloop()

n = len(k)
if n == 0:
    messagebox.showerror('INSUFFICIENT ENTRY',
                         'PLEASE ENTER THE REQUIRED INPUT')
    messagebox.showinfo('YOU HAVE ENCOUNTERED A ERROR',
                        'INSUFFICIENT INPUT PROVIDED. PLEASE RUN THE PROGRAM AGAIN')
else:
    if len(b) != n**2:
        messagebox.showerror(
            'INSUFFICIENT ENTRY', 'YOU HAVE NOT ENTERED ALL THE VALUES IN COEFFICIENT MATRIX')
        messagebox.showinfo('YOU HAVE ENCOUNTERED A ERROR',
                            'THE COEFFICIENT MATRIX IS INCOMPLETE. PLEASE RUN THE PROGRAM PROGRAM')
    elif len(h) != n:
        messagebox.showerror(
            'INSUFFICIENT ENTRY', 'YOU HAVE NOT ENTERED ALL THE VALUES IN CONSTANT  MATRIX')
        messagebox.showinfo('YOU HAVE ENCOUNTERED A ERROR',
                            'THE CONSTANT MATRIX IS INCOMPLETE. PLEASE RUN THE PROGRAM AGAIN')
    else:
        z = 0
        c = [[0 for i in range(n)]for j in range(n)]
        for i in range(n):                  # taking the value of matrix A
            for j in range(n):
                c[i][j] = b[z]
                z = z+1
        if h == [0 for i in range(n)]:
            global det
            det = np.linalg.det(c)

            if det == 0:
                root1 = Tk()
                root1.title(" Solving simultaneous linear equations ")
                root1.geometry('100x100')
                p = Label(text='the system has infinitely many  solutions ').grid(
                    row=0, column=0, columnspan=3)
                root1.mainloop()
            else:
                root2 = Tk()
                root2.title(" Solving simultaneous linear equations ")
                root2.geometry('100x100')
                q = Label(text=" the system has trivial solution that is X ").grid(
                    row=0, column=0, columnspan=3)
                root2.mainloop()
        else:
            if np.linalg.det(c) == 0:
                jk = Tk()
                jk.title("Solving simultaneous linear equations ")
                jk.geometry('100x100')
                jk.config(bg='teal')
                w = Label(text='the system of equation given has no solutions').grid(
                    row=0, column=0, columnspan=3)
                jk.mainloop()
            else:
                j = np.linalg.solve(c, h)
                d = list(zip(k, j))
                lol = Tk()
                lol.title(" Solving simultaneous linear equations ")
                lol.geometry('550x500')
                lol.config(bg='teal')
                ha = Label(lol, text=" the solution for the given linear equation is").grid(
                    row=0, column=0, columnspan=3)
                hh = Listbox(lol, width=40)
                for i in range(n):
                    hh.insert(0, d[i])
                hh.grid(row=1, column=0, columnspan=3)
                lol.mainloop()
