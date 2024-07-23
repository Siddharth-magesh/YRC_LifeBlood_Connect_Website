from flask import Blueprint,flash,render_template,url_for,session,redirect,request

main = Blueprint("main",__name__)

@main.route("/home",methods=["GET","POST"])
@main.route("/",methods=["GET","POST"])
def home():
    """
    The `home` function returns the rendered template "index.html".
    :return: The `render_template("index.html")` function is being returned.
    """
    return render_template("HOME.html")


@main.route("/register",methods=['GET','POST'])
def register():
    return render_template("REGISTER/register.html")