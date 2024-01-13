from tkinter import *

root=Tk()
root.title('Calc')

root.geometry('150x180')

v=IntVar()

l1=Label(root,text="Calculator").pack(side=TOP)

e1=Entry(root,textvariable=v,bd=5).pack()

t1=Frame(root)
t1.pack()
t2=Frame(root)
t2.pack()
t3=Frame(root)
t3.pack()
t4=Frame(root)
t4.pack()

#--------------------------------------------------------------------
x=''

def press(n):
    global x
    x=x+str(n)
    v.set(x)

def equal():
    try:
        global x
        o=str(eval(x))
        v.set(o)
        x=''
    except:
        v.set('SyntaxError')
        x=''

def clear():
    global x
    x=''
    v.set(0)

#--------------------------------------------------------------------

a1=Button(t1,text='1',width=3,command=lambda:press('1')).pack(side=LEFT)
a2=Button(t1,text='2',width=3,command=lambda:press(2)).pack(side=LEFT)
a3=Button(t1,text='3',width=3,command=lambda:press(3)).pack(side=LEFT)
a4=Button(t1,text='+',width=3,command=lambda:press('+')).pack(side=LEFT)

b1=Button(t2,text='4',width=3,command=lambda:press(4)).pack(side=LEFT)
b2=Button(t2,text='5',width=3,command=lambda:press(5)).pack(side=LEFT)
b3=Button(t2,text='6',width=3,command=lambda:press(6)).pack(side=LEFT)
b4=Button(t2,text='-',width=3,command=lambda:press('-')).pack(side=LEFT)

c1=Button(t3,text='7',width=3,command=lambda:press(7)).pack(side=LEFT)
c2=Button(t3,text='8',width=3,command=lambda:press(8)).pack(side=LEFT)
c3=Button(t3,text='9',width=3,command=lambda:press(9)).pack(side=LEFT)
c4=Button(t3,text='*',width=3,command=lambda:press('*')).pack(side=LEFT)

d1=Button(t4,text='C',width=3,command=clear).pack(side=LEFT)
d2=Button(t4,text='0',width=3,command=lambda:press('0')).pack(side=LEFT)
d3=Button(t4,text='=',width=3,command=equal).pack(side=LEFT)
d4=Button(t4,text='/',width=3,command=lambda:press('/')).pack(side=LEFT)

root.mainloop()
