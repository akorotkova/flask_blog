from time import time
import jwt
from datetime import datetime
from . import db, login_manager
from flask import current_app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_seconds=600):
        token = jwt.encode(
                {'user_id': self.id, 'exp': time() + expires_seconds},
                  current_app.config['SECRET_KEY'], algorithm='HS256')
        return token
    
    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f'(User: name - {self.username}, email - {self.email}, image_file - {self.image_file})'

        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'(Post: title - {self.title}, date_posted - {self.date_posted})'
