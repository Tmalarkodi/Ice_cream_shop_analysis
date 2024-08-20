import joblib
from flask import Flask, render_template, request

app = Flask(__name__)
model = joblib.load('model.pkl')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def predict():
    prediction=model.predict([[float(request.form.get("temperature"))]])
    output=round(prediction[0],2)
    #print(output)
    return render_template('index.html',prediction_text=f'Total revenue generted is Rs.{output}/-') 

if __name__=='__main__':
  app.run(debug=True)