import sqlite3


conn = sqlite3.connect("customer.db")
cur = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS customers " \
        "(id integer PRIMARY KEY AUTOINCREMENT, " \
        "first_name text," \
        "last_name text," \
        "age integer," \
        "address text" \
        ");"

query = "INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('Micah', 'jones', 23, 'Richer Ave');"
query2 ="INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('Sarah', 'Phillips', 29, 'Jackson Ave');"
query3 = "INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('Stewart', 'Hansen', 32, 'January Dr');"
query4 = "INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('SunHee', 'VanDerWeg', 25, 'Kentucky lane');"
query5 =  "INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('Malia', 'AlHausa', 23, '4392 Honolulu Way');"
query6 =  "INSERT INTO customers (first_name, last_name, age, address)" \
        "Values ('Roberto', 'Garcia', 18, 'Stanley Rd');"


cur.execute(query)
cur.execute(query2)
cur.execute(query3)
cur.execute(query4)
cur.execute(query5)
cur.execute(query6)
conn.commit()
conn.close()
