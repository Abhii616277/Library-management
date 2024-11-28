import time
import mysql.connector as mysql
import random
#from tabulate import tabulate
mydb=mysql.connect(host="localhost",
                   user="root",
                   password="root")
if mydb.is_connected():
   print('databases connected sucessfully')
mycursor=mydb.cursor()
try:
    mycursor.execute("create database lootmart;")
    mycursor.execute("create table product_detail(product_code int primary key,product_name varchar(25) not null,quantity int not null,orignal_amount int(10) not null,weight varchar(5),product_sloat varchar(10),date_of_purched date)")
    time.sleep(5)
    mycursor.execute("create table product_demand(product_code int primary key,product_name varchar(25) not null,quantity int not null,orignal_amount int(10) not null,net_price int not null)")
    print("-------^_~   ^_^  ---------------------------------------")

except:
    print("product_table found")
Limit=4 # variabal for security

def new_item():#1
    print("\n\nenter the following details of a new product:-")
    l=[]
    num=input("enter product_code number:-")
    l.append(num)
    name=input("enter name of product:-")
    l.append(name)
    amo=int(input("enter quantity of new product:-"))
    l.append(amo)
    cp=int(input("enter it cost prise:-"))
    l.append(cp)
    cpi=int(input("enter it net weight:-"))
    l.append(cpi)
    slot=input("enter sloat for product:-")
    l.append(slot)
    rl=(l)
    sql="insert into product_detail ( product_code,product_name, quantity,weight,orignal_amount,product_sloat,date_of_purched) values (%s,%s,%s,%s,%s,%s,now());"
    mycursor.execute(sql,rl)
    if security():
        mydb.commit()
    print("\n\n new record added...")
    op=input("want to run again y/n:-")
    if op in ["y","n"]:
        if op=="y":
            new_item()
            print("\n\n")
        else:
            admin()
    



def remove_product():#2
    print("\n\n")
    id_=int(input("Enter the product_code number which you want to delete:- "))
    rl=(id_)
    sql="Delete from product_detail where id=%s"
    mycursor.execute(sql,rl)
    if security()==True:
        mydb.commit()
    print("data is removed!!")
    op=input("want to run again y/n:-")
    if op in ["y","n"]:
        if op=="y":
            remove_product()
        else:
            admin()

def update_product():#3
     print("\n\n")
     print("Select the option  to modify : ")
     print("1. product_name")
     print("2. quantity")
     print("3.amount")
     print("4.sloat")
     L=[]
     print("\n\n")
     ch=int(input("Enter the choice : "))
     if ch==1:
         sql_="update product_detail set product_name='%s' where product_name='%s' "
     if ch==2:
         sql_="update product_detail set quantity='%s' where quantity='%s' "
     if ch==3:
         sql_="update product_detail set amount='%s' where amount='%s' "
     if ch==4:
         sql_="update product_detail set sloat='%s' where sloat='%s' "
     rl1=input("your old data:-")
     L.append(rl1)
     rl2=input("your new data:-")
     L.append(rl2)
     stud=(L)
     mycursor.execute(sql_,stud)
     mydb.commit()
     print("okaya! data is changed.")
     op=input("want to run again y/n:-")
     if op in ["y","n"]:
         if op=="y":
             update_product()
         else:
            admin()

def inspect_product():#4
    print("\n\n")
    print("Select the search criteria : ")
    print("1. product_code ")
    print("2. product_name")
    print("3. sloat")
    print("4. all")
    print("5. quantity")
    ch=int(input("Enter the choice : "))
    print("\n")
    if ch==1:
        s=int(input("Enter id no : "))
        rl=(s,)
        sql_="select * from product_detail where product_code=%s"
        mycursor.execute(sql_,rl)
    if ch==2:
        s=input("Enter product_name : ")
        rl=(s,)
        sql_="select * from product_detail where product_name=%s"
        mycursor.execute(sql_,rl)
    if ch==3:
        s=int(input("Enter product_sloat : "))
        rl=(s,)
        sql_="select * from product_detail where product_sloat=%s"
        mycursor.execute(sql_,rl)
    if ch==4:
        sql_="select * from product_detail"
        mycursor.execute(sql_)
    if ch==5:
        print("\n")
        print("1.greater than \n2. smaller than \n3.equal to")
        ch=int(input("enter your choice:-"))
        s=int(input("Enter quantity : "))
        if ch==1:
            rl=(s,)
            sql_="select * from product_detail where quantity > %s"
            mycursor.execute(sql_,rl)
        if ch==2:
            rl=(s,)
            sql_="select * from product_detail where quantity < %s"
            mycursor.execute(sql_,rl)
        if ch==3:
            rl=(s,)
            sql_="select * from product_detail where quantity = %s"
            mycursor.execute(sql_,rl)
    res=mycursor.fetchall()
    print("\n,\n")
    print(tabulate(res, headers=["product_code","product_name","quantity ","orignal_amount","weight","product_sloat","date_of_purched"], tablefmt='psql'))
    print("\n\n")
    op=input("want to run again y/n:-")
    if op in ["y","n"]:
        if op=="y":
           inspect_product()
        else:
           admin()

