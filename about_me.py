from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return "<h1>What Up Cuh</h1> "
    return render_template("index.html")


# @app.route("/second_page")
# def second_page():
#     return "Its the second page"


# @app.route("/third")  # Redirect example
# def third():
#     return redirect(url_for("home", name="Vip"))


if __name__ == "__main__":
    app.run()
