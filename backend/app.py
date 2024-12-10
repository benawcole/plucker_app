import os
from flask import Flask, request, render_template
from db.db_connection import get_flask_database_connection
from flask_cors import CORS

# Create a new Flask app
app = Flask(__name__)
CORS(app)

# == Your Routes Here ==
#--------------Route Example-------------
# @app.route('/goodbye', methods = ['GET'])
# def say_goodbye():
#     return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
