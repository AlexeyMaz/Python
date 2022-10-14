import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)


# def tables_create(con):
#     dispatchers_create(con)
#     customers_create(con)
#     drivers_create(con)
#     cargoes_create(con)
#     customers_cargoes_create(con)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE if not exists employees(id integer PRIMARY KEY, name text, salary\
                    real, department\
                    text, position\
                    text, hireDate\
                    text)")
    con.commit()


def sql_faculties(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Faculties("
        "FacultyID integer PRIMARY KEY,"
        "FacultyName text,"
        "Descript text)")

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(1, 'ФКТиПМ', 'Факультет питона')"
    )
    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(2, 'РГФ', 'Гуманитарии')"
    )

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(3, 'Журфак', 'Бесполезнарии')"
    )
    con.commit()


def sql_specialities(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Specialties("
        "SpecialtyID integer PRIMARY KEY,"
        "FacultyID integer,"

        "SpecialtyName text,"
        "SpecialtyCode integer,"
        "Descript text)")
    con.commit()


def sql_sets(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Sets(SetID integer PRIMARY KEY,"
        "SpecialtyID integer,"

        "SetName text,"
        "SetYear text)")
    con.commit()


def sql_teach_form(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE TeachForm("
        "TeachFormID integer PRIMARY KEY,"
        "Descript text)")
    con.commit()


def sql_groups(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Groups("
        "GroupID integer PRIMARY KEY,"

        "TeachFormID integer,"

        "GroupName text)")
    con.commit()


def sql_students(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Students("
        "StudentID integer PRIMARY KEY,"
        "GroupID integer,"

        "Surname text,"
        "Firstname text,"
        "Lastname text,"
        "Phone text)")
    con.commit()


def add_table_data(con, tbl_name):
    cursorObj = con.cursor()
    # andrew 3 dskfksd dsfkks 03.12
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
    # con.commit()


def print_table_data(con, tbl_name):
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT * FROM {tbl_name}')
    [print(row) for row in cursorObj.fetchall()]


connection = sql_connection()
sql_table(connection)
# delete_table_data(connection, 'employees')
add_table_data(connection, 'employees')
