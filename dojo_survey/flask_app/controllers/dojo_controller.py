from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo

# display dojo survey form
@app.route('/')
def index():
    return render_template("index.html")


# performing the action of submitting survey
@app.route('/result', methods=['POST'])
def survey_create():
    # if user inputs are not valid, redirect to home page
    if not Dojo.validate(request.form):
        return redirect('/')

    # if input is valid, put user input into db
    id = Dojo.create(request.form)
    return redirect(f"/display/{id}")


# display single dojo survey result
@app.route('/display/<int:dojo_id>')
def display(dojo_id):
    # redirect successfully, show the result page
    return render_template("result.html", dojo = Dojo.get_one({"id": dojo_id}))


