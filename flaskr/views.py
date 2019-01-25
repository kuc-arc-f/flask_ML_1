# 日本語

# coding: utf-8
#
from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
import numpy as np
#
@app.route('/')
def show_entries():
    return redirect(url_for('predict_show'))
#
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    from flaskr.include.pred_price import  PredPrice
    if request.method == "POST":
        siki_price=request.form['siki_price']
        rei_price =request.form['rei_price']
        menseki   =request.form['menseki']
        nensu     =request.form['nensu']
        toho      =request.form['toho']
#        print(request.form )
        #param
        params = {"siki_price" : siki_price
        , "rei_price" : rei_price
        , "menseki" : menseki
        , "nensu"   : nensu
        , "toho"    : toho
        }
#        print("#POST")
        pred =PredPrice()
        model =pred.load_model()
        df = pred.load_data( params )
        price = model.predict(df )
        price_int = np.array( price , np.int32)        
        print( price_int[0] )
    #print(model )
        return render_template('show_price.html' ,price=price_int[0] )
    else:
        return "0"
#
@app.route('/predict_show', methods=['GET', 'POST'])
def predict_show():
    return render_template('predict.html' )
#
