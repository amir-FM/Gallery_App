from flask import Flask, request, render_template, redirect, session

# Note: static folder means all files from there will be automatically served over HTTP
app = Flask(__name__, static_folder="public")
app.secret_key = "TODO_task3"

# TODO Task 02: you can use a global variable for storing the auth session
# e.g., add the "authenticated" (boolean) and "username" (string) keys.

# you can use a dict as user/pass database
ALLOWED_USERS = {
    "test": "test123",
    "admin": "n0h4x0rz-plz",
}

# Task 04: database filename
DATABASE_FILE = "database.txt"


@app.route("/land")
def landing():
    return render_template('land.html', image="./public/images/html-programming.jpg")

@app.route("/")
def index():
    # TODO Task 01: render the index page using child template
    return render_template('index.html')

@app.route("/second")
def second():
    # TODO Task 01: render the second page using child template
    return render_template('second.html', mycontent=request.args.get('mycontent'))

# TODO Task 02: Authentication
@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = "Wrong username or password"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if ALLOWED_USERS.get(username) == password:
            session['username'] = username
            return redirect("/")
        else:
            return render_template("login.html", error_msg=error_msg)
    elif request.method == "GET":
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error_msg = "Wrong username or password"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if ALLOWED_USERS.get(username) == password:
            session['username'] = username
            return redirect("/")
        else:
            return render_template("register.html", error_msg=error_msg)
    elif request.method == "GET":
        return render_template("register.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    error_msg = "Wrong username or password"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if ALLOWED_USERS.get(username) == password:
            session['username'] = username
            return redirect("/")
        else:
            return render_template("login.html", error_msg=error_msg)
    elif request.method == "GET":
        return render_template("upload.html")

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

@app.errorhandler(404)
def error404(code):
    # bonus: make it show a fancy HTTP 404 error page, with red background and bold message ;) 
    return "HTTP Error 404 - Page Not Found"


# Run the webserver (port 5000 - the default Flask port)
if __name__ == "__main__":
    app.run(debug=True, port=5000)

