from n_class_northwind import *


class CustomerTable(NorthwindCon):

    # Get one row (specific customer)
    def fetch_by_customer_id(self, c_id):
        return self.sql_query(f"SELECT * FROM Customers WHERE CustomerID = '{c_id}'").fetchone()

    # Get all rows
    def fetch_all(self, company_name=None):
        output = []
        if company_name is None:
            q_result = self.sql_query('SELECT * FROM Customers')
        else:
            q_result = self.sql_query(f"SELECT * FROM Customers WHERE CompanyName LIKE '%{company_name}%' ")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            output.append(row)
        return output

    # Insert new customer
    def insert_row(self, c_id, customer_name, city, country):
        return self.sql_query(f"""
        INSERT INTO Customers
        (CustomerID, CompanyName, City, Country)
        VALUES
        ('{str(c_id)}', '{customer_name}', '{city}', '{country}')""")
