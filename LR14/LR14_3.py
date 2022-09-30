from tkinter import filedialog
from tkinter import *

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


def save_file_as_txt():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".txt")
    except:
        return
    with open(path + ".txt", 'w') as f:
        f.write(entry.get())
        f.close()


def save_file_as_html():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Html file", "*.html"), ("All files", "*.*"))).name
        window.title('Notepad - ' + path + ".html")
    except:
        return
    with open(path + ".html", 'w') as f:
        f.write(html_template1)
        f.write(entry.get())
        f.write(html_template2)
        f.close()


window = Tk()
window.title('Сохранение текста')
window.config(bg="DarkGray")

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=2)
filemenu.add_command(label="Сохранить как .txt",  command=save_file_as_txt, font=('Courier', 12))
filemenu.add_command(label="Сохранить как .html", command=save_file_as_html, font=('Courier', 12))
filemenu.add_separator()
filemenu.add_command(label="Выход", command=window.destroy, font=('Courier', 12))
menubar.add_cascade(label="Файл", menu=filemenu)

entry = Entry(width=40, borderwidth=2, relief="solid", font=('Courier', 16))
entry.grid(row=0, column=1, pady=10, padx=10)
button_exit = Button(window, text='Выход', command=window.destroy, font=('Courier', 16), bg="lime")
button_exit.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

window.config(menu=menubar)
window.mainloop()
