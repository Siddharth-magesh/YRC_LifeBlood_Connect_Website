from flask import Blueprint,flash,render_template,url_for,session,redirect,request
from werkzeug.security import generate_password_hash,check_password_hash
from ..models import *
from ..extensions import db
from ..helper import *
import os,math
from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import pandas as pd
import string,random

# The line `admin = Blueprint("admin",__name__,url_prefix="/admin")` in the code snippet is creating a
# Blueprint object named "admin" in the Flask application.
admin = Blueprint("admin",__name__,url_prefix="/admin")

# This class represents a form in a Flask application for adding donor details by uploading a file.
class AddDonorDetails(FlaskForm):
    new_donor_file = FileField("Donor Details File",validators=[InputRequired()])
    submit = SubmitField("Add")

def add_address(path,address_ids):
    """
    The function `add_address` reads address information from a CSV file and adds it to a database using
    SQLAlchemy.
    
    :param path: The `path` parameter in the `add_address` function is the file path to the CSV file
    containing donor information such as current address, city, pin code, and state. This function reads
    the CSV file, extracts the relevant columns for address information, and then adds each donor's
    address to a
    :param address_ids: The `address_ids` parameter in the `add_address` function is a list of unique
    identifiers for each address. These identifiers will be used to create new `Address` objects in the
    database with corresponding IDs
    """
    csvFile = pd.read_csv(path)
    donors_address = csvFile["Current Address:"]
    donors_city = csvFile["City:"]
    donors_pinCode = csvFile["Pin-code:"]
    donors_state = csvFile["State:"]
    for i in range(len(address_ids)):
        new_donor_address = Address(
            address_id = address_ids[i],
            pincode = int(donors_pinCode[i]),
            state = donors_state[i],
            city = donors_city[i],
            address = donors_address[i]
        )
        db.session.add(new_donor_address)
        db.session.commit()

def add_disease(path,disease_ids):
    """
    The function `add_disease` reads a CSV file, extracts disease information, replaces any missing
    values, and adds the diseases to a database with corresponding disease IDs.
    
    :param path: The `path` parameter in the `add_disease` function is the file path to a CSV file that
    contains information about diseases or allergies. This function reads the CSV file, extracts the
    disease information, and adds it to a database along with the corresponding disease IDs provided in
    the `disease_ids
    :param disease_ids: The `disease_ids` parameter in the `add_disease` function is a list of unique
    identifiers for diseases that you want to add to the database. Each identifier in the list
    corresponds to a specific disease entry in the CSV file that you are reading
    """
    csvFile = pd.read_csv(path)
    diseases = csvFile['Any Disease or Allergies : ']
    replaced_diseases = [replace_none(str(text)) for text in diseases]
    for i in range(len(disease_ids)):
        new_donor_disease = Disease(
            disease_id = disease_ids[i],
            disease = replaced_diseases[i]
        )
        db.session.add(new_donor_disease)
        db.session.commit()


@admin.route("/",methods=['GET', 'POST'])
def login():
    """
    The `login` function checks if the user's login credentials are valid and redirects to the admin
    dashboard if successful.
    :return: The `render_template("admin/index.html")` function is being returned if the request method
    is not "POST" or if the username and password do not match during the login process.
    """
    if request.method == "POST":
        session.permanent=True
        username,passwd = request.form["adminName"],request.form["adminPass"]
        user = db.session.query(Admin).filter(Admin.admin_username == username).first()
        if user is not None:
            if check_password_hash(user.admin_password,passwd):
                session['adminLogin'] = True
                session['adminName'] = username
                return redirect(url_for("admin.dashboard"))
            else:
                flash("Username or password doesn't exists!")
        else:
            flash("User doesn't exist!")
    return render_template("admin/index.html")

