from flask import Flask, Blueprint, render_template, request

from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users/new")
def users():
    return render_template("homepage.html")

@users_blueprint.route("/users", methods=['POST'])
def new_user():
    users = user_repository.select_all()
    name = request.form['name']
    budget = request.form['budget']
    new_user = User(name, budget)
    user_repository.save(new_user)
    return render_template("user/login.html", new_user = new_user, users=users)
    