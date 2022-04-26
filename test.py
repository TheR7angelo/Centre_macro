import pyodbc

connetor = 'Driver={SQL Server};' \
           'Server=BORDEAUX04\sqlexpress;' \
           'Database=Access;' \
           'Trusted_Connection=yes;'

with pyodbc.connect(connetor) as conn:
    cursor = conn.cursor()
    cursor.execute('''SELECT *
                    FROM "Pers 100 Personnel"
                    ORDER BY "Nom"
                    ''')
    rows = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

liste = [dict(zip(cols, row)) for row in rows]
print("hey")
