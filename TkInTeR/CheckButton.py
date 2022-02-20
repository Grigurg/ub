import tkinter as tk


def select_all():
    for check in [over_18, uag, u_or_nu]:
        check.select()


def deselect_all():
    for check in [over_18, uag, u_or_nu]:
        check.deselect()


def switch_all():
    for check in [over_18, uag, u_or_nu]:
        check.toggle()


def show():
    print(over_18_value.get())


win = tk.Tk()

over_18_value = tk.StringVar()
over_18_value.set('No')

com_value = tk.IntVar()
win.geometry('300x400+1400+400')
win.title('GUI')

over_18 = tk.Checkbutton(win, text='Вам исполнилось 18 лет?', indicatoron=False, bd=4)
uag = tk.Checkbutton(win, text='Вы гей?', variable=over_18_value,
                     offvalue='No', onvalue='Yes')

u_or_nu = tk.Checkbutton(win, text='Вы или нет?')
over_18.pack()
uag.pack()
u_or_nu.pack()
tk.Button(win, text='select_all', command=select_all).pack()
tk.Button(win, bd=0, activebackground='blue', cursor='', command=deselect_all).pack()
tk.Button(win, text='switch_all', command=switch_all).pack()
tk.Button(win, text='show', command=show).pack()

win.mainloop()
