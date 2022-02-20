import tkinter as tk
from tkinter import ttk


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {self.x} {self.y}'


def show_day():
    print(combo.get(), combo_int.get())


weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
list_int = [str(i) for i in range(30)]

win = tk.Tk()
win.geometry('300x400+1400+400')
win.title('TK')

combo = ttk.Combobox(win, values=weekDays)
combo_int = ttk.Combobox(win, values=list_int)
ttk.Button(win, text='show_day', command=show_day).pack()
combo.current(0)
combo_int.current(15)
combo.pack()
combo_int.pack()

win.mainloop()
