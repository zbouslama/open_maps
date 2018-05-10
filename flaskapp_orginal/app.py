from flask import Flask, render_template,request, jsonify
from data import Articles
import pandas as pd

app = Flask (__name__)

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

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        data_xls = pd.read_excel(f)
        return data_xls.to_html()
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/export", methods=['GET'])
def export_records():
    return 

if __name__ == '__main__' :
	app.run(debug= True)
