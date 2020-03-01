First step. Create a virtual environment through anaconda. conda create -n flask_app python=3.7.3

Install all the dependencies in your application pip install -r requirements.txt (when is available) dependencies is are all the pip libraries needed eg. flask, sqlalchemy. 2a. To generate requirements.text run pip freeze >> requirements.txt run this anytime you run a new library.

Export Flask app.

export FLASK_APP=flask_app.py and then flask run# hw4-beer-app