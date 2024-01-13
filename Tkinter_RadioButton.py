from tkinter import *

def sel():
    selection = "You selected the option " + str(v.get())
    lab.config(text = selection)
rt=Tk()
v=IntVar()

r1=Radiobutton(rt,text='Option 1',variable=v,value=1,command=sel).pack()
r2=Radiobutton(rt,text='Option 2',variable=v,value=2,command=sel).pack()
r3=Radiobutton(rt,text='Option 3',variable=v,value=3,command=sel).pack()

lab=Label(rt)
lab.pack()

rt.mainloop()

#===========================================================

# def sel():
#     selection = "You selected the option " + str(var.get())
#     label.config(text = selection)
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
# command=sel)
# R1.pack( anchor = W )
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
# command=sel)
# R2.pack( anchor = W )
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
# command=sel)
# R3.pack( anchor = W)
# label = Label(root)
# label.pack()
# root.mainloop()