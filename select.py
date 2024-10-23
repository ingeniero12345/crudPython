import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=bdprueba;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM personas')

for row in cursor:
    print('row = %r' % (row,))
    print(row)
cnxn.commit()
cnxn.close()