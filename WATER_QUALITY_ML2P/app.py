from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__,static_url_path='/static')

if __name__=='__main':
    app.run(debug=True)
    
model=pickle.load(open('water.pkl','rb'))
@app.route('/')

def home():
    return render_template('home.html')
@app.route('/',methods=['POST'])


def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])



def waterPred():
    ph=request.form['ph']
    hardness=request.form['hardness']
    solids=request.form['solids']
    choloronim=request.form['chloromines']
    sulphate=request.form['sulphate']
    conductivity=request.form['conductivity']
    halomethanes=request.form['trihalomethanes']
    carbon=request.form['organic carbon']
    turbidity=request.form['turbidity']
    
    formdata=[ph,hardness,choloronim,solids,sulphate,conductivity,halomethanes,carbon,turbidity]
    cleanData=[float(i) for i in formdata]
    
    arr=np.array(cleanData).reshape(1,-1)
    result=model.predict(arr)
    return render_template('predict.html',data=result[0])
    
