# from flask_app.config.mysqlconnection import connectToMySQL 
# from flask import flash
# from flask_app import app
# from flask_app.models import user
# from flask_app.controllers import results
# import datetime
# import os
# import pymysql
# from werkzeug.utils import secure_filename

# class Result:
    
    
    
#     this_db = "paddock_schema"
    
#     def __init__(self,data):
#         self.id = data["id"]
#         self.filename = data["filename"]
#         self.filetype = data["filetype"]
#         self.filepath = data["filepath"]
#         self.upload_time = data["upload_time"]
#         self.user = None
        
#     #where uploads will be stored
#     UPLOAD_FOLDER = 'C:\Users\Trevor\OneDrive\Desktop\Paddock\Uploads'
#     app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER;

#     # making sure folder exists
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER);
        
#     @classmethod
#     def store_file(cls,data):
#         query = "INSERT INTO result (filename, filetype, filepath, upload_time) VALUES = (%s, %s, %s, %('upload_time')s)"
#         result = connectToMySQL(cls.this_db).query_db(query,data)
#         return result
    

    

        
        
