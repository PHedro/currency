### Usage:
Install Python 3.8.5 or greater, you can do it via pyenv https://github.com/pyenv/pyenv#installation and virtualenv
```commandline
pyenv install 3.8.5
pyenv virtualenv 3.8.5 currency
```
Activate the virtualenv
```commandline
pyenv activate currency
```
Clone the project
```commandline
git clone git@github.com:PHedro/currency.git
```
Go to the project folder (the one where you can find the README file)
```commandline
cd /path/to/project/ 
```
Install the project requirements (remember to activate the virtualenv)
```commandline
pip install -r requirements.txt
```

Running tests, from the project folder (the one containing README.md):
```commandline
python -m unittest discover -v 
```
