# Imported symbols here please!
from flask import Flask, request, render_template, redirect


# Initialize the Flask application
# Note: static folder means all files in there will be automatically offered over HTTP
app = Flask(__name__, static_folder="public")


@app.route("/")
def index():
    # TODO_task03: read & respond with your HTML page, as string!
    return render_template('initial_design.html')

@app.route("/google")
def redir_to_google():
    # TODO_task03: temporary redirect to https://www.google.com
    return redirect("https://www.google.com", code=302)

# TODO_task03: Add the second page to your website!
@app.route("/second")
def second_page():
    # just like the index!
    # make sure to clone/rename the html file and adjust its contents!
    return render_template('second.html', mycontent=request.args.get("mycontent", "<not specified>"))

@app.errorhandler(404)
def error404(code):
    # TODO_bonus: make it show a fancy HTTP 404 error page, with red background and bold message ;) 
    return "HTTP Error 404 - Page Not Found"


# this is the equivalent of the main() function, only executed if script is started directly!
# (e.g., condition is false if script is imported as library)
if __name__ == "__main__":
    # start the Flask server (port 5000 - the default one, though you can freely change it!)
    app.run(debug=True, port=5000)

