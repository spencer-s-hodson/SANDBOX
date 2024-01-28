from database import MySQLDatabase

insert = {'First_Name' : 'bob', 'Last_Name' : 'john', 'Address' : '5554934 dfkjhd', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}

db = MySQLDatabase('localhost', 'hackathon', 'kerdos2', 'kerdos123', 'listings')

db.insert_data(insert)
print(db.query_data())
from database import MySQLDatabase

insert = {'First_Name' : 'bob', 'Last_Name' : 'john', 'Address' : '5554934 dfkjhd', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}

db = MySQLDatabase('localhost', 'hackathon', 'kerdos', 'kerdos123', 'listings')

db.insert_data(insert)
print(db.query_data())