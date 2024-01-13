from tkinter import *

rt=Tk()

l=Listbox(rt)

l.insert(1,'charu') # index number is not important here, it's just a syntax
l.insert(1,'arun')
l.insert(4,'pranav')
l.insert(3,'athira')

l.pack()

rt.mainloop()