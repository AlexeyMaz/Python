#!/usr/bin/env python3
import cgi
from LR15 import *

form = cgi.FieldStorage()
if form.getvalue('table_list') is not None:  # запись в файл
    tbl_name = form.getvalue('table_list')
    file = open("cgi-bin/table.txt", "w")
    file.write(form.getvalue('table_list'))
else:
    inp = open("cgi-bin/table.txt", "r")
    tbl_name = inp.read()
    inp.close()

print("Content-type: text/html\n")
print(f"""<!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Работа с таблицей {tbl_name}</title>
            </head>
            <body>
                <form action="/cgi-bin/form.py">
                    <h3>Что Вы хотите сделать с таблицей {tbl_name}?</h3>
                    <p><select name="act_list">
                        <option></option>
                        <option>Добавить запись</option>
                        <option>Обновить запись</option>
                        <option>Удалить запись</option>
                        <option>Вывести все записи</option>
                    </select></p>
                    <p><input type="submit" value="Отправить"></p>
                </form>""")

# if form.getvalue('act_list') is not None:
connection = sql_connection()
table_str = '<table><tr>\n'
act = form.getvalue('act_list')
if act is not None:
    if act == 'Добавить запись':
        print("""<form action="/cgi-bin/form.py">
                Введите данные новой записи через пробел: <input type="text" name="new_tran">
                <p><input type="submit" value="Отправить"></p>
                    <style>
                    input[type="text"] 
                    {
                        width: 300px;
                    }
                    </style>
               </form>
        """)
        cursorObj = connection.cursor()
        row = form.getfirst("new_tran").split()
        print(f"""{row}""")
        fields = ""
        for j in range(len(row)):
            fields += '?, '
        fields = fields[:-2]
        cursorObj.execute(f'INSERT INTO {tbl_name} VALUES(null, {fields})', row)
        connection.commit()
        # Прав Левонбаум Антонович 2015-04-19
        print(f"""{row}
                     """)
    if act == 'Вывести все записи':
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
        headers = [description[0] for description in cursor.description]
        for i in range(len(headers)):
            table_str += '<th>' + headers[i] + '</th>'
        table_str += '</tr>\n\n'

        for row in cursor.fetchall():
            table_str += '<tr>\n'
            tmp = list(row)
            for i in range(len(tmp)):
                table_str += '<td>' + str(tmp[i]) + '</td>'
            table_str += '</tr>\n'

        table_str += """<style>table {
           border: 1px solid grey;
           border-collapse: collapse;
            }
           td {
           border: 1px solid grey;
           text-align: center;
            }
            th {
           border: 1px solid grey;
           min-width:160px;
            }
        </table>
        </style>"""
        print(table_str)
        print('</table>')
print("""</body>
     </html>""")
