from tkinter import *
# fd=Tk()
#
# F1=Frame(fd)
# F1.pack()
#
# #creating a button and print an output in the console
#
# def login():
#     print('Logoin Successfully')
#
# def logout():
#     print('Logout Successfully')
#
# Button(F1,text='Login',bg='green',command=login).pack()
# Button(F1,text='Logout',bg='red',command=logout).pack()
#
# fd.mainloop()

#=============================================================

# from tkinter import messagebox
#
# tp=Tk()
# tp.geometry('500x500')
#
# def Hello():
#     mg=messagebox.showinfo('Python','Hello Python')
#
# Button(tp,text='Hello',command=Hello).place(x=100,y=50)
#
# tp.mainloop()

#===========================================================

root=Tk()

f=Frame(root)
f.pack()

def login():
    print('Login Successful')

def logout():
    print('Logout Successful')

Button(f,text='login',command=login).pack()
Button(f,text='logout',command=quit).pack()
root.mainloop()

