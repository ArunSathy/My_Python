from tkinter import *

rt=Tk()

sb=Scrollbar(rt)
sb.pack(side=RIGHT,fill=Y)

lt=Listbox(rt,yscrollcommand=sb.set)
for line in range(100):
    lt.insert(END,'the lines'+str(line))

lt.pack( side = LEFT, fill = BOTH )
sb.config(command=lt.yview)

rt.mainloop()

#=============================================

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill=Y )
# mylist = Listbox(root, yscrollcommand = scrollbar.set )
# for line in range(100):
#     mylist.insert(END, "This is line number " + str(line))
# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
# mainloop()