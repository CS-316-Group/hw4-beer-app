from flask import Flask, request, redirect, url_for
from flask import render_template
from database import db

app = Flask(__name__)


@app.route('/serves', methods=['GET', 'POST'])
def serves():
	beer_names = @TODO
	form = forms.ServingsFormFactory.form( @TODO )
	if form.@TODO():
		return @TODO('/servings/' + form.beer_sel.data)
	return render_template('serves.html', form=form)

@app.route('/servings/<beer_name>')
def servings_for(beer_name):
	results = db.session.query(models.Serves, models.Bar) \
				.filter(@TODO) \
				.join(@TODO).all()
	return render_template('servings_for.html', beer_name=beer_name,
							data=results)