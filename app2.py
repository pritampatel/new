import sqlite3
from models.item import ItemModel
def insert(v1,v2):
        connection= sqlite3.connect('data.db')
        cursor= connection.cursor()

        query={"INSERT INTO items VALUES (?,?)"}
        cursor.execute(query,(v1,v2))

        connection.commit()
        connection.close()
        return {"message":"success"}

v=insert("test1",10)
print(v)