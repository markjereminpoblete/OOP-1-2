import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\poblete\Documents\Database1.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('''INSERT INTO Table1 (ID, FullName, Age, Address, Birthdate, SemGrade)
                        VALUES(11, 'Mark Jeremin Poblete', 18, 'Cavite', 'June 4, 2003', 90)
                        ''')
    database.commit()
    print("Data is Added")


except pyodbc.Error:
    print("Error in Connection")
