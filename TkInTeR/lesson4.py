import tkinter as tk

win = tk.Tk()
win.geometry('400x500+1450+400')
win.title('TK')

# btn1 = tk.Button(win, text='Hello1')
# btn2 = tk.Button(win, text='Hello2')
# btn3 = tk.Button(win, text='Hello3')
# btn4 = tk.Button(win, text='Helloword')
# btn5 = tk.Button(win, text='Hello5')
# btn6 = tk.Button(win, text='Hello6')
# btn7 = tk.Button(win, text='Hello7')
# btn8 = tk.Button(win, text='Hello8')
#
# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, sticky='w')
# btn3.grid(row=1, column=0)
# btn4.grid(row=1, column=1)
# btn5.grid(row=2, column=0)
# btn6.grid(row=2, column=1, sticky='e')
# btn7.grid(row=3, column=0, columnspan=2, sticky='we')
# btn8.grid(row=0, column=3, rowspan=4, sticky='ns')

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column=j, sticky='we')

win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