def order():
    print("\n\n")
    """------------------------------------------welcome to order page---------------------------------------------------"""
    print("select the option:- \n1.view old  bill   \n2. create a new order bill \n3. return to main memu")
    print("\n\n")
    op=int(input("enter choice here:-"))
    if op in [1,2,3]:
        if op==1:
            inspect_orderproduct()
        if op==2:
            mycursor.execute("truncate table product_demand")
            new_order()
        if op==3:
            main_menu()
    else:
        print("hey! wrong intrises\t\t try again")
        order()

import time
import mysql.connector as mysql
import random
mydb=mysql.connect(host="localhost",
                   user="root",
                   password="root",
                   database="lootmart")
if mydb.is_connected():
   print('databases connected sucessfully')
mycursor=mydb.cursor()
try:  
    mycursor.execute("create table product_detail(product_code int primary key,product_name varchar(25) not null,quantity int not null,orignal_amount int(10) not null,weight varchar(5),product_sloat varchar(10),date_of_purched date)")
    time.sleep(5)
    mycursor.execute("create table product_demand(product_code int primary key,product_name varchar(25) not null,quantity int not null,orignal_amount int(10) not null,net_price int not null)")
    print("-------^_~   ^_^  ---------------------------------------")

except:
    print("product_table found")
def inspect_orderproduct():#4
    print("\n\n")
    print("Select the search criteria : ")
    print("1. product_code ")
    print("2. product_name")
    print("3. sloat")
    print("4. all")
    print("\n\n")
    ch=int(input("Enter the choice : "))
    print("\n")
    if ch==1:
        s=int(input("Enter id no : "))
        rl=(s,)
        sql_="select * from product_demand where product_code=%s"
        mycursor.execute(sql_,rl)
    elif ch==2:
        s=input("Enter product_name : ")
        rl=(s,)
        sql_="select * from product_demand where product_name=%s"
        mycursor.execute(sql_,rl)
    elif ch==3:
        s=int(input("Enter quantity : "))
        rl=(s,)
        sql_="select * from product_demand where quantity=%s"
        mycursor.execute(sql_,rl)
    elif ch==4:
        sql_="select * from product_demand"
        mycursor.execute(sql_)   
    res=mycursor.fetchall()
    print(res)
    print(tabulate(res, headers=['product_code','product_name', 'quantity','orignal_amount','net_price'], tablefmt='psql'))
    print("\n\n")
    op=input("want to run again y/n:-")
    if op in ["y","n"]:
        if op=="y":
           inspect_orderproduct()
        else:
           order()
def new_order():
    print("\n\n")
        
    print("creating new bill")
    time.sleep(3)
    print("enter the following details of a new product,")
    print("\n\n")
    l=[]
    num=input("enter product_code number:-")
    l.append(num)
    name=input("enter name of product:-")
    l.append(name)
    amo=int(input("enter quantity of new product:-"))
    l.append(amo)
    cp=int(input("enter it cost prise:-"))
    l.append(cp)
    l.append(cp*amo)
    rl=(l)
    sql="insert into product_demand ( product_code,product_name, quantity,orignal_amount,net_price) values (%s,%s,%s,%s,%s);"
    mycursor.execute(sql,rl)
    mydb.commit()
    print("\n\n")
    print("new demand added...")
    op=input("want to add again y/n or view(v):-")
    print("\n\n")
    if op in ["y","v"]:
        if op=="y":
            new_order()
        if op=="v":
            sql_="select  product_code,product_name,quantity,orignal_amount,net_price from product_demand"
            mycursor.execute(sql_)   
            res=mycursor.fetchall()
            print(tabulate(res, headers=['product_code','product_name', 'quantity','orignal_amount','net_price'], tablefmt='psql'))
            mycursor.execute("select sum(net_price) from product_demand")
            print("total price is",mycursor.fetchall()[0][0])
            mycursor.execute("select count(net_price) from product_demand")
            print("total products are", mycursor.fetchall()[0][0])
            order()
    else:
        order()
