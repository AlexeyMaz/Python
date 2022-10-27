import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('C:/Users/Al Maz/PycharmProjects/Python/Shipping.db')
        return con
    except Error:
        print(Error)


def tables_create(con):
    dispatchers_create(con)
    customers_create(con)
    drivers_create(con)
    cargoes_create(con)
    customers_cargoes_create(con)


def dispatchers_create(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists Dispatchers("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "surname text,"
        "name text,"
        "lastname text,"
        "hireDate text)")
    con.commit()


def customers_create(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists Customers("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "customer_id integer,"
        "dispatcher_id integer,"
        "coworkTime text)")
    con.commit()


def drivers_create(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists Drivers("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "surname text,"
        "name text,"
        "lastname text,"
        "hireDate text)")
    con.commit()


def cargoes_create(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists Cargoes("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "cargo_id integer,"
        "driver_id integer,"
        "destination text,"
        "weight real)")
    con.commit()


def customers_cargoes_create(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE if not exists CustomersCargoes("
        "id integer PRIMARY KEY AUTOINCREMENT,"
        "customer_id integer,"
        "cargo_id integer)")
    con.commit()


def add_table_data(con, tbl_name):
    cursorObj = con.cursor()

    for i in range(int(input("Введите кол-во записей, которые хотите добавить: "))):
        row = input("Введите данные о записи через пробел\n").split()
        fields = ""
        for j in range(len(row)):
            fields += '?, '
        fields = fields[:-2]
        cursorObj.execute(f'INSERT INTO {tbl_name} VALUES(null, {fields})', row)
    con.commit()


def print_table_data(con, tbl_name):
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT * FROM {tbl_name}')
    [print(row) for row in cursorObj.fetchall()]
    cursorObj1 = con.cursor()
    cursorObj1.execute('DELETE from Dispatchers where id = 2')
    con.commit()
    cursorObj.execute(f'SELECT * FROM {tbl_name}')
    [print(row) for row in cursorObj1.fetchall()]


def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]
        print()


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE Cargoes SET destination = "Космонавтов,15" where destination = "Крылатая,6"')
    cursorObj.execute('UPDATE Drivers SET '
                      'surname = "Войсковой", name = "Иван",lastname = "Вениаминович" where id = 4')
    cursorObj.execute('UPDATE Customers SET dispatcher_id = 3 where customer_id = 5')
    con.commit()


def sql_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from Dispatchers where id = 3')
    con.commit()
