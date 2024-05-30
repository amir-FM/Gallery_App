from flask import Flask, request, render_template, redirect, session, abort
from pymongo import MongoClient
import os

# Note: static folder means all files from there will be automatically served over HTTP
app = Flask(__name__, static_folder="public")
#modal = Modal(app)
app.secret_key = "TODO_task3"

# TODO Task 02: you can use a global variable for storing the auth session
# e.g., add the "authenticated" (boolean) and "username" (string) keys.

# you can use a dict as user/pass database
ALLOWED_USERS = {
    "test": "test123",
    "admin": "n0h4x0rz-plz",
}

# Task 04: database filename
PHOTOS_BASE = "./public/photos"
client = MongoClient('localhost', 27017)
db = client.photoapp


@app.route("/land")
def landing():
    return render_template('land.html', image="./public/images/html-programming.jpg")

@app.route("/")
def index():
    # TODO Task 01: render the index page using child template
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    # TODO Task 01: render the gallery page using child template
    if not session:
        abort(403)
    path = PHOTOS_BASE + "/" + session['username']
    photos = os.listdir(path)
    return render_template('gallery.html', path=path, photos=photos)

# TODO Task 02: Authentication
@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = "Wrong username or password"
    invalid_fields = "Invalid username or password"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "" or password == "":
            return render_template("login.html", error_msg=invalid_fields)
        if db.users.find_one({"username": username, "password" : password}):
            session['username'] = username
        else:
            return render_template("login.html", error_msg=error_msg)
        path = PHOTOS_BASE + "/" + session['username']
        # init dirs
        if not os.path.isdir(path):
            os.mkdir(path)

        return redirect("/")
    elif request.method == "GET":
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error_msg = "User already exists"
    invalid_fields = "Invalid username or password"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "" or password == "":
            return render_template("register.html", error_msg=invalid_fields)
        if not db.users.find_one({"username": username}):
            db.users.insert_one({"username": username, "password": password})
            return redirect("/login")
        else:
            return render_template("register.html", error_msg=error_msg)
    elif request.method == "GET":
        return render_template("register.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    error_msg = "Wrong username or password"
    if request.method == "POST":
        file = request.files["file"]
        rename = request.form.get("fileRename", "")
        section = request.form.get("section", "")
        path = PHOTOS_BASE + "/" + session['username']
        extension = file.filename.split(".")[-1]
        if rename:
            file.filename = section + "_" + rename.replace(" ", "") + "." + extension
        else:
            file.filename = section + "_" + file.filename.replace(" ", "")

        file.save(os.path.join(path, file.filename))
        return redirect("/gallery");
    elif request.method == "GET":
        if session:
            return render_template("upload.html")
        abort(403)
        return jsonify({"success": "false"})

@app.route("/logout")
def logout():
    # TODO Task 02: clear authentication status
    # session["authenticated"] = False
    session.clear()
    return redirect("/")
    # return "TODO"

# @app.context_processor
# def inject_template_vars():
#     if session["authenticated"]:
#         return

# You can use this as a starting point for Task 04
# (note: you need a "write" counterpart)
def read_database(filename):
    """ Reads the user account details database file (line by line). """
    with open(filename, "rt") as f:
        line1 = f.readline()
        line2 = f.readline()
        age = int(f.readline())
        return {
            "first_name": line1,
            "last_name": line2,
            "age": age,
        }

# TODO Task 04: Save Account Details
@app.route("/account-details", methods=["GET", "POST"])
def save_account():
    # Hint: if method == "GET", read the data from the database and pass it to the template
    # otherwise (when POST), replace the database with the user-provided data.
    return "TODO_task4"

@app.route("/gallery/<file>", methods=["POST"])
def gallerydel(file):
    # TODO Task 01: render the gallery page using child template
    if request.method == "GET":
        abort(403)
        return redirect("/gallery")
    if not session:
        abort(403)
    path = PHOTOS_BASE + "/" + session['username']
    if not os.path.isfile(path + "/" + file):
        return redirect("/gallery")
    os.remove(path + "/" + file)
    return redirect("/gallery");

@app.errorhandler(404)
def error404(code):
    # bonus: make it show a fancy HTTP 404 error page, with red background and bold message ;) 
    return "HTTP Error 404 - Page Not Found"


# Run the webserver (port 5000 - the default Flask port)
if __name__ == "__main__":
    app.run(debug=True, port=5000)

