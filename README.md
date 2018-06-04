# Minibank Challenge

A Restful application with event sourcing 


### Prerequisites

```
Python==2.7
Flask==0.12.2
Flask-RESTful==0.3.6
psycopg2
PostgreSQL10 
```

### Installing

All these prerequisites can be installed using pip, except PostgreSQL10 and Python

```
Using pip: pip install Flask-RESTful
```

And repeat

```
until finished
```

After installing Postgre create a sample database named 'minibank'.
Then execute the following script to create a event table:
```
CREATE TABLE EVENTS (
	id serial primary key,
    id_event UUID not null,
    version integer not null,
    data bytea not null
)
```

## Running the tests

On the folder root execute the unitTests.py file.

```
python unitTests.py
```


## Deployment
To run a server execute the app.py file.

```
python app.py
```
The server will start and then the following message will appear in the terminal.

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

That's indicating the server is working.


## Running API
To call a service from this API, you can call like this

```
curl -d "{\"name\":\"value1\", \"email\":\"value2\"}" -H "Content-Type: application/json" -X POST http://localhost:5000/client
```
The command above will create a new client into the app. The return will something like: "/client/31fb57b4-1fe3-4254-8401-7f70e7a5daad".
That's return is a link to get the informations about the client.

To get the client created
```
curl -H "Content-Type: application/json" -X GET http://localhost:5000/client/31fb57b4-1fe3-4254-8401-7f70e7a5daad
```

### Others services
Here is a list of all urls in this API

This will create a new account to previous client.
The client_id parameter is an id of a valued client.

```
curl -d "{\"client_id\":\"31fb57b4-1fe3-4254-8401-7f70e7a5daad\"}" -H "Content-Type: application/json" -X POST http://localhost:5000/account
```

To get an account.

```
curl -H "Content-Type: application/json" -X GET http://localhost:5000/account/f298a359-3459-4e49-a02b-ac2770a80ab8
```

To make some deposits.

```
curl -d "{\"amount\":2000.00}" -H "Content-Type: application/json" -X POST http://localhost:5000/account/f298a359-3459-4e49-a02b-ac2770a80ab8/deposit
```

To make some withdrawals.

```
curl -d "{\"amount\":2000.00}" -H "Content-Type: application/json" -X POST http://localhost:5000/account/f298a359-3459-4e49-a02b-ac2770a80ab8/withdrawal
```

To show the history account.

```
curl  -H "Content-Type: application/json" -X GET http://localhost:5000/account/f298a359-3459-4e49-a02b-ac2770a80ab8/history
```


### Notes

To send emails to each created account, it is necessary to uncomment the line 'self.send_email (account.id)' in the accountService.py file and perform the proper configuration, email, password and recipients in the 'def send_email (self, account) '.



