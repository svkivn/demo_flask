import os
basedir = os.path.abspath(os.path.dirname(__file__))

# General Config
WTF_CSRF_ENABLED = True
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

# Database
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance\\site4.db')