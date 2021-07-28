import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
app = Flask(__name__)
model=pickle.load(open('university.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['post'])
def y_predict():
    gre=request.form["gre"]
    tofel=request.form["tofel"]
    select_university=request.form["age"]
    sop1=request.form["sop1"]
    lor1=request.form["lor1"]
    cgpa1=request.form["cgpa1"]
    research=request.form["re"]
    total=[[gre,tofel,select_university,sop1,lor1,cgpa1,research]]
    final=np.asarray(total,dtype='float64')
    prediction=model.predict(final)
    if(prediction==False):
            return render_template('no.html',prediction_text='You dont have a chance')
    else:
            return render_template('yes.html',prediction_text="You have a choice")

if __name__=="__main__":
    app.run(debug=True)        