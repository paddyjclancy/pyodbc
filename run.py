from n_subclass_product_table import *
from n_subclass_customer_table import *


northwind = NorthwindCon()
northwind_p = ProductTable()
northwind_c = CustomerTable()


# print(northwind.sql_query("SELECT * FROM Products").fetchone())

# Products
# Get one
print("Products \n Get one")
print(northwind_p.fetch_by_product_id(5))
print(northwind_p.fetch_by_product_id(3))
print(northwind_p.fetch_by_product_id(25))

# Insert
northwind_p.insert_row('Matcha', 8, 80)
northwind_p.insert_row('Coffee', 2, 300)

# Get all
print("\n Get all")
print(northwind_p.fetch_all())

# Update


# Customers
# Get one
# print(northwind_c.fetch_by_customer_id(1))

# Get all
print(northwind_c.fetch_all())

# Insert row
# print(northwind_c.insert_row('500000', 'Locker', 'London', 'UK'))
