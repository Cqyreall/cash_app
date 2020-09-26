class Transaction:

    def __init__(self, tag, merchant, user, amount, date, id=None):
        self.tag = tag
        self.merchant = merchant
        self.user = user
        self.amount = amount
        self.date = date
        self.id = id
        self.total_amount = []

    def add_amount(self, transaction):
        transaction.total_amount.append(transaction.amount)