from db.run_sql import run_sql

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING *"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():

    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['name'], results['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags where id=%s"
    values = [id]
    run_sql(sql,values)

def update(tag):
    sql = "UPDATE tags SET name = %s WHERE id = %s"
    values = [tag.name, tag.id]
    run_sql(sql,values)

def transactions(tag):
    transactions = []

    # sql = "SELECT transactions.amount FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchants.id WHERE transactions.tag_id = %s"
    sql = "SELECT * FROM merchants INNER JOIN transactions ON transactions.merchant_id = merchants.id WHERE transactions.tag_id = %s"
    values =[tag.id]
    results = run_sql(sql, values)

    for row in results:
        # transaction = Transaction(tag, merchant)
        merchant_id = row['merchant_id']
        merchant = merchant_repository.select(merchant_id)
        transaction = Transaction(tag, merchant, row['amount'], row['date'])
        transactions.append(transaction)
    return transactions
        
    

