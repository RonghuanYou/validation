from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.email import Email


# display form to create email
@app.route("/")
def index():
    return render_template("index.html")


# performing the action of creating emails
@app.route("/create", methods=['POST'])
def create():
    # if input email is not valid, redirect to form page
    if not Email.email_validate(request.form):
        return redirect("/")

    # if email is valid, store it in db
    id = Email.create(request.form)
    return redirect(f"/success/{id}")


# display all emails
@app.route("/success/<int:email_id>")
def display_all_emails(email_id):
    return render_template("success.html", all_emails = Email.get_all(), cur_email = Email.get_one({"id": email_id}))

