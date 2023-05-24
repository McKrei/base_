from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Optional

from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField('Категория', choices=get_categories, validators=[Optional()])
    submit = SubmitField('Добавить')


class EnterEmail(FlaskForm):
    email = EmailField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    submit = SubmitField('Поиск')

class SearchForm(FlaskForm):
    qeury = StringField(
        'Запрос',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    submit = SubmitField('Поиск')
