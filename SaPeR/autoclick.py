import tkinter as tk
import pyautogui, time

win = tk.Tk()
win.geometry('300x400+1400+400')

pixel = tk.PhotoImage(width=1, height=1)

win.config(bg='black')
count = 0
time.sleep(2)


def counter():
    global count
    count += 1
    btn.config(text=count)


btn = tk.Button(win,
                text='count',
                image=pixel,
                compound=tk.CENTER,
                command=counter,
                )
btn.configure(image=pixel,
              width=40,
              height=40)
x, y = btn.size()
print(x, y)
btn.place(x=20, y=20)

win.mainloop()
# import tkinter as tk
# import tkinter.font as tkFont
#
# app = tk.Tk()
# app.geometry("600x500")
#
#
# def decreaseSize():
#     buttonExample1.configure(height=100,
#                              width=100)
#
#
# def increaseSize():
#     buttonExample2.configure(height=400,
#                              width=400)
#
#
# pixelVirtual = tk.PhotoImage(width=1, height=1)
#
# buttonExample1 = tk.Button(app,
#                            text="Decrease Size",
#                            image=pixelVirtual,
#                            width=200,
#                            height=200,
#                            command=decreaseSize)
# buttonExample2 = tk.Button(app,
#                            text="Increase Size",
#                            image=pixelVirtual,
#                            width=200,
#                            height=200,
#                            compound=tk.LEFT,
#                            command=increaseSize)
#
# buttonExample1.pack(side=tk.LEFT)
# buttonExample2.pack(side=tk.RIGHT)
# app.mainloop()
