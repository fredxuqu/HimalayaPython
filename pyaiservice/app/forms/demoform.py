"""
    create by Fred on 2018/8/22
"""

__author__ = 'Fred'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class DemoForm(Form):
    userid = StringField(validators=[DataRequired(), Length(min=1, max=3)], default=1)
    #age = IntegerField(validators=[NumberRange(min=1, max=99)], default=10)
    username = StringField(validators=[DataRequired(), Length(min=1, max=30)], default='')