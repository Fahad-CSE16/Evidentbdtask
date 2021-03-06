# Evidentbd Task Evaluation
## Run using Docker
### install docker and docker-compose (manually start docker if os=windows)

and then run these command

```
docker-compose build
docker-compose up
```

##### To migrate and createsuperuser , in another terminal
```
docker ps
```
copy the container name and 
```
docker exec containername python manage migrate
docker exec -it containername python manage createsuperuser 
```

### Steps to Run Without Docker
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

Create User and Database on Postgresql similar as projects settings.py DATABASE Settings and change DATABASE Settings

`'HOST': 'db'` to `'HOST': 'localhost'`

##### Step 4

run 
```
python manage.py migrate
python manage.py runserver
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

{"status":"success","user_id":"1","payload":[{"timestamp":"2021-09-23 17:57:51","input_values":"4, 3, 2, 1"},{"timestamp":"2021-09-23 17:58:36","input_values":"11, 10, 9, 7, 5, 1, 0"},{"timestamp":"2021-09-23 17:58:59","input_values":"11, 10, 9, 7, 5, 1, 0"}]}
