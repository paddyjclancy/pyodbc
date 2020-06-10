from class_northwind import *


class ProductTable(NorthwindCon):

    # Get one
    def fetch_by_product_id(self, p_id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(p_id)).fetchone()

    # Get all
    def fetch_all(self):
        return self.sql_query('SELECT * FROM Products').fetchall()

    # Insert
    def insert_row(self, product_id):
        self.sql_query('INSERT INTO Products (ProductID) VALUES (' + str(product_id) + ')')
        # return self.sql_query('SELECT * FROM Products WHERE ProductName=' + product_name).fetchone()
        # self.connection.commit()