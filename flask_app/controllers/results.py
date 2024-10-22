import os
from flask import Flask, request, redirect, render_template
import pymysql
from werkzeug.utils import secure_filename
from flask_app.models import user

app = Flask(__name__)


# #where uploads will be stored
# UPLOAD_FOLDER = 'C:\Users\Trevor\OneDrive\Desktop\Paddock\Uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # making sure folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user=user.User)

# @app.route('/upload_file', methods = ['POST'])
# def upload_file():
#     if 'file1' not in request.files or 'file2' not in request.files:
#         return 'No files uploaded'
    
#     file1 = request.files['file1']
#     file2 = request.files['file2']
    
#     if file1.filename == '' or file2.filename == '':
#         return 'No files selected'
    
#     file1_name = secure_filename(file1.name)
#     file2_name = secure_filename(file2.name)
    
#     file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1_name)
#     file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2_name)
    
#     file1.save(file1_path)
#     file2.save(file2_path)
    
#     file1_mimetype = file1.mimetype
#     file2_mimetype = file2.mimetype
    
    
    