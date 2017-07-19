__author__ = 'ASHOK KUMAR'


from flask import Flask
app = Flask(__name__)

@app.route("/ashok")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()