# from flask import Flask
import pymongo

from pymongo import MongoClient
from pymongo import database

# app = Flask(__name__)

password = "tasteclan"
mong_database = "TasteClan"

cluster = MongoClient("mongodb+srv://Tastec:tasteclan@cluster0.x2e0r.mongodb.net/Tasteclan?retryWrites=true&w=majority")
db = cluster["Tasteclan"]

# choosing a collection
# collection = db["name of db"]

# collection.insert_many([])

class Mongodb_db():
        
    def Restaurants_db(self,id,resName,fname,city,phone,email,owner,resPhone,sun,mon,tue,wed,thur,fri,sat,breakfast,lunch,dinner,cafe,local,internation,fastfood,drinks,cash,card,paypal,transfer,opened,location):
        collecton = db['register']
        query = {'id':id,'Restaurants_Name': resName,'Full_Name': fname, 'City': city, 'Phone': phone, 'Email': email,
                 'Owner': owner, 'Restaurants_Phone': resPhone,'sun':sun,'mon':mon,'tue':tue,'wed':wed,'thur':thur,'fri':fri,'sat':sat,
                  'breakfast':breakfast,'lunch':lunch,'dinner':dinner,'cafe':cafe,'local':local,'international':internation,
                  'fastfood':fastfood,'drinks':drinks,'cash':cash,'card':card,'paypal':paypal,'transfer': transfer,'opened': opened,
                   'location':location}
        collecton.insert_one(query)
        
    def Register(self,name, email, passwd):
        collection = db['user']
        post = {'name': name, 'email': email, 'password': passwd}
        collection.insert_one(post)
    
    def token(self, name, token):
        collection = db["token"]
        collection.insert_one({'name': name, 'token' : token})
        
    def Login(self,name,email,passwd):
        collection = db["user"]
        result = collection.find_one({'name': name, 'email': email, 'password': passwd})
        return False if result == None else True

    def Subscribers(self,email):
        collection = db["subsribers"]
        collection.insert_one({'email': email})
        
    def Auth_email(self,email):
        collection = db["user"]
        result = collection.find_one({'email': email})
        return False if result == None else True
        # print(result) 
    def Auth_res(self,name,email):
        collection = db["restaurants"]
        result = collection.find_one({'Restaurants_Name': name,'Email':email})
        return False if result == None else True

        

mongodb = Mongodb_db()
# res = mongodb.Login("david","Hello")
# print(res)
print("Mongodb connected")


# app.run(debug=True) if __name__ == "__main__" else print("Server unaccessible!")