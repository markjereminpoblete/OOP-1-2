import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\poblete\Documents\Database1.accdb;')
    print("Database is Connected")

    user_id=11
    database = connect.cursor()
    database.execute('delete from Table1 where id=?', (user_id))
    database.commit()
    print("Data is Deleted")


except pyodbc.Error:
    print("Error in Connection")