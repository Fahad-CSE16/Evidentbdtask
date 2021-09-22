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


## Run using Docker

### Step 1

run postgresql 
```
sudo systemctl start postgresql
sudo systemctl enable postgresql
```
### step 2  install docker and docker-compose (manually start docker if os=windows)

and then run these command

```
docker-compose build
docker-compose up
```


# API Documentation

## API 1.1  Get All Input Values
This API don't receives user credentials, it will allow anyone to get data

<b> URL: </b>http://127.0.0.1:8000/khoj/api/

<b> Method: </b> “POST”
Fields : “start_datetime”, ”end_datetime”, "user_id"


<b>API Payload Field Definitions: </b>

user_id: just pass integer value like 1 or 2 (type: Integer)

start_datetime: format='%Y-%m-%d %H:%M:%S'  example:'2021-09-21 19:12:11'  (Type: Text)

end_datetime: format='%Y-%m-%d %H:%M:%S' example:'2021-09-21 19:12:11' (Type: Text)

Response:
{"status":"success","user_id":"1","payload":[{"input_values":"['4', '3', '2', '1']","timestamp":"2021-09-21T19:12:11.867663+06:00"},{"input_values":"['6', '5', '4', '2', '1', ' 3', '', '', '', '']","timestamp":"2021-09-21T19:51:54.456657+06:00"}]}
