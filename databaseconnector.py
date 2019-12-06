import mysql.connector

def connect(): 
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root' ,
        passwd = '' ,
        
    )
    

    cursor = mydb.cursor()

    
    cursor.execute('create database if not exists assignweek3')
    cursor.execute('use assignweek3')
    cursor.execute('create table if not exists categories(id int auto_increment,category text,brand text,itemDescription longtext,serial_number longtext,price float,stock int,primary key (id));')
    
    cursor.execute('create table if not exists stocks(id int auto_increment,categories_id int,stockin int,stockout int,stock_date Date, primary key (id));')

    return cursor,mydb
 
