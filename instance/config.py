import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                           'sqlite:///' + os.path.join(basedir, 'site4.db')


#https://uniwebsidad.com/libros/explore-flask/chapter-5/the-simple-case\
#https://stackoverflow.com/questions/65621720/where-does-flask-look-to-find-config-files-when-using-flask-config-from-object