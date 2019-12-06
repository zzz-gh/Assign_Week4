from Category import Category
from Stock import Stock



# def setup():
#     cursor.execute('create database if not exists assignweek3')
#     cursor.execute('use assignweek3')
#     cursor.execute('create table if not exists categories(id int auto_increment,category text,brand text,itemDescription longtext,serial_number longtext,price float,stock int,primary key (id));')
    
#     cursor.execute('create table if not exists stocks(id int auto_increment,categories_id int,stockin int,stockout int,stock_date Date, primary key (id));')

#step1 build table categories and stock
#categories(id int auto_increment,category text,brand text,
#           itemDescription longtext,serial_number longtext,
#           price float,stock int,primary key (id))
#stocks(id int auto_increment,categories_id int,stockin int,
#           stockout int,stock_date Date, primary key (id))
#step2 addNewCategories() for adding new categories
#step3 displayAllCategories()
#step4 addNewStocks() for get in and get out categories from categories table
#step5 displayStocks()
#step6 getCategoriesId()
#step7 availabe_netStock() to calculate the net stock after addNewStock()
#step8 displayMenu()

def addNewCategories():

    category = Category()
    category.category = input("Please enter the type of category item(laptop,phone,accessories etc..) :")
    category.brand = input('Please enter the type of brand(Apple,Samsung,Xiaomi etc..)')
    category.itemDescription = input('Enter item description for your item (eg. macbook 13inches,Mi9T,Remaxspeaker)')
    category.serial_number = input('Enter serial number for your item(eg,ZT79LV1379M)')
    category.price = input('Enter the price of your item:')
    category.stock = input('Enter the available stock.')
    
    category.save()
    


def displayAllCategories():

    category_list = Category.get()
    
    for category in category_list:
        category.display()
   
    



def addNewStock():

    stock = Stock()
    print('Categories.......')
    displayAllCategories()
    stock.categories_id = input("Enter categories id that you want to stock in stock out,choose from above:") 
    stock.stockin = input('Enter import number of your stock_item to your shop:')
    stock.stockout = input('Enter export number of your stock_item from yout shop:')
    stock.stock_date = input('Enter the date(YY/MM/DD):')
    stock.save()

def displayStocks():
    stocks = Stock.get()
    for stk in stocks:
        stk.display()
    




# def getCategoriesId(id):
#     cursor.execute("select * from categories where id = %s", [id])
#     category = cursor.fetchone()
#     return category




def availabe_netStock():
    print('Preparing to calculate net stock:')
    print('Catergories.........')
    displayAllCategories()
    print('Stocks..............')
    displayStocks()
    category_id = input('Please select the category:')
    cid = Category.find(category_id)
    # cate = getCategoriesId(category_id)
    
    
    user_choice = input(f'Are you sure want to calculatae net amount of stock  net ammount: y/n:')
    if(user_choice == 'y'):
        # increaseAmount = int(input('How do you want to increse :'))
        
        
        # cid = int(category_id)
        stock_id = int(input('Enter the stock_id for the category that you input above:'))
        sid = Stock.find(stock_id)
        # cursor.execute('SELECT * FROM assignweek3.stocks where categories_id = %s and id = %s;',[cid,s])
        # for sii in cursor.fetchall():
            # sin = sid.stockin
            # sout = sid.stockout
        cid.stock = (int(sid.stockin) + int(cid.stock)) - int(sid.stockout)
        print('This is your update')
        cid.update()
        # mydb.commit()
        print('Categories.....')
        displayAllCategories()


def displayMenu():
    try:
        selected_option= input(
            f'Please select the action you want to do\n'
            f'[1] Add new categories \n'
            f'[2] Add new stocks \n'
            f'[3] View All Categories \n'
            f'[4] View All Stocks \n'
            f'[5] Calculate Net Amount \n'

        )

        if(selected_option == '1'):
            addNewCategories()
        elif(selected_option == '2'):
            addNewStock()
        elif(selected_option == '3'):
            displayAllCategories()
        elif(selected_option == '4'):
            displayStocks()
        elif(selected_option == '5'):
            availabe_netStock()
        choose = input('Do you want to go back to menu: y/n \n')
        if (choose == 'y'):
            displayMenu()
        else:
            print('Bye Bye')
        
    except KeyboardInterrupt:
        print('Bye Bye')




# setup()
displayMenu()
# availabe_netStock()

# addNewCategories()
# displayAllCategories()
# addNewStock()
# displayStocks()

