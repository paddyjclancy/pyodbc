from subclass_product_table import *


northwind = NorthwindCon()
northwindsub = ProductTable()

print(northwind.sql_query("SELECT * FROM Products").fetchone())
print(northwindsub.fetch_by_product_id(5))
print(northwindsub.insert_row(99999999999))
print(northwindsub.fetch_all())
