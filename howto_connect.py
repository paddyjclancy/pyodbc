import pyodbc


# 1) DB server connection variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# 2) establishing the connection
# connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


# 3) make cursor (this keeps state)
# making a cursor
cursor = connection.cursor()

# being a code plumber and investigating
print(connection)
print(cursor)

query_result = cursor.execute('SELECT * FROM Products')

print(query_result)


# .fetchone() --> output next 1 pyodbc.Row -- remember cursor maintains state
# if you want to get back to the start, you need a new cursor or to run the execute command again.
print(query_result.fetchone()) # less one entry in the cursor
print(query_result.fetchone()) # less one entry in the cursor
data_point_card = query_result.fetchone()

# this one entry of data is a 'pyodbc.Row' object
print(type(data_point_card))
# behaves like an iterable list - organised with index
print(data_point_card[1])
# also behave like a oop object, where the initialized parameters/attribute are the column names
print(data_point_card.ProductName)

# Search documentatio/or internet to use a for loop to get our all of the data using the .fetchone() method


# .fecthall --> output all the pyodbc.Row (s) into list -- remember cursor maintains state
# DANGEROUS -- Do not use in real life. So also not here :)
list_of_all_rows = query_result.fetchall()
print(len(list_of_all_rows))
# if you have a million entries this will cause your server to run out of intantanous memory and wil crash.

# # print(query_result.fetchall())
# # print(query_result.fetchall())
# all_results_list = query_result.fetchall()
#
# for data in all_results_list:
#     print(data.ProductName, 'costs: ', data.UnitPrice)



# The Better way of getting out all your data
# query_result = [10, 10, 100, 30, 50, None]
query_result = cursor.execute('SELECT UnitPrice FROM Products')


while True:
#     user our query results or cursor with query result and
#     fectch one at a time and
#     do whatever we want/need with that data point - print it? get out the price? add a discount?
#       Stop the iteration when there is no more data
#           --> or when the data point in None (python) (null is in SQL)
#     print(type(query_result)) is a cursors
    row = query_result.fetchone()
    if row is None:
        break
    print('NOW ONLY:' , float(row.UnitPrice) * 1.25)


# fetchmany when you know how many
print(cursor.fetchmany(30))
print(cursor.fetchmany(30))
print(cursor.fetchmany(30))

# The way you fetch data will have an impact on performance and PRICE at then end of the month


# for data in all_results:
#     print(data.ProductName, ": ", float(data.UnitPrice))

while True:
    one_result = query_result.fetchone()
    if not one_result:
        break
    print("UnitPrice")

# for row in all_results:
#     print(row)
