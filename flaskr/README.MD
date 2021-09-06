*****create environment
py -3 -m venv venv

****** activate environment
venv\Scripts\activate

***** install flask

pip install Flask

$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run