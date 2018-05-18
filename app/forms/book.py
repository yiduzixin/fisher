"""
Created by 逗蛆 on 2018/5/8

"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import NumberRange, Length, DataRequired

__author__ = "逗蛆"


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
