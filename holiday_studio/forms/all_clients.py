from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Client, create_session


def all_clients():
    session = create_session()
    clients = session.query(Client).all()
    return clients


class GetAllClientsForm(FlaskForm):
    client_list = QuerySelectField("Клиенты",
                                   query_factory=all_clients,
                                   get_pk=lambda client: client.id,
                                   get_label=lambda client: client.full_name)