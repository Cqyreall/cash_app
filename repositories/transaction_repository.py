from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
from models.user import User
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.user_repository as user_repository


def save(transaction):
    sql = "INSERT INTO transactions (tag_id, merchant_id, user_id, amount, date) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [transaction.tag.id, transaction.merchant.id, transaction.user.id, transaction.amount, transaction.date]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    transaction.add_amount(transaction)
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        user = user_repository.select(row['user_id'])
        transaction = Transaction(tag, merchant, user, row['amount'], row['date'], row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = tag_repository.select(result['tag_id'])
    merchant = merchant_repository.select(result['merchant_id'])
    user = user_repository.select(result['user_id'])
    transaction = Transaction(tag, merchant, user, result['amount'], result['date'], result['id'])
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (tag_id, merchant_id, user_id, amount, date) = (%s, %s, %s, %s, %s) where id =%s"
    values = [transaction.tag.id, transaction.merchant.id, transaction.user.id, transaction.amount, transaction.date, transaction.id]
    run_sql(sql, values)

def total_amount():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        user = user_repository.select(row['user_id'])
        transaction = Transaction(tag, merchant, user, row['amount'], row['date'], row['id'])
        transactions.append(transaction.amount)
    amount = sum(transactions)
    return amount