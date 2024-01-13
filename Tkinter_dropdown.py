from tkinter import *
# rt=Tk()
#
# def com():
#     print('coding')
#
# mymenu=Menu(rt)
# rt.config(menu=mymenu)
#
# sub1=Menu(mymenu)
#
# mymenu.add_cascade(label='file',menu=sub1)
# sub1.add_command(label='new',command=com)
# sub1.add_cascade(label='save',command=com)
# sub1.add_separator()
# sub1.add_cascade(label='exit',command=quit)
#
# sub2=Menu(mymenu)
#
# mymenu.add_cascade(label='edit',menu=sub2)
# sub2.add_command(label='alter',command=com)
# sub2.add_separator()
# sub2.add_command(label='undo',command=com)
# sub2.add_command(label='redo',command=com)
#
# rt.mainloop()

#========================================================

root=Tk()

menu=Menu(root)
root.config(menu=menu)

def code():
    print('it\'s working')

menu1=Menu(menu)

menu.add_cascade(label="File",menu=menu1)
menu1.add_command(label='New',command=code)
menu1.add_command(label="Save",command=code)
menu1.add_separator()
menu1.add_command(label='Exit',command=quit)

menu2=Menu(menu)

menu.add_cascade(label='Edit',menu=menu2)
menu2.add_command(label='Alter',command=code)
menu2.add_separator()
menu2.add_command(label='Options',command=code)


root.mainloop()

