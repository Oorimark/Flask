# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from sys import modules
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


# using flask_sqlalchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:markoori@localhost/tasteclandb"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
# # secret key!
# app.config['SECRET_KEY'] = "secret"
# initializing the db...
# db = SQLAlchemy(app)

#connecting to the mysql database
db = mysql.connector.connect(
    host= "mysql-71846-0.cloudclusters.net",
    port = 19414,
    user= "admin",
    passwd = "LwqrO6YF",
    database = "Tasteclandb"
)

my_cursor = db.cursor()

class Mysql_db():        
    def Register_db(self,name,email,passwd):
        my_cursor.execute(f"INSERT INTO users (`NAME`,`EMAIL`,`PASSWORD`) VALUES ('{name}','{email}','{passwd}')")
        db.commit()
        
        
    def Contact_db(self,name,email,msg):
        my_cursor.execute(f"INSERT INTO contact (`NAME`,`EMAIL`,`MESSAGE`) VALUES ('{name}','{email}','{msg}')")
        db.commit()
        
        
    def Comment_db(self,email,body):
        my_cursor.execute(f"INSERT INTO comment (`EMAIL`,`BODY`) VALUES ('{email}','{body}'")
        db.commit()
        
        
    def Faq_db(self,body):
        my_cursor.execute(f"INSERT INTO faq (`QUESTION` VALUES ('{body}')")
        db.commit()
        
    def Restaurants_db(self,id,resName,fname,city,phone,email,owner,resPhone,sun,mon,tue,wed,thur,fri,sat,breakfast,lunch,dinner,cafe,local,internation,fastfood,drinks,cash,card,paypal,transfer,opened,location):
            my_cursor.execute(f"INSERT INTO register (`_id`,`Restaurant_Name`,`Full_Name`,`City`,`Phone`,`Email`,`Owner`,`Restaurants_Phone`,`sun`,`mon`,`tue`,`wed`,`thur`,`fri`,`sat`,`breakfast`,`lunch`,`dinner`,`cafe`,`local`,`international`,`fastfood`,`drinks`,`cash`,`card`,`paypal`,`transfer`,`opened`,`location`)  VALUES ('{id}','{resName}','{fname}','{city}','{phone}','{email}','{owner}','{resPhone}','{sun}','{mon}','{tue}','{wed}','{thur}','{fri}','{sat}','{breakfast}','{lunch}','{dinner}','{cafe}','{local}','{internation}','{fastfood}','{drinks}','{cash}','{card}','{paypal}','{transfer}','{opened}','{location}') ")    
            db.commit()
        
    def get_restaurants(self):
            res = my_cursor.execute("SELECT * FROM register ")
            


# mysql = Mysql_db()
# mysql.Contact_db('david','someone@gmail.com','This is me!')

# db.commit()
# my_cursor.close()
# print('sent!')

mysql_db = Mysql_db()

print("mysql connected")
# app = Flask(__name__)


        
# if __name__ == "__main__":
#     app.run(debug=True)
