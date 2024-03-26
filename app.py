from flask import Flask, render_template, request
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('rainfall_prediction_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        
        # Make the prediction
        prediction = model.predict([[temperature, humidity]])
        
        return render_template('index.html', prediction=prediction)
    else:
        return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
