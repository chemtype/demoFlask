import os
from random import randrange
from flask import Flask, render_template, request, redirect, url_for

#Configuration
app = Flask(__name__)
UPLOAD_FOLDER = '/Users/bradleyemi/newchemtype/uploads'
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def homeScreen():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/")
    return render_template("index.html")

@app.route('/train', methods=['GET','POST'])
def trainScreen():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/")
    return render_template("train.html", molecule=randrange(26))

if __name__ == '__main__':
    app.run(port=8000)
