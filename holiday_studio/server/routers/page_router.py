import sqlalchemy
from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from forms.create_client import CreateClientForm
from forms.create_order import CreateOrderForm
from forms.all_clients import GetAllClientsForm
from forms.all_orders import GetAllOrdersForm
from forms.client_del import DeleteClientForm
from forms.client_put import PutClientForm
from forms.order_put import PutOrderForm
from forms.order_del import DeleteOrderForm
from forms.login import LoginForm
from models import AlchemyEncoder, Employee, Client, EmployeeOrder, ClientOrder
from models import Order, create_session
import json
# from flask_login import current_user

router = Blueprint("",
                   __name__,
                   template_folder="/server/templates")


@router.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session = create_session()
        employee = session.query(Employee).\
            filter(Employee.email == login_form.email.data).first()
        if employee and employee.check_password(login_form.password.data):
            login_user(employee)
            session.close()
            return redirect("/")
        else:
            session.close()
            return redirect("/site/login")
    return render_template("login.html", title="Авторизация", form=login_form)


@router.route("/create_client", methods=["GET", "POST"])
@login_required
def create_client():
    create_client_form = CreateClientForm()
    if create_client_form.validate_on_submit():
        session = create_session()
        client = Client(full_name=create_client_form.full_name.data,
                        age=create_client_form.age.data,
                        phone=create_client_form.phone.data,
                        email=create_client_form.email.data)
        session.add(client)
        try:
            session.commit()
            session.close()
            return redirect("/")
        except IntegrityError:
            create_client_form.email.errors.append("Email уже используется")
            session.close()
            return render_template("create_client.html", title="Создание клиента", form=create_client_form)

    return render_template("create_client.html", title="Создание клиента", form=create_client_form)


@router.route("/create_order", methods=["GET", "POST"])
@login_required
def create_order():
    create_order_form = CreateOrderForm()
    if create_order_form.validate_on_submit():
        client = create_order_form.client_list.data
        session = create_session()
        order = Order(price=create_order_form.price.data,
                      title=create_order_form.title.data,
                      describtion=create_order_form.describtion.data)
        # чтобы получить order_id сначала добавим в базу
        session.add(order)
        session.commit()

        # связываем M:M
        employee_order = EmployeeOrder(id_employee=current_user.id,
                                       id_order=order.id)
        client_order = ClientOrder(id_client=client.id,
                                   id_order=order.id)

        session.add(client_order)
        session.add(employee_order)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("create_order.html", title="Создание заказа", form=create_order_form)


@router.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@router.route("/all_clients")
@login_required
def all_clients():
    all_clients_form = GetAllClientsForm()
    return render_template('all_clients.html', form=all_clients_form)


@router.route("/all_orders")
@login_required
def all_orders():
    all_orders_form = GetAllOrdersForm()
    return render_template('all_orders.html', form=all_orders_form)


@router.route("/put_client", methods=["GET", "POST"])
@login_required
def put_client():
    put_client_form = PutClientForm()
    if put_client_form.validate_on_submit():
        session = create_session()
        client = put_client_form.client_list.data
        client = session.query(Client).get(client.id)
        client.full_name = put_client_form.full_name.data
        client.age = put_client_form.age.data
        client.phone = put_client_form.phone.data
        client.email = put_client_form.email.data
        session.add(client)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("client_put.html", title="Изменение клиента", form=put_client_form)


@router.route("/put_order", methods=["GET", "POST"])
@login_required
def put_order():
    put_order_form = PutOrderForm()
    if put_order_form.validate_on_submit():
        session = create_session()
        order = put_order_form.order_list.data
        order = session.query(Order).get(order.id)
        order.price = put_order_form.price.data
        order.title = put_order_form.title.data
        order.describtion = put_order_form.describtion.data
        session.add(order)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("order_put.html", title="Изменение клиента", form=put_order_form)


@router.route("/delete_client", methods=["POST", "GET"])
@login_required
def delete_client():
    delete_client_form = DeleteClientForm()
    session = create_session()
    if delete_client_form.validate_on_submit():
        client = delete_client_form.client_list.data
        client_to_delete = session.query(Client).get(client.id)
        if client_to_delete:
            session.delete(client_to_delete)
            session.commit()
        clients_orders = session.query(ClientOrder).all()
        clients_orders = json.loads(json.dumps(clients_orders, cls=AlchemyEncoder, ensure_ascii=False))
        client_order_ids = []
        for elem in clients_orders:
            if elem["id_client"] == client.id:
                client_order_ids.append(elem["id"])
        if client_order_ids:
            for id in client_order_ids:
                client_order_to_delete = session.query(ClientOrder).get(id)
                session.delete(client_order_to_delete)
                session.commit()
        session.close()
        return redirect("/")
    return render_template("client_delete.html", form=delete_client_form)


@router.route("/delete_order", methods=["POST", "GET"])
@login_required
def delete_order():
    delete_order_form = DeleteOrderForm()
    if delete_order_form.validate_on_submit():
        session = create_session()
        order = delete_order_form.order_list.data
        order = session.query(Order).get(order.id)
        session.delete(order)
        session.commit()
        clients_orders = session.query(ClientOrder).all()
        clients_orders = json.loads(json.dumps(clients_orders, cls=AlchemyEncoder, ensure_ascii=False))
        employee_order = session.query(EmployeeOrder).all()
        employee_order = json.loads(json.dumps(employee_order, cls=AlchemyEncoder, ensure_ascii=False))
        client_order_id = []
        employee_order_id = []
        for elem in clients_orders:
            if elem["id_order"] == order.id:
                client_order_id.append(elem["id"])
        for elem in employee_order:
            if elem["id_order"] == order.id:
                employee_order_id.append(elem["id"])
        for id in client_order_id:
            client_order_to_delete = session.query(ClientOrder).get(id)
            session.delete(client_order_to_delete)
            session.commit()
        for id in employee_order_id:
            employee_order_to_delete = session.query(EmployeeOrder).get(id)
            session.delete(employee_order_to_delete)
            session.commit()
        session.close()
        return redirect("/")
    return render_template('order_delete.html', form=delete_order_form)