import mysql.connector as sql
import random
conn=sql.connect(host="localhost",user="root",password="root",database="lootmart")
mycursor=conn.cursor()
print("Database connected")

try:
    mycursor.execute("create table customer_details(bill_no int auto_increment not null,name varchar(30),address varchar(50),phone_no varchar(10),date_ datetime ,primary key(bill_no),total_price int,total_product int)")
    mycursor.execute("create table bill_details(bill_no int,product_id int not null,product_name varchar(10),quantity int(3),price int not null,net_price int not null,foreign key(bill_no) references customer_details(bill_no))")
    print("Table created")
except:
    print("table found")


# insert the customer ditail:
def customer_detail():
    print("\n\n")
    print("detail of customer ")
    p=[]
    cname=input("Enter the name:-")
    p.append(cname)
    address=input("Enter the address:-")
    p.append(address)
    phone=int(input("Enter the contact no:-"))
    p.append(phone)
    Done=(p)
    Q="insert into customer_details(name,address,phone_no,date_)values(%s,%s,%s,now())" 
    mycursor.execute(Q,Done)
    if security()==True:
        conn.commit()
    mycursor.execute(f"select bill_no,name, address,phone_no,date_ from customer_details where phone_no ={phone}")
    res=mycursor.fetchall()
    print(tabulate(res, headers=['bill_no','name', 'address','phone_no','date_'], tablefmt='psql'))
    mycursor.execute(f"select bill_no from customer_details where phone_no ={phone}")
    re=mycursor.fetchall()[0][0]
    print("product detail")
    customer_product_detail(re)

def customer_product_detail (bill):
    print("\n\n")
    p=[]
    p.append(bill)
    productid=input('Enter product_id:-')
    p.append(productid)
    product=input('Enter the name of product:-')
    p.append(product)
    quantity=int(input("Enter the quantity:-"))
    p.append(quantity)
    Amount=int(input("Enter the price:-"))
    p.append(Amount)
    t_amount=Amount*quantity
    p.append(t_amount)
    Done=(p)
    Q="insert into bill_details(bill_no,product_id,product_name,quantity,price,net_price)values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(Q,Done)
    conn.commit()
    print("Inserted")
    print("\n\n")
    op=input("want to add more y/n:-")
    if op=="y":
        customer_product_detail(bill)
    else:
        mycursor.execute(f"select * from bill_details where bill_no={bill}")
        res=mycursor.fetchall()
        print("tabulate"(res, headers=['bill_no','product_id','product_name','quantity','price','net_price'], tablefmt='psql'))
        mycursor.execute(f"select sum(net_price) from bill_details where bill_no={bill}")
        res=mycursor.fetchall()[0][0]
        print("total price is",res)
        mycursor.execute(f"update customer_details set total_price= {res} where bill_no={bill}")
        conn.commit()
        mycursor.execute(f"select count(net_price) from bill_details where bill_no={bill}")
        res=mycursor.fetchall()[0][0]
        print("total products are",res)
        mycursor.execute(f"update customer_details set total_product= {res} where bill_no={bill}")
        conn.commit()
        mycursor.execute(f"select * from customer_details where bill_no ={bill}")
        res=mycursor.fetchall()
        print(tabulate(res, headers=['bill_no','name', 'address','phone_no','date_','total_price','total_product'], tablefmt='psql'))


