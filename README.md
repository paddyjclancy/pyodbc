# PYODBC and OOP

We are looking into the PYODBC package. 

1) We are going to use the package to make an OOP module that abstracts our interaction with the NW DB. Starting with the connection.

2) And then further abstract the interaction with specific Tables. 

3) Finally, where appropriate we will use CRUD to build methods.

### CRUD - Product table

You can CRUD the product table. Available methods:

##### Initialisation

```python
northwind = NorthwindCon()
northwindsub = ProductTable()
```



#### - Create (Insert)

#### - Read (Get)
 - READ one: 
 
get_by_id(self, id) --> one object

Use this method to get out a product by ID
```python
    def fetch_by_product_id(self, p_id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID=' + str(p_id)).fetchone()


print(northwindsub.fetch_by_product_id(5))
```
 - READ all:
```python
    def fetch_all(self):
        return self.sql_query('SELECT * FROM Products').fetchall()


print(northwindsub.fetch_all())
```
#### - Update

#### - Delete





