from database import MySQLDatabase

insert = {'First_Name' : 'john', 'Last_Name' : 'john', 'Address' : 'wrong address1', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}
insert1 = {'First_Name' : 'mary', 'Last_Name' : 'john', 'Address' : 'ASDSA', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}
insert2 = {'First_Name' : 'alex', 'Last_Name' : 'john', 'Address' : 'adsfadsf', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}
insert3 = {'First_Name' : 'bodsflkjh;dflsb', 'Last_Name' : 'john', 'Address' : 'dasfdsfa', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}
insert4 = {'First_Name' : 'bodsflkjh;dflsb', 'Last_Name' : 'john', 'Address' : 'asfdsfad', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}

db = MySQLDatabase('localhost', 'hackathon', 'kerdos', 'kerdos123', 'listings')

db.insert_data(insert)
db.insert_data(insert1)
db.insert_data(insert2)
db.insert_data(insert3)
db.insert_data(insert4)
print(db.query_data())
print()
print(db.query_data_sorted("Brigham Young University, Provo, UT 84602, United States", 2))