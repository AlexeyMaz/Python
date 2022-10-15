import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('Shipping.db')
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


def delete_table_data(con, tbl_name):
    cursorObj = con.cursor()
    cursorObj.execute(f'DROP TABLE {tbl_name}')


def print_table_data(con, tbl_name):
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT * FROM {tbl_name}')
    [print(row) for row in cursorObj.fetchall()]


connection = sql_connection()
cur = connection.cursor()
cur.execute('DROP TABLE Cargoes')
tables_create(connection)
add_table_data(connection, 'Cargoes')
add_table_data(connection, 'CustomersCargoes')
