<!-- setup venv named venv and activate that venv and then do pip3 install -r requirements.txt


activate pipenv by using pipenv shell command
and after that run command pipenv install to get all the dependencies from Pipfile.lock so that what we have done using requirements.txt will get fullfilled instead of using requirements.txt -->

pipenv install
pipenv run python3 scrb/app.py
pipenv run python3 dodone/app.py

