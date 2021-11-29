import sqlite3 as sql
import pandas as pd


class DataBase:


    def __init__(self):
        self.conn=sql.connect("DATA")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY,name text,quantity integer, price real)")
        #self.cur.execute("DELETE * FROM stock")
        self.conn.commit()
    

    def Add_object_to_base(self,nam,num,price):
        self.cur.execute("INSERT INTO stock VALUES (NULL,?,?,?)",(nam,num,price))
        self.conn.commit()


    def Remove_object_from_base(self,id):
        
        
        self.cur.execute("DELETE FROM stock WHERE id=?",(id,))
        self.conn.commit()

    def View_all(self):
       
            self.cur.execute("SELECT * FROM stock")
            rows=self.cur.fetchall()
            return rows
        
    def Remove_all_content(self):
        self.cur.execute("DELETE FROM stock")
        self.conn.commit()



    def Check_if_database_is_empty(self):

        self.cur.execute("Select id FROM stock where quantity is NULL;")
        data = self.cur.fetchone()
        return data
    
    def Writing_into_csv_file(self):
        with open("./Data.csv","w+") as file:
            for row in self.cur.execute("SELECT * FROM stock"):
                file.write(row)

