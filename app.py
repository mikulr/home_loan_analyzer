import numpy as np
import pandas as pd
import json
from flask import Flask, jsonify, render_template, request 
import pickle
#################################################

#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def index():

  
    return render_template("index.html") 

@app.route("/result", methods=["post"])
def get_values():

    # Get input values for the model from html & convert string to int 
    input = []
    state = []
    loan_amount = request.form["loanamount"] # for the input
    input.append(int(loan_amount))
    income = request.form["income"]
    input.append(int(income))
    loantype = request.form["type"]
    for i in loantype:
        input.append(int(i))
    raw_residence = request.form["resi"]
    state= raw_residence[52:]
    residence=raw_residence[:52]
    for i in residence:
        input.append(int(i))
    aeth = request.form["aeth"]
    for i in aeth:
        input.append(int(i))
    coaeth = request.form["coaeth"]
    for i in coaeth:    
        input.append(int(i))
    arac = request.form["arac"]
    for i in arac:
        input.append(int(i))
    coarac = request.form["coarac"]
    for i in coarac:
        input.append(int(i))
    asex = request.form["asex"]
    for i in asex:
        input.append(int(i))
    coasex = request.form["coasex"]
    for i in coasex:
        input.append(int(i))

    print("---------------------------------------------")
    print(input)
    print("---------------------------------------------")
    print(residence)
    print(state)
   


    model = pickle.load(open('resources/lr_classifier.pkl', 'rb'))       
    chance=0

    data = np.array(input)[np.newaxis, :]  # converts shape for model test
    predict = model.predict(data)  # runs model on the data
    prob= model.predict_proba(data)


    if predict == [1]:
        prediction = "We predict success, congratulations!"
    else:
        prediction = "Sorry, you will likely not qualify."

    prob= model.predict_proba(data)

    if predict == [1]:
        chance = prob[0][1]
    else:
        chance = prob[0][0]

    print(prediction)
    print("---------")
    print(chance)

            
    model_result = {
        "prediction":prediction,
        "probability":str((chance*100)) + '%'
    }
  
    with open('resources/state_summary_remix.json', 'r') as myfile:
        data = myfile.read()

    appstate= {'openingState': state}

    # Render the result through a html page
    return render_template("result.html", result = model_result, stateData=data, homeState=appstate) 
    return render_template("index.html",)    

#  ,result = model_result

if __name__ == '__main__':
    app.run(debug=True)
