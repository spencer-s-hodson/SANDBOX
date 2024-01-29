from database import MySQLDatabase

insert = {'First_Name' : 'johnhy', 'Last_Name' : 'john', 'Address' : 'bad address', 'Price' : 1243.44, 'Type' : 'Covered', 'Contact'  : "898-999-9999"}
 
db = MySQLDatabase('localhost', 'hackathon', 'kerdos', 'kerdos123', 'listings')

db.insert_data(insert)

print(db.query_data())
print()
print(db.query_data_sorted("Brigham Young University, Provo, UT 84602, United States", 2))