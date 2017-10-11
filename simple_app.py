__author__ = 'ASHOK KUMAR'

from flask import Flask

app = Flask('__name__')

app.run(debug=True, port=8000,host='127.0.0.1')