from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, budget) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    result = run_sql(sql)
    for row in result:
        user = User(row['name'], row['budget'], row['id'])
        users.append(user)
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    user = User(result['name'], result['budget'], result['id'])
    return user