from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Client, create_session


def all_clients():
    session = create_session()
    clients = session.query(Client).all()
    return clients


class DeleteClientForm(FlaskForm):
    client_list = QuerySelectField("Выберите клиента",
                                   query_factory=all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name)
    submit = SubmitField("Удалить")
