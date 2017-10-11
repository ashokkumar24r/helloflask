from flask import Flask
#from flask import request

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='AshokStudy'):
    #name=request.args.get('name',name)
    return "Hell0 {}" .format(name)

app.run(debug=True,port=8000,host='127.0.0.1')
