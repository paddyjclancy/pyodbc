from n_class_northwind import *


class ProductTable(NorthwindCon):

    # Get one row of data - specified
    def fetch_by_product_id(self, p_id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(p_id)).fetchone()

    # Get all data from table
    def fetch_all(self, product_name=None):
        output = []
        if product_name is None:
            q_result = self.sql_query('SELECT * FROM Products')
        else:
            q_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{product_name}%' ")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            output.append(row)
        return output

    # Insert - requires a product name, price, and quantity in stock
    def insert_row(self, product_name, product_price, product_stock):
        return self.sql_query(f"""
        INSERT INTO Products
        (ProductName, UnitPrice, UnitsInStock)
        VALUES
        ('{product_name}', '{product_price}', '{product_stock}')""")

    # Update - replaces value(s)