def view_customer():
    print("\n\n")
    print("Select the search criteria : ")
    print("1. bill_no")
    print("2. name")
    print("3. contact")
    print("4. all")
    print("\n\n")
    ch=int(input("Enter the choice : "))
    print("\n\n")
    if ch==1:
        s=int(input("Enter bill no : "))
        rl=(s,)
        sql_="select * from customer_details where bill_no=%s"
        mycursor.execute(sql_,rl)
    elif ch==2:
        s=input("Enter name : ")
        rl=(s,)
        sql_="select * from customer_details where name=%s"
        mycursor.execute(sql_,rl)
    elif ch==3:
        s=int(input("Enter phone_no : "))
        rl=(s,)
        sql_="select * from customer_details where phone_no=%s"
        mycursor.execute(sql_,rl)
    elif ch==4:
        sql_="select * from customer_details"
        mycursor.execute(sql_)   
    res=mycursor.fetchall()
    print(tabulate(res, headers=['bill_no','name','address' ,'phone_no','date_','net_price'], tablefmt='psql'))
    print("\n\n")
    op=input("want to run again y/n:-")
    if op in ["y","n"]:
        if op=="y":
            view_customer()



def customer():
    print("\n \n\nselect from the following:-\n 1.create bill \n 2.view bill \n 3.demand from customer")
    see=int(input("\n your choice:-"))
    if see in [1,2,3]:
        if see==1:
            customer_detail()
        if see==2:
            view_customer()
        if see==3:
            order()
    else:
        print("plz select from above-----")
        customer()

def admin():
    print("\n\n\nselect your choice:-")
    print("1.add_new_product\n2.update product detail \n3.remove product \n4.inspect product \n5.return to main menue \n6.for order")
    op=int(input("\n\nenter choice here:-"))
    if op in [1,2,3,4,5,6]:
        if op==1:
            print("\n\n")
            new_item()
            print("\n\n")
        if op==2:
            print("\n\n")
            update_product()
            print("\n\n")
        if op==3:
            print("\n\n")
            remove_product()
            print("\n\n")
        if op==4:
            print("\n\n")
            inspect_product()
            print("\n\n")
        if op==5:
            print("\n\n")
            main_menu()
            print("\n\n")
        if op==6:
            print("\n\n")
            order()
            print("\n\n")
    else:
        print("hey! wrong intrises\t\t try again")
        admin()

def security():
    import random
    global limit
    lst=[1,2,3,4,"A","m","C","d","F","g","V","j","p","i","o","s","!","@","#","$","%","&",5,6,7,8,9,"!","@","#","$","%","&"]
    j=["A","m","C","d","F","g","V","j","p","i","o","s","!","@","#","$","%","&"]
    p=[1,2,3,4,"A","m","C","d","F","g","V","j","p","i","o","s","!","@","#","$","%","&",5,6,7,8,9]
    h=["!","@","#","$","A","m","C","d","F","g","V","j","p","i","o","s","%","&",1,2,3,4,5,6,7,8,9]
    q=str(random.choice(lst))
    g=str(random.choice(h))
    z=str(random.choice(j))
    s=str(random.choice(p))
    cap=""
    print("for security plz enter the recaptha")
    cap=q+g+z+s
    print("\n")
    print("\t\t\t\t",cap )
    check=(input("write here:"))
    if cap==check:
        limit=4
        return True
    else:
        limit=limit-1
        if limit<=0:
            exit()
        print("its wrong try again")
        security()
#----------------------------------------first page-------------------
def main_menu():
    print("------------------------------------------------------------------welcome to lootmart-------------------------------------------------")
    print("select the options:-")
    print("1.admin \n2.customer")
    op=int(input("1 or 2 :-"))
    if op in [1,2]:
        if op==1:
            print("------------------------------------------------------------------- ADmIN page:)-------------------------------------------------------------------- ")
            if security()==True:
                admin()
        if op==2:
            if security()==True:
                print(" \n\n\n\n----------------------------------------------lootmart------------------------------------------------------- ")
                print("\n ------------------------------------------------------------customer page---------------------------------------------------")
                customer()
    else:
        print("hey! plz enter above option")
        main_menu()
def hoster():
    user=input("\n \nenter user name :-")
    passwd=input("\nenter password:-")
    if security()==True:
        if user=='root' and passwd=='root':
            print("\nverification done")
            main_menu()
        else:
            print("wrong entries \t try again...")
hoster()

