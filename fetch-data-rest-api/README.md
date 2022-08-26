# REST API DATA COLLECTION
Try getting data in REST API using python and insert data in database
choosen database here sqlite database.

# Dependencies
- [requests](https://pypi.org/project/requests/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)

# Structures
- *countries.db* represent current database for countries (It is a file)
- *database.py*  python module for communicate with database
- *main.py*      entry for programm excute it after run all installations
- *queries_helpers* helpers simple file with creation database request
- *requirements* contains all dependencies for applications
- *launch.bat*   bash script written for windows plateform . He run application .

# Getting starting
-  Creation de l'environement virtuel
```
    python -m venv env  
```
-  Lancer l'environement virtuel
```
    .\env\Scripts\activate   
```
-  Installation des dependences
```
    pip install -m requirements.txt
```
-  Lancer l'application
```
    ./launch.bat
```

# Tools
Pour visualiser les données de la base de données, vous devez installer ces outils.
- [SQLite Viewer (for vscode)](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)
- [DB browser Sqlite](https://sqlitebrowser.org/dl/)



