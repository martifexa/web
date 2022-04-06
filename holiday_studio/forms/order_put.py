from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FloatField, SelectField
from wtforms.validators import DataRequired, optional
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Order, create_session


def all_orders():
    session = create_session()
    orders = session.query(Order).all()
    return orders


class PutOrderForm(FlaskForm):
    order_list = QuerySelectField("Заказ",
                                   query_factory=all_orders,
                                   get_pk=lambda order: order.id,
                                   get_label=lambda order: order.title)
    price = FloatField("Цена заказа", validators=[DataRequired()])
    title = StringField("Название заказа", validators=[DataRequired()])
    describtion = StringField("Описание заказа", validators=[DataRequired()])
    submit = SubmitField("Изменить")
