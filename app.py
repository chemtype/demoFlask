import os
import base64
import subprocess
import uuid
from PIL import Image
from io import BytesIO
from random import randrange
from flask import Flask, render_template, request, redirect, make_response, url_for, send_from_directory

#Configuration
app = Flask(__name__)
#UPLOAD_FOLDER = '/Users/bradleyemi/demoFlask/uploads'
UPLOAD_FOLDER = '/home/azureuser/demoFlask/uploads'
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
        im.save(UPLOAD_FOLDER + '/unlabeled' + '/typeset_'+uuid.uuid4().hex+'.png', 'PNG')
        print "saved"
    return render_template("indextemp.html")

@app.route('/train', methods=['GET','POST'])
def trainScreen():
    if request.method == 'POST':
        data = request.json
        # in POST method expect previously sent molecule id
        moleculeID = data["moleculeID"]
        imageData = data["base64PNGData"]
        im = Image.open(BytesIO(base64.b64decode(imageData)))
        try: 
            im.save(UPLOAD_FOLDER + "/" + str(moleculeID) + '/train_'+uuid.uuid4().hex+'.png', 'PNG')
        except IOError:
            try:
                subprocess.call(["mkdir", UPLOAD_FOLDER + "/" + str(moleculeID)])
                im.save(UPLOAD_FOLDER + "/" + str(moleculeID) + '/train_'+uuid.uuid4().hex+'.png', 'PNG')
            except:
                resp = make_response('{"redirect" : "'+ url_for('failureScreen') + '"}', 200)
                resp.mimetype = "application/json; charset=utf-8"
                return resp
        resp = make_response('{"redirect" : "'+ url_for('successScreen') + '"}', 200)
        resp.mimetype = "application/json; charset=utf-8"
        return resp
    # In GET method randomly choose a molecule id
    moleculeID = randrange(26)
    return render_template("train.html", molecule=moleculeID)

@app.route('/train/success', methods=['GET','POST'])
def successScreen():
    return render_template("success.html")

@app.route('/train/failure', methods=['GET','POST'])
def failureScreen():
    return render_template("failure.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
import os
import base64
import subprocess
import uuid
from PIL import Image
from io import BytesIO
from random import randrange
from flask import Flask, render_template, request, redirect, make_response, url_for, send_from_directory

#Configuration
app = Flask(__name__)
#UPLOAD_FOLDER = '/Users/bradleyemi/demoFlask/uploads'
UPLOAD_FOLDER = '/home/azureuser/demoFlask/uploads'
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
        im.save(UPLOAD_FOLDER + '/unlabeled' + '/typeset_'+uuid.uuid4().hex+'.png', 'PNG')
        print "saved"
    return render_template("indextemp.html")

@app.route('/train', methods=['GET','POST'])
def trainScreen():
    if request.method == 'POST':
        data = request.json
        # in POST method expect previously sent molecule id
        moleculeID = data["moleculeID"]
        imageData = data["base64PNGData"]
        im = Image.open(BytesIO(base64.b64decode(imageData)))
        try: 
            im.save(UPLOAD_FOLDER + "/" + str(moleculeID) + '/train_'+uuid.uuid4().hex+'.png', 'PNG')
        except IOError:
            try:
                subprocess.call(["mkdir", UPLOAD_FOLDER + "/" + str(moleculeID)])
                im.save(UPLOAD_FOLDER + "/" + str(moleculeID) + '/train_'+uuid.uuid4().hex+'.png', 'PNG')
            except:
                resp = make_response('{"redirect" : "'+ url_for('failureScreen') + '"}', 200)
                resp.mimetype = "application/json; charset=utf-8"
                return resp
        resp = make_response('{"redirect" : "'+ url_for('successScreen') + '"}', 200)
        resp.mimetype = "application/json; charset=utf-8"
        return resp
    # In GET method randomly choose a molecule id
    moleculeID = randrange(26)
    return render_template("train.html", molecule=moleculeID)

@app.route('/train/success', methods=['GET','POST'])
def successScreen():
    return render_template("success.html")

@app.route('/train/failure', methods=['GET','POST'])
def failureScreen():
    return render_template("failure.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)

