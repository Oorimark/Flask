from flask import Flask

app = Flask(__name__)
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
