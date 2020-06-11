from n_class_northwind import *


class CustomerTable(NorthwindCon):

    # Get one row (specific customer)
    def fetch_by_customer_id(self, c_id):
        return self.sql_query('SELECT * FROM Customers WHERE CustomerID=' + str(c_id)).fetchone()

    # Get all rows
    def fetch_all(self):
        return self.sql_query('SELECT * FROM Customers').fetchall()

    # Insert new customer
    def insert_row(self, c_id, customer_name, city, country):
        return self.sql_query(f"""
        INSERT INTO Customers
        (CustomerID, CompanyName, City, Country)
        VALUES
        ('{str(c_id)}', '{customer_name}', '{city}', '{country}')""")
