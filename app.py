from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models
import forms

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

@app.route('/')
def all_drinkers():
    drinkers = db.session.query(models.Drinker).all()
    return render_template('all-drinkers.html', drinkers=drinkers)

@app.route('/drinker/<name>')
def drinker(name):
    drinker = db.session.query(models.Drinker)\
                        .filter(models.Drinker.name == name).one()
    return render_template('drinker.html', drinker=drinker)

@app.route('/edit-drinker/<name>', methods=['GET', 'POST'])
def edit_drinker(name):
    drinker = db.session.query(models.Drinker)\
                        .filter(models.Drinker.name == name).one()
    beers = db.session.query(models.Beer).all()
    bars = db.session.query(models.Bar).all()
    form = forms.DrinkerEditFormFactory.form(drinker, beers, bars)
    if form.validate_on_submit():
        try:
            form.errors.pop('database', None)
            models.Drinker.edit(name, form.name.data, form.address.data,
                                form.get_beers_liked(), form.get_bars_frequented())
            return redirect(url_for('drinker', name=form.name.data))
        except BaseException as e:
            form.errors['database'] = str(e)
            return render_template('edit-drinker.html', drinker=drinker, form=form)
    else:
        return render_template('edit-drinker.html', drinker=drinker, form=form)

@app.route('/serves', methods=['GET', 'POST'])
def serves():
    beer_names = db.session.query(models.Beer.name) 
    dropdown_list = []
    for beer in beer_names:
        dropdown_list.append(beer[0])
    form = forms.ServingsFormFactory.form(dropdown_list)
    if form.validate_on_submit():
        return redirect('/servings/' + form.beer_sel.data) # not sure if this is right
    return render_template('serves.html', dropdown_list=dropdown_list, form=form)

@app.route('/servings/<beer_name>', methods=['GET', 'POST'])
def servings_for(beer_name):
    results=db.session.query(models.Bar, models.Serves).filter(models.Serves.beer == beer_name).join(models.Bar, models.Bar.name==models.Serves.bar).all()
    return render_template('servings_for.html', 
                            beer_name=beer_name,
                            data=results)

@app.template_filter('pluralize')
def pluralize(number, singular='', plural='s'):
    return singular if number in (0, 1) else plural


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
