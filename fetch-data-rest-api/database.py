import sqlite3

def fetchDBB():
    con = sqlite3.connect('countries.db')
    print("Connexion ouverte")
    return con

def getAllData():
    con = fetchDBB()
    cur = con.cursor()
    cur.execute('SELECT * FROM countries')
    return cur.fetchall()

def createTable():
    con = fetchDBB()
    cur = con.cursor()

    # check if table exists
    query = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='countries'")

    if query.fetchone() is None:
        cur.execute("CREATE TABLE countries (ID INTEGER PRIMARY KEY  AUTOINCREMENT,name VARCHAR(255) NOT NULL,area VARCHAR(255) NOT NULL,image TEXT NULL)")
        con.commit()
        print("Table created")
    else:
        cur.execute("DROP TABLE countries")
        con.commit()
        print("Table dropped")
        createTable()

def insertData(Liste: list):
    con = fetchDBB()
    cur = con.cursor()
    createTable()
    cur.executemany("INSERT INTO countries VALUES (null,?,?,?)", Liste)
    con.commit()
    print("Insertion terminee!")

