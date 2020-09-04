
import pickle
from flask import Flask,request,render_template,jsonify
from flask_cors import cross_origin
import pickle
app1=Flask(__name__)
@app1.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')
@app1.route('/process',methods=['POST','GET'])
def process1():
    if (request.method=='POST'):
        pregencies=float(request.form['Pregencies'])
        glucose=float(request.form['Glucose'])
        bloodpresure=float(request.form['BloodPressure'])
        SkinThickness=float(request.form['SkinThickness'])
        Insulin=float(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        DiabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
        Age=float(request.form['Age'])
        print(Age)
        #result=[pregencies,glucose,bloodpresure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        filename='Algo.pickle'
        model=pickle.load(open(filename,'rb'))
        result1=model.predict([[pregencies,glucose,bloodpresure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if result1==1:
            return render_template('result.html',result="Diabitic")
        else:
            return render_template('result.html',result="NO Diabitic")

if __name__=='__main__':
    app1.run(debug=True)