test project

# Prerequisites
python 3

# Requirements
aniso8601==8.0.0
click==7.1.2
Flask==1.1.2
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.3
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
pytz==2020.1
six==1.15.0
SQLAlchemy==1.3.18
Werkzeug==1.0.1

# Virtual Env Setup
## windows setup:

to set up the virtual env run (replace the fp below with the location of your local python 3.6 installation): `virtualenv . -p C:/Users/PC/AppData/Local/Programs/Python/Python36/python.exe`

to run the virtualenv, run: `./Scripts/activate`

to deactivate, run: `deactivate`

## macos setup: 

to set up the virtual env run: `virtualenv venv`

if you want your virtualenv to inherit globally installed packages, run: `virtualenv venv --system-site-packages`

to run the virtualenv, run: `source venv/bin/activate`

to deactivate, run: `deactivate`

# Instructions