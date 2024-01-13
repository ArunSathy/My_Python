from tkinter import *

rt=Tk()

check1=IntVar()
check2=IntVar()
check3=IntVar()

one=Checkbutton(rt,text='first',variable=check1,onvalue=1,offvalue=0,height=5,width=15).pack()
two=Checkbutton(rt,text='second',variable=check2,onvalue=1,offvalue=0,height=5,width=30).pack()
three=Checkbutton(rt,text='three',variable=check3,onvalue=1,offvalue=0,height=5,width=20).pack()


rt.mainloop()