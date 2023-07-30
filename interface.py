import config
import numpy as np
from flask import Flask, request, render_template
from utils import Life_Expectancy_Prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('life_expectancy.html')

@app.route('/life_ecpectancy_prediction', methods = ['GET','POST'])
def predict_life():
    if request.method == 'GET':
        data = request.args.get
        Country = data('Country')
        Year =eval(data('Year'))
        Status=data('Status')
        Adult_Mortality=eval(data('Adult_Mortality'))
        infant_deaths=eval(data('infant_deaths'))
        Alcohol=eval(data('Alcohol'))
        percentage_expenditure=eval(data('percentage_expenditure'))
        Hepatitis_B=eval(data('Hepatitis_B'))
        Measles=eval(data('Measles'))
        BMI=eval(data('BMI'))
        under_five_deaths=eval(data('under_five_deaths'))
        Polio = eval(data('Polio'))
        Total_expenditure=eval(data('Total_expenditure'))
        Diphtheria=eval(data('Diphtheria'))
        HIV_AIDS=eval(data('HIV_AIDS'))
        GDP=eval(data('GDP'))
        Population=eval(data('Population'))
        thinness__1_19_years=eval(data('thinness__1_19_years'))
        thinness_5_9_years=eval(data('thinness_5_9_years'))
        Income_composition_of_resources=eval(data('Income_composition_of_resources'))
        Schooling=eval(data('Schooling'))
        obj = Life_Expectancy_Prediction(Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,Hepatitis_B
                                         ,Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,GDP,
                                        Population,thinness__1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling)
        predict_life = obj.life_expectancy_prediction()
        return render_template('life_expectancy.html', prediction = predict_life)

    elif request.method == 'POST':
        data = request.form
        print(data)
        Country = data['Country']
        Year = eval(data['Year' ])
        Status = data['Status']
        Adult_Mortality = eval(data['Adult_Mortality'])
        infant_deaths = eval(data['infant_deaths'])
        Alcohol = eval(data['Alcohol'])
        percentage_expenditure=eval(data['percentage_expenditure'])
        Hepatitis_B=eval(data['Hepatitis_B'])
        Measles=eval(data['Measles'])
        BMI=eval(data['BMI'])
        under_five_deaths=eval(data['under_five_deaths'])
        Polio = eval(data['Polio'])
        Total_expenditure=eval(data['Total_expenditure'])
        Diphtheria=eval(data['Diphtheria'])
        HIV_AIDS=eval(data['HIV_AIDS'])
        GDP=eval(data['GDP'])
        Population=eval(data['Population'])
        thinness__1_19_years=eval(data['thinness__1_19_years'])
        thinness_5_9_years=eval(data['thinness_5_9_years'])
        Income_composition_of_resources=eval(data['Income_composition_of_resources'])
        Schooling=eval(data['Schooling'])
        obj = Life_Expectancy_Prediction(Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,Hepatitis_B
                                         ,Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,GDP,
                                        Population,thinness__1_19_years,thinness_5_9_years,Income_composition_of_resources,Schooling)
        predict_life = obj.life_expectancy_prediction()
        return render_template('life_expectancy.html', prediction = predict_life)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.port_number)






        
        