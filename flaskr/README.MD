*****create environment
py -3 -m venv venv

****** activate environment
venv\Scripts\activate

***** install flask

pip install Flask

# Power Shell
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

# Bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development


flask run