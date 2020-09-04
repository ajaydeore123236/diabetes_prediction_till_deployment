import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
Diabetes_data=pd.read_csv('E:\i neuron ML\Machine Learning\logistic regression\Logistic-regression_final\diabetes.csv')
Diabetes_data['Glucose']=Diabetes_data['Glucose'].replace(0,np.mean(Diabetes_data['Glucose']))
Diabetes_data['BloodPressure']=Diabetes_data['BloodPressure'].replace(0,np.mean(Diabetes_data['BloodPressure']))
Diabetes_data['SkinThickness']=Diabetes_data['SkinThickness'].replace(0,np.mean(Diabetes_data['SkinThickness']))
Diabetes_data['Insulin']=Diabetes_data['Insulin'].replace(0,np.mean(Diabetes_data['Insulin']))
Diabetes_data['DiabetesPedigreeFunction']=Diabetes_data['DiabetesPedigreeFunction'].replace(0,np.mean(Diabetes_data['DiabetesPedigreeFunction']))
Diabetes_data['Age']=Diabetes_data['Age'].replace(0,np.mean(Diabetes_data['Age']))

regression=LogisticRegression()
train_data=Diabetes_data.drop(['Outcome'],axis=1)
test_data=Diabetes_data['Outcome']
regression_object=regression.fit(train_data,test_data)
filename='Algo.pickle'
pickle.dump(regression_object,open(filename,'wb'))
