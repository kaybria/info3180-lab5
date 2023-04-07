# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime


class Movie(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    poster = db.Column(db.String(300))
    created_at = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)

    def __init__(self, title, description, poster,created_at):
        self.title = title
        self.description=description
        self.poster = poster
        self.created_at = created_at

     
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Movie %r>' % (self.title)