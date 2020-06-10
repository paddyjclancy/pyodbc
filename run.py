from n_subclass_product_table import *


northwind = NorthwindCon()
northwindsub = ProductTable()

print(northwind.sql_query("SELECT * FROM Products").fetchone())
print(northwindsub.fetch_by_product_id(5))

northwindsub.insert_row('Matcha', 8, 88)

# print(northwindsub.fetch_all())
