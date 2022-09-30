import random
from tkinter import *


def click_try():
    global k
    var = entry.get()
    if label_rus.cget("text") != "":
        if var.isalpha():
            if k != 0:
                if var == dictionary[rus]:
                    label_text.config(text="Ответ правильный!")
                    k = 2
                else:
                    label_text.config(text="Ответ неправильный! Попыток осталось: " + str(k))
                    k -= 1
            else:
                label_text.config(text="Попыток не осталось! Попытайтесь угадать новое слово.")
                click_rand()
                k = 2
        else:
            label_text.config(text="Ошибка ввода! Введите заново!")
    else:
        label_text.config(text="Вы не зарандомили!")


def click_rand():
    global rus, eng
    rus, eng = random.choice(list(dictionary.items()))
    label_rus.config(text=rus)


window = Tk()
window.title("Угадай слово")
window.config(bg="DarkGray")

dictionary = {"картофель": "potato",
              "кукуруза": "corn",
              "капуста": "cabbage",
              "бобы": "beans",
              "салат": "lettuce",
              "морковь": "carrot",
              "гриб": "mushroom",
              "огурец": "cucumber",
              "лук": "onion",
              "томат": "tomato",
              }

k = 2
rus, eng = "", ""
label_rand = Label(text="Случайное слово -> ", width=30, borderwidth=1, relief="solid", font=('Courier', 16), bg="Cyan")
label_rand.grid(row=0, column=0, pady=10, padx=10)

label_rus = Label(width=30, borderwidth=1, relief="solid", font=('Courier', 16), bg="Cyan")
label_rus.grid(row=0, column=1, pady=10, padx=10)

label_guess = Label(text="Введите догадку -> ", width=30, borderwidth=1, relief="solid",
                    font=('Courier', 16), bg="Cyan")
label_guess.grid(row=3, column=0, pady=10, padx=10)

entry = Entry(width=30, borderwidth=1, relief="solid", font=('Courier', 16))
entry.grid(row=3, column=1, pady=10, padx=10)

button_rand = Button(text="Отобразить случайное слово", width=30, command=click_rand, font=('Courier', 16), bg="lime")
button_rand.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

button_try = Button(text="Попытаться угадать", width=30, command=click_try, font=('Courier', 16), bg="lime")
button_try.grid(row=4, column=0, columnspan=3, pady=10, padx=10)

label_text = Label(width=60, height=3, borderwidth=1, relief="groove", font=('Courier', 16), bg="Cyan")
label_text.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

button_exit = Button(window, text='Выход', command=window.destroy, font=('Courier', 16), bg="lime")
button_exit.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

window.mainloop()
