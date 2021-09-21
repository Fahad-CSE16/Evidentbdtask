# Evidentbd Task Evaluation

### Steps to Run 
##### Step 1

Clone The repository and Create Virtual envronment
```
python -m venv venv
venv/Scripts/activate
```
In Case of Ubuntu OS
```
virtualenv venv
source venv/bin/activate
```
##### Step 2

Install all the packages from requirements.txt 

```
pip install -r requirements.txt
```
##### Step 3

Create User and Database on Postgresql similar as projects settings.py DATABASE Settings 

or 

Simply comment postgresql settings portion and uncomment sqlite3 settings portion

##### Step 4

run 
```
python manage.py migrate
python manage.py runserver
```