@admin.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == "POST":
        username,email,passwd,repasswd = request.form['adminName'],request.form['adminEmail'],request.form['adminPass'],request.form['adminRePass']
        if not db.session.query(Admin).filter_by(admin_username=username).scalar():
            if repasswd == passwd:
                hashed_passwd = generate_password_hash(passwd,method="pbkdf2:sha256")
                try:
                    admin_id = "AM"+"".join(random.sample(string.ascii_uppercase+string.digits,k=6))
                    new_admin = Admin(
                        admin_id = admin_id,
                        admin_name = email,
                        admin_username = username,
                        admin_password = hashed_passwd
                    )
                    db.session.add(new_admin)
                    db.session.commit()
                except Exception as e:
                    flash(e)
            else:
                flash("Passwords doesn't match!")
        else:
            flash("Username already exists!")
    return render_template("admin/index.html")

@admin.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if session['adminName'] is not "":
        username = session.get('adminName')
        return f"<h1> Welcome {username}! </h1>"
    else:
        return redirect(url_for("admin.login"))

@admin.route("/add_donor_details",methods=['GET','POST'])
def add_donor_csv():
    """
    The `add_donor_csv` function reads donor details from a CSV file, processes the data, and adds the
    donor information to a database.
    :return: The function `add_donor_csv()` returns a rendered template "admin/donor_details.html" with
    the form data if the request method is POST and the form is validated successfully. If there is an
    exception during the processing of the CSV file data, an error message is flashed.
    """
    form = AddDonorDetails()
    if request.method == 'POST':
        if form.validate_on_submit():
            csv_file = form.new_donor_file.data
            csv_filename = secure_filename(csv_file.filename)
            csv_file.save(os.path.join(os.path.abspath("app/static/files/"),csv_filename))
            try:
                csvFile = pd.read_csv(os.path.join(os.path.abspath("app/static/files/"),csv_filename))
                first_names = csvFile["First Name: "]
                last_names = csvFile["Last Name or Initial : "]
                donor_names = [f"{first.strip()} {last.strip()}" for first, last in zip(first_names, last_names)]
                donors_age = csvFile["Age:"]
                donors_blood_grp = csvFile["Blood Group:"]
                donors_dob = convert_to_date(csvFile["Date of Birth:"])
                donors_status = csvFile["Status:"]
                donors_contact_no = csvFile["Personal Contact Number:"]
                # blood_donated = csvFile["Donated Blood Already :"]
                blood_donated_dates = csvFile["Last Blood Donated Date:"]
                blood_donated_times = [0 if math.isnan(x) else int(x) for x in csvFile['No. of times donated:'].tolist()]
                address_ids = ["AD"+"".join(random.sample(string.ascii_uppercase+string.digits,k=6)) for i in range(len(donor_names))]
                unique_ids = ["U"+"".join(random.sample(string.ascii_uppercase+string.digits,k=7)) for i in range(len(donor_names))]
                disease_ids = ["D"+"".join(random.sample(string.ascii_uppercase+string.digits,k=7)) for i in range(len(donor_names))]
                last_donated = convert_to_date(blood_donated_dates)
                # Adding Address to DB 
                add_address(os.path.join(os.path.abspath("app/static/files/"),csv_filename),address_ids)
                # Adding Disease details to DB
                add_disease(os.path.join(os.path.abspath("app/static/files/"),csv_filename),disease_ids)
                # Adding other donar details to DB
                for i in range(len(unique_ids)):
                    new_donor = Donor(
                        unique_id = unique_ids[i],
                        Name = donor_names[i],
                        age = int(donors_age[i]),
                        blood_grp = donors_blood_grp[i],
                        DOB = donors_dob[i],
                        address_id = address_ids[i],
                        no_of_times_donated = blood_donated_times[i],
                        disease_id = disease_ids[i],
                        last_donated_date = last_donated[i],
                        status = donors_status[i],
                        contact_no = str(donors_contact_no[i])
                    )
                    db.session.add(new_donor)
                    db.session.commit()
                flash("Details added successfully!")
            except Exception as e:
                flash(e)
    return render_template("admin/donor_details.html",form=form)