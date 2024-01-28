import mysql.connector
from mysql.connector import Error
from geo import AddressComparator

class MySQLDatabase:
    def __init__(self, host, database, user, password, table_name):
        """
        this is my python
        """
        self.connection = None
        self.table_name = table_name
        self.address_compare = AddressComparator()
        try:
            self.connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("MySQL Database connection successful")
        except Error as e:
            print(f"Error: {e}")

    def insert_data(self, data_dict):
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['%s'] * len(data_dict))
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, tuple(data_dict.values()))
            self.connection.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Error: {e}")
    
    def query_data_sorted(self, dest_address: str, addr_column: int, columns=None):
        data = self.query_data(columns)
        data_by_addr = {}  
        data_by_dist = {}
        dist_list = []
        out = []
        for tup in data:
            data_by_addr[tup[addr_column]] = tup
        
        for addr in data_by_addr.keys():
            dist = self.address_compare.calculate_distance(dest_address, addr)
            data_by_dist[dist] = data_by_addr[addr]
        
        dist_list = sorted(data_by_dist.keys())
        
        for dist in dist_list:
            out.append(data_by_dist[dist])

        return out

    def query_data(self, columns=None):
        column_str = ', '.join(columns) if columns else '*'
        query = f"SELECT {column_str} FROM {self.table_name}"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
        

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")