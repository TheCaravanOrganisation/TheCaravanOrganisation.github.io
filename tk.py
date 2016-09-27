from Tkinter import *

panel = Tk()
pann = Tk
labell= Label(panel, text = "kill all humans")
def meme():
	p2 = Tk()
	label2 = Label(p2, text = "ISHYGDDT")

labell.pack()
panel.minsize(500,500)
butt = Button(panel, text="pressme", command=meme())
butt.pack()
panel.mainloop()