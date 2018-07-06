from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/result',methods = ['GET'])
def result():
	name  = request.args.get('name','')
	age   = request.args.get('age','')
	number= request.args.get('numb','')
	return  "name =" + name + " <br/> age =" + age + "<br/> number = " + number
	

if __name__== "__main__":
	app.run()
