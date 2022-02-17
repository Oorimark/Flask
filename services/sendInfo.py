from flask import Flask
from flask_mail import Mail, Message
from email import plainMail

app = Flask(__name__)

mail = Mail(app)

def Bulk():
    #adding attachment
    with app.open_resource('file_name') as file:
        # attach the right MIME type
        file.attach('fcat.jpg', 'image/jpeg', file.read())
    with mail.connect as con:
        msg = Message('Verfying email', recepients=[])
        con.send()
        
script = """
            df = pd.read_csv("")
            msg = ""
            for val in df['EMAIL']:
                plainMail(msg,val)
                
         """


#exec(script) #// uncomment to run the file