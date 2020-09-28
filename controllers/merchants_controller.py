from flask import Flask, redirect, request, render_template

from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchant", __name__)


@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)

@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html") 

@merchants_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    name = request.form['name']
    disable = True if 'disable' in request.form else False
    new_merchant = Merchant(name, disable)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    disable = True if 'disable' in request.form else False
    merchant = Merchant(name, disable, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")

