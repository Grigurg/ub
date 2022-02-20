import tkinter as tk

win = tk.Tk()
win.title('TK')
win.geometry('500x600+710+240')
# win.geometry('1000000x100000000')
label_1 = tk.Label(win, text='privet',
                   bg='red',
                   fg='white',
                   font=('Arial', 20, 'bold'),
                   padx=20,
                   pady=40,
                   width=10,
                   height=10,
                   anchor='nw',
                   relief=tk.RAISED,
                   bd=10,
                   justify=tk.LEFT
                   )
label_1.pack()

win.mainloop()
