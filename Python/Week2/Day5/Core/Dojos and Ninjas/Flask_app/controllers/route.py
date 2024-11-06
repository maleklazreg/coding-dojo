from flask import render_template, redirect, request # type: ignore
from Flask_app.models.dojos import Dojo
from Flask_app.models.ninja import Ninja
from models import app

@app.route('/dojos')
def dojos():
    return render_template('dojo.html', dojos=Dojo.get_all())

@app.route('/dojos', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = Dojo.get_with_ninjas(dojo_id)
    return render_template('show_dojo.html', dojo=dojo)

@app.route('/ninjas')
def ninjas():
    ninjas = Dojo.get_all()
    return render_template('ninja.html', ninjas=ninjas)

@app.route('/ninjas', methods=['POST'])
def creat_ninja():
     Ninja.save(request.form)
     return redirect(f"/dojos/{request.form['dojo_id']}")