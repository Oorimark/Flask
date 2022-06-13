from unicodedata import name
from flask import Flask, request
import sys
import os
import requests
from pathlib import Path

from flask.templating import render_template
from flask_wtf import FlaskForm
from pymongo import message


# from setuptools import setup, find_packages
  
# setup(
#     name = 'services',
#     packages= find_packages(),
# )

file = Path(__file__).resolve()
package_root_directory = file.parents[2]
sys.path.append(str(package_root_directory))



# from config._mysql.db_config import mysql_db
from config._mongodb.db_config import mongodb
from services.genToken import token_encode,generate_token
from services.hashpasswd import HashLetter
from services.emailing import plainMail, htmlMail, sendToken # the func takes in three arguments msg,header and recpt
from services.validate import validate                                  


# intialization ...
from index import app


# validate = Validate();

personInfo = {}
token_arr = []

if len(personInfo) == 30:
    personInfo.clear
    token_arr.clear()


# a decorator that connect the signUp route and validateEmail
def validDecor(f):
    token = token_encode("encode") 
    def wrapper(*args, **kwargs):
        f()

    return wrapper
        
def objectDeco(f):
    def wrapper(*args,**kwargs):
        return_func = f(*args, **kwargs)
        
        
 
# login route
@app.route("/login",methods=['GET','POST'])
def Login():
    try:
        if request.method == "POST":
            email = request.form['email']
            password = request.form['password']
            # 1. check if the email and password is in the db
            res = mongodb.Login(f"{name}",f"{email}",f"{password}")
        if res is True:
            # 2. generate a token
            token = generate_token()
            # 3. send a token to the mongodb db
            mongodb.token(token)
        else:
            status = "error"
            msg = "Sorry you are not Registered as a clan yet"
            message = [status,msg]
            return render_template('message.html', message = message)
    except Exception as e:
        status = "error"
        msg = "Something went wrong, Try Again!"
        return render_template('message.html', message = [status,msg,e])

# authentication: checking if username exist or not

# singup route
@app.route("/signup",methods=['GET','POST'])
def SignUp():
    if request.method == "POST":
        fullname = request.form['fullname'] 
        password = request.form['password']
        email = request.form['email']

        if validate.ValidateText(fullname) and validate.ValidatePassword(password):
            # check if account already exist
            # res = mongodb.Login(f"{name}",f"{email}",f"{password}") 
            try:
                res = mongodb.Auth_email(email)
                if res is True:
                    status = "error"
                    msg = "An account with this email already exist"
                    return render_template("message.html", message = [status, msg])
                else: 
                                # generate token
                    # token = HashLetter(fullname[:5])
                    token = generate_token()
                    global token_arr
                    token_arr.append(token)
                    # sending token to the user
                    #sendToken(token,email)
                    res = requests.get(f"https://tasteclan.pythonanywhere.com/{token}/{email}")
                    status = "success"
                    personProfile(token,fullname,password,email)
                    temp_msg  = "A Link has been sent with your email, click the link to validate your Email"
                    message = [status,temp_msg]
                    return render_template('message.html', message= message)
            except Exception as e:
                    status = "error"
                    msg = "Sorry, the server cannot connect at the moment, Try Again!"
                    return render_template('message.html', message = [status,msg,e])
                
            
            # data should not be sent to the server except the user has validated his email
            
            # Mysql_db.Register_db(fullname,password) # mysql db
            # Mongodb_db.Restaurants_db(fullname,password) # mongodb db
        else: 
            status = 'error'
            msg = Exception("The Validaton was not successfull check parameters")

            return render_template('message.html',message= [status,msg])
        
    else: 
        status = 'error'
        msg = Exception("This operation cannot be performed")

        return render_template('message.html',message= [status,msg])


def personProfile(token,fName,Passwd,email):
    global personInfo
    personInfo[f'{token}'] = [f'{fName}', f'{Passwd}', f'{email}']
    return personInfo
    

@validDecor
@app.route("/verifymail/<token>", methods=['POST','GET'])
def ValidEmail(token):
    if token in token_arr:
        status = 'success'
        # send info to the db
        print(personInfo)
       # mysql_db.Register_db(personInfo[token][0], personInfo[token][2], personInfo[token][1]) # mysql db
        mongodb.Register_db(personInfo[token][0],personInfo[token][2], personInfo[token][1]) # mongodb db
        render_msg = "You\'ve successfully SignUp. You\'re Now a clan"
        return render_template('message.html',message= [status, render_msg])
    else:
        status = 'error'
        render_msg = "Sorry you use the wrong token or token as expired, try signing Up again"
        return render_template('message.html',message = [status,render_msg])
        
