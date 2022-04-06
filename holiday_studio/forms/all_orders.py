from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Order, create_session


def all_orders():
    session = create_session()
    orders = session.query(Order).all()
    return orders


class GetAllOrdersForm(FlaskForm):
    order_list = QuerySelectField("Заказы",
                                   query_factory=all_orders,
                                   get_pk=lambda order: order.id,
                                   get_label=lambda order: order.title)