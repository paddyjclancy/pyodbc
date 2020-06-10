from n_class_northwind import *


class ProductTable(NorthwindCon):

    # Get one row of data - specified
    def fetch_by_product_id(self, p_id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(p_id)).fetchone()

    # Get all data from table
    def fetch_all(self):
        return self.sql_query('SELECT * FROM Products').fetchall()

    # Insert - requires a product name, price, and quantity in stock
    def insert_row(self, product_name, product_price, product_stock):
        return self.sql_query(f"""
        INSERT INTO Products
        (ProductName, UnitPrice, UnitsInStock)
        VALUES
        ('{product_name}', '{product_price}', '{product_stock}')""")
