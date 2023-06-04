#Python REST API
...
## Rest app with flask

this project is a starter app for makin a crud api:

1)install latest python from www.python.org
2)initial virtual environnement

    -python3.11 -m venv .venv
        (ask python use venv module pour creer environnement      virtuel .venv)
    -[cmd][shift][p] Python: Select interpreter 
        (tell vscode which virtual env to use select the one we just  created)

2)install flask

    -pip install flask
        (install flask inside the virtual .venv create app.py with Flask boilerplate then create the endPoint for the app)
    -flask run 
        (flask run will look for a file call app.py then inside the app.py it will look for an app variable then flask run will make those endpoints available for a client which gonna his requests to the flask server address )
    -[ctrl+ c]
        (close the app)