# Задание 1. Напишите программу, переводящую градусы по Фаренгейту
# в градусы по Цельсию. Интерфейс работы с программой представлен ниже.

import tkinter


def click():
    inp = entry.get()
    try:
        res = (float(inp) - 32) / (9 / 5)
        label_res.config(text=res)
    except ValueError:
        label_res.config(text="Ошибка, введите число")


window = tkinter.Tk()
window.title("Перевод градусов")
window.config(bg="DarkGray")
label = tkinter.Label(window, text="Температура в Фаренгейтах:", font=('Courier', 16), bg="DarkGray")
label.pack()
entry = tkinter.Entry(window, font=('Courier', 16))
entry.pack(side='top')

label_res = tkinter.Label(window, font=('Courier', 16), bg="DarkGray")
label_res.pack()
button_work = tkinter.Button(window, text='Вычислить', font=('Courier', 16), bg='lime', command=click)
button_work.pack()
button_quit = tkinter.Button(window, text='Выход', font=('Courier', 16), bg='lime', command=window.destroy)
button_quit.pack()

window.mainloop()
