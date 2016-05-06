from flask import Flask, render_template, request, make_response, redirect
import os
import sqlite3

app = Flask(__name__, template_folder='.')



app.debug = True

def setupdb():
    conn = sqlite3.connect('db.db')
    
    conn.execute('CREATE TABLE IF NOT EXISTS inbox(title,email,first,surname,number,comment)')
    
    conn.commit()
    conn.close()

setupdb()



@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/')
def root():
    return redirect('/home.html')




@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

@app.route('/asterion.html')
def asterion():
    return render_template('asterion.html')

@app.route('/aventador.html')
def aventador():
    return render_template('aventador.html')

@app.route('/centenario.html')
def centenario():
    return render_template('centenario.html')



@app.route('/contactus.html')
def contactus():
    return render_template('contactus.html')

@app.route('/features.html')
def features():
    return render_template('features.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/huracan.html')
def huracan():
    return render_template('huracan.html')

@app.route('/veneno.html')
def veneno():
    return render_template('veneno.html')

    

@app.route('/saveindb', methods=['post'])
def saveindb():
    conn = sqlite3.connect('db.db')
    
    title = request.form['title']
    email = request.form['email']
    first = request.form['first']
    surname = request.form['surname']
    number = request.form['number']
    comment = request.form['comment']
    
    conn.execute('INSERT INTO inbox (title,email,first,surname,number,comment) VALUES (?,?,?,?,?,?)', [title,email,first,surname,number, comment])
    conn.commit()
    conn.close()
    return redirect('/')

    




app.run(port=int(os.getenv('PORT', '8080')), host=os.getenv('IP', '0.0.0.0'))