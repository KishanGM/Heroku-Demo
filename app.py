import numpy as np
from flask import Flask, request, jsonify, render_template
from model import make_predictions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = request.form['question']
    #_logger.info(f'Inputs: {text}')
    #final_features = [np.array(int_features)]
    prediction = make_predictions(text)

    output = prediction

    return render_template('index.html', prediction_text='Sentiment is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
