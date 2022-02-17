from flask import Flask
from flask_mail import Mail, Message
import blinker
import sys
from pathlib import Path

app = Flask(__name__)


file = Path(__file__).resolve()
package_root_directory = file.parents[1]
print(package_root_directory)
sys.path.append(str(package_root_directory))

# import config.email.emailconfig
# from config.email.emailconfig import configMail






#configuration of the mail


app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'markpublicm@gmail.com'
app.config['MAIL_PASSWORD'] = 'markoori'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_DEFAULT_SENDER'] = ('Tasteclan','markpublicm@gmail.com')
app.config['MAIL_ASCII_ATTACHMENTS'] = False



# configMail()

""" The email script provides and avenue for mailing here service here mails 
    can be sent easily by just using the PlainMail function, for plain mails
    and 
"""

# plain text mails
mail = Mail(app)
def sendToken(token,recp):
    with app.app_context():
        msg = Message(' Verifying Email <no reply>', recipients=[f'{recp}'])
        msg.html = f"<p>Thank you for choosing Tasteclan please validate your mail. Your token is {token}. click the Link <a href='http://127.0.0.1:5000/verifymail/{token}'>verify account</a></p>"
        mail.send(msg)
    return "success"

def plainMail(msg,header,recp):
    with app.app_context():
        message = Message(header,recipients=[f'{recp}'])
        message.body = msg
        mail.send(message)
    return "success"
# html formated mail
def htmlMail(msg,header,recp):
    with app.app_context():
        message = Message(header,recipients=[f'{recp}'])
        message.body = msg
        mail.send(message)
    return "success"


# print(sendToken(2343,'oorimark@gmail.com'))
# plainMail("Whats Bro, how do you do?",'oorimark@gmail.com')
# print("success")



