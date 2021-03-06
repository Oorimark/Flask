from flask import Flask, request, render_template

# from pathlib import Path
# import sys

# file = Path(__file__).resolve()
# package_root_directory = file.parents[2] # moves to the root directory for import
# sys.path.append(str(package_root_directory))

app = Flask(__name__, template_folder='template')


# initializatons...  

   
@app.route("/", methods=["GET","POST"])
def Home():
    status = "success"
    msg = "Welcome to Tasteclan."
    det = "This is so because a bad request is made"
    message = [status,msg,det]
    return render_template('index.html', message = message)

# importing route
from api.routes.index import *

 
 
if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")  
