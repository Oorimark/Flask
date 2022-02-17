from flask import Flask, request, render_template

# from pathlib import Path
# import sys

# file = Path(__file__).resolve()
# package_root_directory = file.parents[2] # moves to the root directory for import
# sys.path.append(str(package_root_directory))

app = Flask(__name__, template_folder='template')


# initializatons...  

   
@app.route("/")
def Home():
    status = "error"
    msg = "Hey! This request cannot be made."
    message = [status,msg]
    return render_template('index.html', message = message)

# importing route
from api.routes.index import *

 
 
if __name__ == "__main__":
    app.run(debug=True)  