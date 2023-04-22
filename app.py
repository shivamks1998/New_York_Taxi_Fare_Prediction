from flask import request,Flask
import pickle
import numpy as np

app = Flask(__name__)

def load_model(path):
    global model
    path =  open(path,'rb') 
    model = pickle.load(path)

@app.route("/")
def hello():
    return "Nice to meet you"

@app.route("/predict",methods= ['POST','GET'])
def prediction():
    if request.method=='POST':
        data = request.get_json(force=True)
        data = np.array([data])
        prediction = model.predict(data)
        return str(prediction[0])
    else: 
        return "please use curl for post request"

if __name__ =="__main__":
    path = ".\\model_weight_noncol.pb"
    load_model(path)
    app.run(debug = True,host ="0.0.0.0" )
