#.
#imprt_db

from . import db

#imprt_UsrMixn

from flask_login import UserMixin

#frm_sqlalchmy
#imprt_functions

from sqlalchemy.sql import func

#class
#class1

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #column_key
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    @usrid_variable
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    
#clss2
#class_user_model
#,

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
#email_id
    email = db.Column(db.String(150), unique=True)
#psswrd
    password = db.Column(db.String(150))
#frst_nam_e
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

    #.
    
