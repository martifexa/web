from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TelField, EmailField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

from models import Client, create_session


def all_clients():
    session = create_session()
    clients = session.query(Client).all()
    return clients


class PutClientForm(FlaskForm):
    client_list = QuerySelectField("Клиент",
                                   query_factory=all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name)
    full_name = StringField("Имя клиента", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[])
    phone = TelField("Номер телефона", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Изменить")
