from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class QuickForm(FlaskForm):
    name=StringField("Name")
    age=IntegerField("Age")
    submit=SubmitField("Submit")
