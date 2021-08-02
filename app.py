
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy


app = Flask(__name__)
app.secret_key = "Ragama"
app. permanent_session_lifetime = timedelta(days=7)

@app.route("/" , methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["mn"]
        session ["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html")
    else:
        flash("You are not Logged")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have left us, {user}", "info")
    session.pop("user", None)   
    return redirect(url_for("login"))


@app.route("/home")
def home():
    return render_template("home.html", content="Testing")




if __name__ == "__main__":
    app.run(debug=True)
