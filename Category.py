from Database import Database
# from Department import Department


class Category:

    id = None
    category = None
    brand = None
    itemDescription = None
    serial_number = None
    price = None
    stock = None
    

    # department_name = None

    def __init__(self, tuple = None) :
        if(tuple):
            self.id = tuple[0]
            self.category = tuple[1]
            self.brand = tuple[2]
            # self.item_description = Department.find(self.department_id)
            self.itemDescription = tuple[3]
            self.serial_number = tuple[4]
            self.price = tuple[5]
            self.stock = tuple[6]

    def display(self):
        print(f'[{self.id}]- {self.category} -  {self.brand} brand-  {self.itemDescription} -  [{self.serial_number}]  - {self.price} Ks  - {self.stock} Stock')



    def save(self):
        Database._cursor.execute('insert into categories(category,brand,itemDescription,serial_number,price,stock) values (%s,%s,%s,%s,%s,%s)',[self.category,self.brand,self.itemDescription,self.serial_number,self.price,self.stock])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        # self.department = Department.find(self.department_id)
        self.display()

    def update(self):
        Database._cursor.execute('Update categories set stock = %s,category = %s,brand = %s, itemDescription = %s , serial_number = %s , price = %s  where id = %s',[self.stock,self.category,self.brand,self.itemDescription,self.serial_number,self.price,self.id])
        Database._db.commit()
        # self.department = Department.find(self.department_id)
        self.display()

    @staticmethod
    def find(id):
        Database._cursor.execute("Select * from categories where id = %s",[id])
        result = Database._cursor.fetchone()
        return Category(result)

    

    @staticmethod
    def get():
        Database._cursor.execute("select * from categories ")
        category_list = []
        for categoryTuple in Database._cursor.fetchall():
            category = Category(categoryTuple)
            category_list.append(category)

        return category_list