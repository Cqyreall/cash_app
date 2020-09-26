from flask import Blueprint, Flask, render_template, request, redirect

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.user_repository as user_repository

transactions_blueprint= Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total_amount = transaction_repository.total_amount()
    user_budget = []
    users = user_repository.select_all()
    for user in users:
        user_budget.append(user.budget)
    sum_total = sum(user_budget)
    track = (total_amount/sum_total) * 100
    return render_template("transactions/index.html", transactions=transactions, total_amount=total_amount, track=track)

@transactions_blueprint.route("/transactions/new")
def new_transaction():
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    users = user_repository.select_all()
    return render_template("transactions/new.html", tags=tags, merchants=merchants, users=users)

@transactions_blueprint.route("/transactions", methods=['POST'])
def add_transaction():
    tag_id = request.form['tag_id']
    merchant_id = request.form['merchant_id']
    user_id = request.form['user_id']
    amount = request.form['amount']
    date = request.form['date']
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    user = user_repository.select(user_id)
    new_transaction = Transaction(tag, merchant, user, amount, date)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    users = user_repository.select_all()
    return render_template("transactions/edit.html", transaction=transaction, tags=tags, merchants=merchants, users=users)

@transactions_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    tag_id = request.form['tag_id']
    merchant_id = request.form['merchant_id']
    user_id = request.form['user_id']
    amount = request.form['amount']
    date = request.form['date']
    tag = tag_repository.select(tag_id)
    merchant = merchant_repository.select(merchant_id)
    user = user_repository.select(user_id)
    updated_transaction = Transaction(tag, merchant, user, amount, date, id)
    transaction_repository.update(updated_transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")





