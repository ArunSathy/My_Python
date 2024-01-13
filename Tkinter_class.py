from tkinter import *

# tr=Tk()
#
# class Lp:
#     def __init__(self,rt1):
#         fr=Frame(rt1)
#         fr.pack()
#         Button(fr,text='START',command=self.start).pack()
#         Button(fr,text='STOP',command=fr.quit).pack()
#
#     def start(self):
#         print('Start Coding')
#
# obj=Lp(tr)
#
# tr.mainloop()

#=====================================================================

# tr=Tk()
#
# class Lp:
#     def __init__(self):
#         Button(text='START',command=self.start).pack()
#         Button(text='STOP',command=quit).pack()
#
#     def start(self):
#         print('Start Coding')
#
# obj=Lp()
#
# tr.mainloop()

#===============================================================

root=Tk()

class code:
    def __init__(self):
        f=Frame(root)
        f.pack()
        Button(f,text='Hello',command=self.print).pack()
        Button(f,text='exit',command=quit).pack()

    def print(self):
        print('Hello')

ob=code()

root.mainloop()

#----------------- or else -------------------------------

# root=Tk()
#
# class code:
#     def __init__(self,one):
#         f=Frame(one)
#         f.pack()
#         Button(f,text='Hello',command=self.print).pack()
#         Button(f,text='exit',command=quit).pack()
#
#     def print(self):
#         print('Hello')
#
# ob=code(root)
#
# root.mainloop()