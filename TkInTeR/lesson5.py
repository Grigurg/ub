import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('empty entry')


def del_entry():
    name.delete(0, tk.END)


def submit():
    print(password.get())


win = tk.Tk()
win.geometry('400x500+1450+400')
win.title('TK')
tk.Label(win, text='Имя').grid(row=0, column=0, sticky='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, sticky='w')

name = tk.Entry(win)
name.grid(row=0, column=1)
password = tk.Entry(win, show='*')
password.grid(row=1, column=1)
tk.Button(win, text='get', command=get_entry) \
    .grid(row=2, column=0, sticky='we')
tk.Button(win, text='del', command=del_entry) \
    .grid(row=2, column=1, sticky='we')
tk.Button(win, text='submit', command=submit) \
    .grid(row=3, column=0, sticky='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello')) \
    .grid(row=2, column=2, sticky='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
