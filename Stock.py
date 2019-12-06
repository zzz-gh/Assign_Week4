from Database import Database
from Category import Category

class Stock():
    id = None
    categories_id = None
    stockin = None
    stockout = None
    stock_date = None

    category_name = None

    def __init__(self,tuple_data = None):
        if(tuple_data):
            self.id = tuple_data[0]
            self.categories_id = tuple_data[1]
            self.category = Category.find(self.categories_id)
            self.stockin = tuple_data[2]
            self.stockout = tuple_data[3]
            self.stock_date = tuple_data[4]

        

    def save(self):
        Database._cursor.execute('insert into stocks(categories_id,stockin,stockout,stock_date) values (%s,%s,%s,%s)',[self.categories_id,self.stockin,self.stockout,self.stock_date])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        self.category = Category.find(self.categories_id)
        self.display()

    def display(self):
        
        print(f'[{self.id}] - categoryid [{self.categories_id}]  - {self.stockin} Instock   - {self.stockout} Stockout  - {self.stock_date} date')


    @staticmethod
    def find(id):
        Database._cursor.execute("Select * from stocks where id = %s",[id])
        result = Database._cursor.fetchone()
        return Stock(result)

    @staticmethod
    def get():
        Database._cursor.execute("select * from stocks ")
        stk_list = []
        for stkTuple in Database._cursor.fetchall():
            stk = Stock(stkTuple)
            stk_list.append(stk)

        return stk_list