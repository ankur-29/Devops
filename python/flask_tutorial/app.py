from flask import flask

app = Flask(__name__)

@app.route('/') #localhost:5000
@app.route('/second') #localhost:5000/second
@app.route('/api/<user>') #localhost:5000/api/ankur

#home route function
def home:
    print("Hello guys!!")
    return "Welcome to flask learning"

#second route function
def second:
    return "Welcome to second page"

#varible name as route
def name(user): 
    return "Hi " + name + ", Welcome to flask learning"

if __name__ == "__main__" :
    app.run(debug = True)