### route for Register sign up
# registeration would be covered by Node.js

# comment route
@app.route("/comment",methods = ['GET','POST'])
def Comment():
    email = request.form['email']
    body = request.form['body']
    #sending the comment to the db...
    try:
        mysql_db.Comment_db(email, body)
        status = "success"
        msg = "Successfully posted comment"
        return render_template('message.html', message = [status,msg])
    except Exception as e:
        status = "error"
        msg = "Sorry, the server cannot connect at the moment"
        return render_template('message.html', message = [status,msg])
        #the body of the comment is 400 words
            
            
# contact route
@app.route("/contact", methods = ['POST'])
def Contact(): 
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    #sending contact details to the db...
    try:
        mysql_db.Contact_db(name, email, message)
        status = "success"
        msg = "We'd get back to your shortly"
        return render_template('message.html', message = [status,msg])
    except Exception as e:
        status = "error"
        msg = "Sorry, the server cannot connect at the moment, Try Again!"
        return render_template('message.html', message = [status,msg,e])
        
    
# FAQ route
@app.route("/faq", methods = ['POST'])
def FAQ():
    body = request.form['body']
    try:
        mysql_db.Faq_db(body)
        status = "success"
        msg = "We've received your question, we'd get to you shortly"
        return render_template('message.html', message = [status,msg])
    except Exception as e:
        status = "error"
        msg = "Something went wrong while submission, Try Again!"
        return render_template('message.html', message = [status,msg,e])
    
# subscribers
@app.route("/subscriber", methods = ['POST'])
def Subscribers():
    email = request.form['email']
    try:
        mongodb.Subscribers(email)
        status = "success"
        msg = "We'd keep you in touch for latest updates"
        return render_template('message.html', message = [status, msg])
    except Exception as e:
        status = "error"
        msg = "Something went wrong, Try Again!"
        return render_template('message.html', message = [status,msg,e])
    


# registering restaurants
@app.route("/register/<cat>", methods=['GET'])
def Register_Res(cat):
    if cat == "restaurants":
        try:
            resname = request.args.get('restaurants_name')
            fname = request.args.get('full_name')
            city = request.args.get('city')
            phone = request.args.get('phone')
            email = request.args.get('email')
            owner = request.args.get('owner')
            resphone = request.args.get('restaurants_phone')
            
            # step 2 (days)
            sun = request.args.get('sunday') #["off" if  is None else "on"] 
            mon = request.args.get('monday')
            tue = request.args.get('tuesday')
            wed = request.args.get('wednesday')
            thur = request.args.get('thursday')
            fri = request.args.get('friday')
            sat = request.args.get('saturday')
            
            # step 3
            # (services)
            breakfast = request.args.get('Breakfast')
            lunch = request.args.get('Lunch')
            dinner = request.args.get('Dinner')
            cafe = request.args.get('cafe')
            # (cuisines)
            local = request.args.get('Local')
            internation = request.args.get('internation')
            fastfood = request.args.get('FastFood')
            drinks = request.args.get('Drinks')
            # (payment)
            cash = request.args.get('Cash')
            card = request.args.get('Card')
            paypal = request.args.get('paypal')
            transfer = request.args.get('transfer')
            # (status)
            opened = request.args.get('opened')
            location = request.args.get('restaurants_address') 
            
            # authenticate restaurants by their name and email
            res = mongodb.Auth_res(resname,email)
            print(res)
            if res is True:
                status = "error"
                msg = "Sorry a user with this name and email already exist"
                return render_template('message.html',message = [status,msg])
            else:
                token = generate_token()
                # send to mysql db
                mysql_db.Restaurants_db(token,resname,fname,city,phone,email,owner,resphone,sun,mon,tue,wed,thur,fri,sat,breakfast,lunch,dinner,cafe,local,internation,fastfood,drinks,cash,card,paypal,transfer,opened,location)
                # send to mongodb db
                mongodb.Restaurants_db(token,resname,fname,city,phone,email,owner,resphone,sun,mon,tue,wed,thur,fri,sat,breakfast,lunch,dinner,cafe,local,internation,fastfood,drinks,cash,card,paypal,transfer,opened,location)
                status = "success"
                msg = "Eureka! you are now a registered vendor witht the clan"
                return render_template('message.html', message = [status,msg])
        except Exception as e:  
            status = "error"
            msg = "Something went wrong, Try Again!"
            return render_template('message.html', message = [status,msg,e])
    elif cat == "drivers":
        pass
    else:
        pass
# if __name__ == "__main__":
#     app.run(debug=True)

    
