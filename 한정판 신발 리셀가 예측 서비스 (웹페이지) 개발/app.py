from flask import Flask, render_template, request
import numpy as np
import pickle 
import pandas as pd

loaded_model = pickle.load(open('lasso0.pkl', 'rb'))
df = pd.read_csv('StockX3.csv')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=["POST"])
def predict():
    if request.method=="POST":
        data2 = int(request.form['Retail Price'])
        data4 = int(request.form['yeezy350'])
        data5 = int(request.form['airjordan'])
        data6 = int(request.form['airforce'])
        data7 = int(request.form['airmax90'])
        data8 = int(request.form['airmax97'])
        data9 = int(request.form['presto'])
        data10 = int(request.form['vapomax'])
        data11 = int(request.form['blazer'])
        data12 = int(request.form['zoom'])
        data13 = int(request.form['react'])
        data14 = int(request.form['California'])
        data15 = int(request.form['New York'])
        data16 = int(request.form['Oregon'])
        data17 = int(request.form['Florida'])
        data18 = int(request.form['Texas'])
        data19 = int(request.form['Other States'])
        data20 = 0.19887497 
        data21 = int(request.form['Black'])
        data22 = int(request.form['White'])
        data23 = int(request.form['Grey'])
        data24 = int(request.form['Red'])
        data25 = int(request.form['Green'])
        data26 = int(request.form['Neo'])
        data27 = int(request.form['Orange'])
        data28 = int(request.form['Tan/Brown'])
        data29 = int(request.form['Pink'])
        data30 = int(request.form['Blue'])
        #data31 = int(float(request.form['Colorful']))
        data32 = int(request.form['Number of Sales'])
        data33 = int(request.form['Days_Since'])

        arr = np.array([[data2, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24, data25, data26, data27, data28, data29, data30, data32, data33]])
        columns_name = ['Retail Price', 'yeezy350', 'airjordan', 'airforce','airmax90', 'airmax97', 'presto', 'vapomax', 'blazer', 'zoom', 'react', 'California', 'New York', 'Oregon', 'Flordia', 'Texas', 'Other States','size_freq','Black','White','Grey','Red','Green','Neo','Orange','Tan/Brown','Pink','Blue', 'Number of Sales','Days_Since']#'Colorful',
        dataall = pd.DataFrame(arr, columns=columns_name)
        predict = loaded_model.predict(dataall)
        return render_template('predict.html', predict=predict)
    else:
        return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
