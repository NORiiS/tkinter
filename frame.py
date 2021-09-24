from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('cooles Ding')
root.iconbitmap('d:/test.ico')

frame = LabelFrame(root, text='This is my Frame', padx=100, pady=100)
frame.pack(padx=30,pady=30)

button = Button(frame, text="Don't click here",command=root.quit)
button.pack()

root.mainloop()
