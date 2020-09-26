import pdb

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository


merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Amazon")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("CineWorld")
merchant_repository.save(merchant_3)


tag_1 = Tag("Entertainment")
tag_repository.save(tag_1)

tag_2 = Tag("Online Shopping")
tag_repository.save(tag_2)

tag_3 = Tag("Groceries")
tag_repository.save(tag_3)

transaction_1 = Transaction(tag_1, merchant_3, 12, "12/04/2020")
transaction_repository.save(transaction_1)

transaction_2 = Transaction(tag_2, merchant_2, 242, "10/04/2010")
transaction_repository.save(transaction_2)

transaction_3 = Transaction(tag_3, merchant_1, 5, "11/04/2020")
transaction_repository.save(transaction_3)

transaction_4 = Transaction(tag_2, merchant_2, 242, "10/04/2010")
transaction_repository.save(transaction_4)



print(tag_repository.transactions(tag_2)[0].__dict__)





pdb.set_trace()