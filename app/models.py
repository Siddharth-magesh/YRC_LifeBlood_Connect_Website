# `from .extensions import db` is importing the `db` object from the `extensions` module in the
# current package or directory. This `db` object is likely an instance of a SQLAlchemy `Database`
# class that is used to interact with the database in the application.
from .extensions import db

# This Python class represents an Address entity with attributes such as address_id, pincode, country,
# state, city, and address.
class Address(db.Model):
    __tablename__ = 'Address_ID'
    address_id = db.Column(db.String(10), primary_key=True)
    pincode = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(20))
    state = db.Column(db.String(25))
    city = db.Column(db.String(25))
    address = db.Column(db.String(225))

    def __init__(self, address_id, pincode, country=None, state=None, city=None, address=None):
        self.address_id = address_id
        self.pincode = pincode
        self.country = country
        self.state = state
        self.city = city
        self.address = address

# This Python class represents a Disease entity with attributes for disease ID and disease name.
class Disease(db.Model):
    __tablename__ = 'Disease_ID'
    disease_id = db.Column(db.String(10), primary_key=True)
    disease = db.Column(db.String(200))

    def __init__(self, disease_id, disease):
        self.disease_id = disease_id
        self.disease = disease

# This Python class defines an Admin model with attributes for admin ID, name, username, password, and
# last login timestamp.
class Admin(db.Model):
    __tablename__ = 'admin_table'
    admin_id = db.Column(db.String(10), primary_key=True)
    admin_email = db.Column(db.String(100))
    admin_username = db.Column(db.String(100), nullable=False)
    admin_password = db.Column(db.String(500), nullable=False)
    last_login = db.Column(db.DateTime)

    def __init__(self, admin_id, admin_name, admin_username, admin_password, last_login=None):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.last_login = last_login

# This class represents a VictimRequest entity with attributes such as request_id, name, age, blood
# group, admitted hospital, contact number, attendant name, hospital address, due date, reason,
# status, donor name, and donor ID.
class VictimRequest(db.Model):
    __tablename__ = 'victim_request'
    request_id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    blood_grp = db.Column(db.String(10), nullable=False)
    admitted_hospital = db.Column(db.String(100),nullable = False)
    contact_number = db.Column(db.Integer)
    attendant_name = db.Column(db.String(100),nullable = False)
    hospital_address = db.Column(db.String(200),nullable = False)
    due_date = db.Column(db.Date)
    reason = db.Column(db.String(150))
    status = db.Column(db.String(25))
    donor_name = db.Column(db.String(100))
    donar_id = db.Column(db.String(10))

    def __init__(self, request_id, name, age, blood_grp, admitted_hospital, contact_number=None,
                 attendant_name=None, hospital_address=None, due_date=None, reason=None, 
                 status=None, donor_name=None, donor_id=None):
        self.request_id = request_id
        self.name = name
        self.age = age
        self.blood_grp = blood_grp
        self.admitted_hospital = admitted_hospital
        self.contact_number = contact_number
        self.attendant_name = attendant_name
        self.hospital_address = hospital_address
        self.due_date = due_date
        self.reason = reason
        self.status = status
        self.donor_name = donor_name
        self.donor_id = donor_id

# This class defines a Donor entity with attributes such as unique_id, Name, age, blood_grp, DOB,
# address_id, no_of_times_donated, disease_id, last_donated_date, and relationships with Address and
# Disease entities.
class Donor(db.Model):
    __tablename__ = 'donars_table'
    unique_id = db.Column(db.String(15), primary_key=True)
    Name = db.Column(db.String(100))
    age = db.Column(db.Integer, nullable=False)
    blood_grp = db.Column(db.String(10), nullable=False)
    DOB = db.Column(db.Date, nullable=False)
    address_id = db.Column(db.String(15), db.ForeignKey('Address_ID.address_id'),nullable=False)
    no_of_times_donated = db.Column(db.Integer)
    disease_id = db.Column(db.String(15), db.ForeignKey('Disease_ID.disease_id'))
    last_donated_date = db.Column(db.Date)
    status = db.Column(db.String(20),nullable=False)
    contact_no = db.Column(db.String(20),nullable=False)
    address = db.relationship('Address', backref=db.backref('donors', lazy=True))
    disease = db.relationship('Disease', backref=db.backref('donors', lazy=True))

    def __init__(self, unique_id, name, age, blood_grp, dob, address_id, no_of_times_donated=None, 
                 disease_id=None, last_donated_date=None, status=None, contact_no=None):
        self.unique_id = unique_id
        self.name = name
        self.age = age
        self.blood_grp = blood_grp
        self.dob = dob
        self.address_id = address_id
        self.no_of_times_donated = no_of_times_donated
        self.disease_id = disease_id
        self.last_donated_date = last_donated_date
        self.status = status
        self.contact_no = contact_no