"""Data models."""
from . import db, bcrypt
from datetime import datetime as dt


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')

    posts = db.relationship('Post', backref='author', lazy=True)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    @property
    def password_hash(self):
        print("get hash")
        return self.password

    @password_hash.setter
    def password_hash(self, plain_text_password):
        print("set hash")
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def verify(self, password):
        if not self.password or not password:
            return False
        return bcrypt.check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = dt.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"




#
#
# from datetime import datetime
# import enum
#
# class EnumPriority(enum.Enum):
#     low = 1
#     medium = 2
#     high = 3
#
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     created = db.Column(db.DateTime, default=datetime.utcnow)
#     # priority = db.Column(db.Enum('low', 'medium', 'high'), nullable=False)
#     priority = db.Column(db.Enum(EnumPriority), default='low')
#     is_done = db.Column(db.Boolean, default=False)
#
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     category = db.relationship('Category', backref='tasks', lazy='dymamic')
#
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     #tasks =db.relationship('Task', backref='category', lazy='dymamic')
#
#
#     def __repr__(self):
#         return f"Category('{self.id}', '{self.name}')"
#









'''
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(32),unique=True)
    surname = db.Column(db.String(32),unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    """Data model for user accounts."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    def __repr__(self):
        return f"<User {self.username}>"
'''
