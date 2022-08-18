import pandas as pd
import sys
import json
import joblib 
from predictfile import predict_label

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alive():
    return render_template("index.html")    # Template appearance before result is shown


@app.route('/predict', methods=['POST','GET'])
def predict():
    """
    This function will be used for the prediction of customer review rating (either positive or negative)
    """
    
    if request.method == 'POST':
            client_review = request.form.get('review')
             

            
            
            ponev=predict_label(client_review)
            
        
            return render_template("index.html", result = ponev)

    if request.method == 'GET':
        return render_template("index.html")    # Positive or Negative result shown
    

if __name__ == '__main__':
   app.run(host="0.0.0.0",debug=True, port=5000)
