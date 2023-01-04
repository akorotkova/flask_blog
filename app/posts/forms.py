from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Название поста: ', validators=[DataRequired()])
    content = TextAreaField('Содержание поста: ', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
