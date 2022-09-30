from tkinter import filedialog
from tkinter import *
from math import pi

html_template1 = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Текст в формате html</h2>
<p>
"""
html_template2 = """.</p>
</body>
</html>
"""

def click():
    if entry.get().isdigit():
        inp = float(entry.get())
        try:
            res = (4 * pi * inp ** 3) / 3
            label_answer.config(text=res)
        except:
            label_answer.config(text="Ошибка, введите число!")
    else:
        label_answer.config(text="Ошибка, введите число!")


def savefileastxt():
    var = str(label_answer.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
            window.title('Результат сохранен')
        except:
            return
        with open(path + ".txt", 'w') as f:
            f.write("Ответ для радиуса длины " + str(entry.get()) + " = " + str(label_answer.cget("text")))
            f.close()
    else:
        pass


def savefileashtml():
    var = str(label_answer.cget("text"))
    if var != "":
        try:
            path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
            window.title('Результат сохранен')
        except:
            return
        with open(path + ".html", 'w') as f:
            f.write(html_template1)
            f.write("Ответ для радиуса длины " + str(entry.get()) + " = " + str(label_answer.cget("text")))
            f.write(html_template2)
            f.close()
    else:
        pass


window = Tk()
window.title('Сохранение текста')
window.config(bg="DarkGray")

label_inp = Label(text="Введите радиус ->", width=30, borderwidth=1, relief="solid", font=('Courier', 16), bg="Cyan")
label_inp.grid(row=0, column=0, pady=10, padx=10)

label_ans = Label(text="Результат вычислений ->", width=30, borderwidth=1, relief="solid",
                  font=('Courier', 16), bg="Cyan")
label_ans.grid(row=3, column=0, pady=10, padx=10)

label_answer = Label(width=30, borderwidth=1, relief="solid", font=('Courier', 16), bg="Cyan")
label_answer.grid(row=3, column=1, pady=10, padx=10)

entry = Entry(width=30, borderwidth=1, relief="solid", font=('Courier', 16))
entry.grid(row=0, column=1, pady=10, padx=10)

button_calc = Button(text="Вычислить", width=20, command=click, font=('Courier', 16), bg="lime")
button_calc.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

button_txt_save = Button(text="Сохранить в .txt", width=20, command=savefileastxt, font=('Courier', 16), bg="lime")
button_txt_save.grid(row=4, column=0, columnspan=1, pady=10, padx=10)

button_html_save = Button(text="Сохранить в .html", width=20, command=savefileashtml, font=('Courier', 16), bg="lime")
button_html_save.grid(row=4, column=1, columnspan=1, pady=10, padx=10)

button_exit = Button(window, text='Выход', width=20, command=window.destroy, font=('Courier', 16), bg="lime")
button_exit.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

window.mainloop()
