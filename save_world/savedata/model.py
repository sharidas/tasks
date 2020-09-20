"""
The model for users who save th world resides here
"""

from flask import current_app


class UserSave(current_app.db.Model):
    """
    Our model for the app
    """
    __tablename__ = "savedata"

    db = current_app.db

    id = db.Column(db.Integer, primary_key=True)
    when_saved = db.Column(db.DateTime, unique=False, nullable=False)
    how_saved = db.Column(db.UnicodeText, unique=True, nullable=False)
    thanks = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return '<how_saved {}>'.format(self.how_saved)
