import tkinter as tk
import random


def insert_bg():
    win.config(background=f'#{random.randrange(0x1000000):06x}')


def say_hello():
    print('hello')


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик: {count}'


count = 0
win = tk.Tk()
win.geometry('500x600')
win.title('TK')
win.config(background=f'#{random.randrange(0x1000000):06x}')
btn1 = tk.Button(win, text='Hello',
                 command=insert_bg
                 )
btn2 = tk.Button(win, text='Add new label',
                 command=add_label
                 )
btn3 = tk.Button(win, text='Add new label',
                 command=lambda: tk.Label(win, text='new lambda').pack()
                 )
btn4 = tk.Button(win, text=f'Счетчик: {count}',
                 command=counter,
                 bg='red',
                 activebackground='blue',
                 state=tk.DISABLED
                 )
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
win.mainloop()
