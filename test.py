from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')

beer_name = 'Amstel'
db = SQLAlchemy(app, session_options={'autocommit': False})
results=db.session.query(models.Bar, models.Serves).join(models.Bar.name== models.Serves.bar).filter(models.Serves.beer == beer_name).all()

for row in results: 
	print(row)