from flask import Flask, request, render_template, redirect, session, abort
from pymongo import MongoClient
import os

app = Flask(__name__, static_folder="public")
app.secret_key = "TODO_task3"

PHOTOS_BASE = "./public/photos"
client = MongoClient(host='mongo_dbs', port=27017)
db = client.photoapp


@app.route("/land")
def landing():
    return render_template('land.html', image="./public/images/html-programming.jpg")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    if not session:
        abort(403)
    path = PHOTOS_BASE + "/" + session['username']
    photos = os.listdir(path)
    return render_template('gallery.html', path=path, photos=photos)

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
    session.clear()
    return redirect("/")

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

@app.route("/account-details", methods=["GET", "POST"])
def save_account():
    return "TODO_task4"

@app.route("/gallery/<file>", methods=["POST"])
def gallerydel(file):
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
    return "HTTP Error 404 - Page Not Found"


if __name__ == "__main__":

    # check if "photo dbs" exists
    if not os.path.isdir(PHOTOS_BASE):
        os.makedirs(PHOTOS_BASE)

    app.run(debug=True, host='0.0.0.0', port=5000)
