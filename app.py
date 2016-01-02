import os
import base64
import subprocess
from PIL import Image
from io import BytesIO
from random import randrange
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

#Configuration
app = Flask(__name__)
UPLOAD_FOLDER = '/home/azureuser/demoFlask'
NEW_UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@app.route('/typeset', methods=['GET', 'POST'])
def homeScreen():
    if request.method == 'POST':
        data = request.json
        imageData = data["base64PNGData"]
        im = Image.open(BytesIO(base64.b64decode(imageData)))
        im.save(UPLOAD_FOLDER + '/unlabeled' + '/test.png', 'PNG')
        print "saved"
    return render_template("index.html")

@app.route('/train', methods=['GET','POST'])
def trainScreen():
    moleculeID = randrange(26)
    if request.method == 'POST':
        data = request.json
        imageData = data["base64PNGData"]
        im = Image.open(BytesIO(base64.b64decode(imageData)))
        try: 
            im.save(UPLOAD_FOLDER + str(moleculeID) + '/test.png', 'PNG')
        except:
            subprocess.call(["mkdir", UPLOAD_FOLDER + str(moleculeID)])
            im.save(UPLOAD_FOLDER + "/" + str(moleculeID) + '/test.png', 'PNG')
        print "saved"
    return render_template("train.html", molecule=moleculeID)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
