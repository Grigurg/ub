import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='medal.png')
win.iconphoto(True, photo)
win.config(bg='#FF1493')
win.title('GUI')
win.geometry('500x600+710+240')
win.minsize(300, 400)
win.maxsize(700, 800)
win.resizable(True, False)
win.mainloop()
