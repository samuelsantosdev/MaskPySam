from Tkinter import *
from maskpysam import maskpysam

def callback(event):
    value = event.widget.get() + event.char
    value = maskpysam.strmask(value, "(##) ###.###-###.###")
    event.widget.delete( 0 , END )
    event.widget.insert( 0 , value )

root = Tk()
et = Entry(root)
et.bind( '<Key>', callback )
et.pack()
et.focus_force()

root.mainloop()


