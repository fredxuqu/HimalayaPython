"""
    create by Fred on 2018/8/22
"""

__author__ = 'Fred'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


# use wtforms to validate the inputted data
class DemoForm(Form):
    username = StringField(validators=[DataRequired(), Length(min=1, max=30)], default='')
    #age = IntegerField(validators=[NumberRange(min=1, max=99)], default=10)
    email = StringField(validators=[DataRequired(), Length(min=1, max=100)], default='')