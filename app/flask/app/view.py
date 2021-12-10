from app import app

from flask import  render_template
import requests as req
import json


@app.route('/')
def homepage():

    r = req.get(
        'https://api.chucknorris.io/jokes/random')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/category')
def category():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/categories/')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/animal')
def animal():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=animal')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/career')
def career():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=career')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/money')
def money():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=money')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/fashion')
def fashion():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=fashion')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/dev')
def dev():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=dev')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/celebrity')
def celebrity():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=celebrity')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/food')
def food():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=food')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/explicit')
def explicit():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=explicit')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/science')
def science():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=science')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/history')
def history():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=history')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/movie')
def movie():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=movie')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/music')
def music():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=music')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/political')
def political():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=political')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/religion')
def religion():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=religion')
    return render_template('app.html', jokes=json.loads(r.text)['value'])
@app.route('/sport')
def sport():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=sport')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

@app.route('/travel')
def travel():
    
    r = req.get(
        'https://api.chucknorris.io/jokes/random?category=travel')
    return render_template('app.html', jokes=json.loads(r.text)['value'])

