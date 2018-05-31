import os
from flask import Flask,flash,redirect,url_for,render_template,request, jsonify
from data import Articles
import pandas as pd
from plot_maps import executeData

app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = './data/'
Articles= Articles()



@app.route('/')

def index():
		return render_template ('home.html')

@app.route('/about')
def about ():
	return render_template ('about.html')

@app.route('/articles')
def articles ():
	return render_template ('articles.html', articles= Articles)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect("/upload")
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect("/upload")
        if file :
            #filename = file.filename #for later use when you want to have different files ***
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],'data.csv'))
            executeData() #execute main function in plot_maps.py with the file data.csv [to change when using diffrent files] 
            return redirect("/result") #redirect to the result map
    return render_template('upload.html')

@app.route('/result')
def result():
    return render_template ('maps.html')
@app.route("/export", methods=['GET'])
def export_records():
    return 

if __name__ == '__main__' :
	app.run(debug= True)
