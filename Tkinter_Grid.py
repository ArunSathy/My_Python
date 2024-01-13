from tkinter import *
# hg=Tk()
#
# Label(hg,text='username').grid(row=0,column=0)
# Label(hg,text='password').grid(row=1,column=0)
#
# Entry(hg).grid(row=0,column=1)
# Entry(hg).grid(row=1,column=1)
#
# hg.mainloop()

#=====================================================

rt=Tk()

Label(rt,text='username',bg='white').grid(row=0,column=0)
Label(rt,text='password',bg='white').grid(row=1,column=0)

Entry(rt).grid(row=0,column=1)
Entry(rt).grid(row=1,column=1)


rt.mainloop()