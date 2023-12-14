from app import database
from werkzeug.security import generate_password_hash, check_password_hash


class Vehicles(database.Model):
    __tablename__ = "vehicle"

    id = database.Column(database.Integer, primary_key=True)
    brand = database.Column(database.String(100), nullable=False)
    model = database.Column(database.String(100), nullable=False)
    category = database.Column(database.String(50), nullable=False)
    type = database.Column(database.String(10), nullable=False)  # Car or Motorcycle
    people_quantity = database.Column(database.Integer)
    image_url = database.Column(database.String(255))  # Address Image
    daily_value = database.Column(database.Float, nullable=False)
    last_revision_date = database.Column(database.Date)
    next_revision_date = database.Column(database.Date)
    last_legalization_date = database.Column(database.Date)
    available = database.Column(database.Boolean, default=True)


class Client(database.Model):
    __tablename__ = "client"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    phone = database.Column(database.String(15))
    user = database.Column(database.String(50), unique=True, nullable=False)
    password_hash = database.Column(database.String(128), nullable=False)
    reserves = database.relationship('Reservation', backref='client', lazy=True)

    def __init__(self, name, email, phone, user, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.user = user
        self.set_password(password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Reservation(database.Model):
    __tablename__ = "reservation"

    id = database.Column(database.Integer, primary_key=True)
    start_date = database.Column(database.Date, nullable=False)
    end_date = database.Column(database.Date, nullable=False)
    vehicle_id = database.Column(database.Integer, database.ForeignKey('vehicle.id'), nullable=False)
    client_id = database.Column(database.Integer, database.ForeignKey('client.id'), nullable=False)
    payment_method_id = database.Column(database.Integer, database.ForeignKey('payment_method.id'), nullable=False)


class PaymentMethod(database.Model):
    __tablename__ = "payment_method"

    id = database.Column(database.Integer, primary_key=True)
    payment_name = database.Column(database.String(50), nullable=False, unique=True)
    description = database.Column(database.String(200))
    reservations = database.relationship('Reservation', backref='payment_method', lazy=True)
