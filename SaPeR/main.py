# import tkinter as tk
# from random import shuffle
#
#
# class MyButton(tk.Button):
#
#     def __init__(self, master, x, y, number, *args, **kwargs):
#         super(MyButton, self).__init__(master, bd=1, bg='white', *args, **kwargs)
#         self.x = x
#         self.y = y
#         self.number = number
#         self.is_mine = False
#
#     def __repr__(self):
#         return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'
#
#
# class MineSweeper:
#     window = tk.Tk()
#     window.config(bg='black')
#     ROW = 10
#     COLUMNS = 7
#     MINES = 15
#
#     def __init__(self):
#         self.buttons = []
#         count = 1
#         for i in range(MineSweeper.ROW):
#             temp = []
#             for j in range(MineSweeper.COLUMNS):
#                 btn = MyButton(MineSweeper.window, x=i, y=j, number=count, text=' ')
#                 temp.append(btn)
#                 count += 1
#             self.buttons.append(temp)
#
#     def create_widgets(self):
#         for i in range(MineSweeper.ROW):
#             for j in range(MineSweeper.COLUMNS):
#                 btn = self.buttons[i][j]
#                 btn.grid(row=i, column=j, padx=1, pady=1)
#
#     def start(self):
#         self.create_widgets()
#         self.insert_mines()
#         game.print_buttons()
#         print(self.get_mines_places())
#         MineSweeper.window.mainloop()
#
#     def print_buttons(self):
#         for row_btn in self.buttons:
#             print(row_btn)
#
#     @staticmethod
#     def get_mines_places():
#         indexes = list(range(1, MineSweeper.COLUMNS * MineSweeper.ROW + 1))
#         shuffle(indexes)
#         return indexes[:MineSweeper.MINES]
#
#     def insert_mines(self):
#         index_mines = self.get_mines_places()
#         for row_btn in self.buttons:
#             for btn in row_btn:
#                 if btn.number in index_mines:
#                     btn.is_mine = True
#
#
# game = MineSweeper()
# game.start()
import sys
import os
import pafy


# url = ""
#
# v = pafy.new(url)
# print(v)
# print(v.title)
# print(v.duration)
# print(v.viewcount)

# streams = v.streams
# for item in streams:
#     print(item)

# audio_streams = v.audiostreams
# for item in audio_streams:
#     print(item)

# all_streams = v.allstreams
# for item in all_streams:
#     print(item.quality)
print("Хотите скачать видео или аудио с YouTube? Просто введите URL ниже...")
url = input("Введите URL: ")

print("Что-бы скачать видео введите: 1 | Что-бы скачать аудио введите: 2 ")
choice = input("Введите цифру: ")

def download(choice):
    try:
        v = pafy.new(url)

        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            sys.exit()

        print("Выберите желаемое качество видеоролика передав цифру. Пример: 1: ") if choice == "1" else print("Выберите желаемое качество аудио передав цифру. Пример: 2: ")

        available_streams = {}
        count = 1
        for stream in streams:
            available_streams[count] = stream
            print(f"{count}: {stream}")
            count += 1
        # print(available_streams)

        stream_count = int(input("Введите номер: "))
        d = streams[stream_count - 1].download()

        if choice == "2":
            audio_extension = str(available_streams[stream_count])
            audio_extension = audio_extension.split("@")[0].split(":")[1]

            file_name = v.title
            music_file = f"{file_name}.{audio_extension}"
            base = os.path.splitext(music_file)[0]
            os.rename(music_file, base + ".mp3")

        print("Скачивание успешно завершено!")
    except:
        print("Упс...Проверьте данные")


download(choice)


# if choice == "1":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#
#         print("Выберите желаемое качество видеоролика передав цифру. Пример: 1: ")
#
#         available_streams = {}
#         count = 1
#         video_streams = v.streams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1
#         # print(available_streams)
#
#         stream_count = int(input("Введите номер: "))
#         d = video_streams[stream_count - 1].download()
#         print("Скачивание успешно завершено!")
#     except:
#         print("Упс...Проверьте данные")
# elif choice == "2":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#
#         print("Выберите желаемое качество аудио передав цифру. Пример: 1: ")
#
#         available_streams = {}
#         count = 1
#         video_streams = v.audiostreams
#         for stream in video_streams:
#             available_streams[count] = stream
#             print(f"{count}: {stream}")
#             count += 1
#         # print(available_streams)
#
#         stream_count = int(input("Введите номер: "))
#         d = video_streams[stream_count - 1].download()
#         print("Скачивание успешно завершено!")
#     except:
#         print("Упс...Проверьте данные")
# else:
#     print("Whaaat???")