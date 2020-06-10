import pyodbc

# 1) DB server connection variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# 2) establishing the connection
connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# making a cursor
cursor = connection.cursor()


# Q1 - How many orders in NWDB?

query_result1 = cursor.execute('SELECT COUNT(OrderID) AS "Number of Orders" FROM Orders')
print(f"1) No. of orders {query_result1.fetchone()}")

# Q2 - How many order that the Ship City is Rio de Janeiro?

query_result2 = cursor.execute('SELECT * FROM Orders')
output2 = []
while True:
    row = query_result2.fetchone()
    if row is None:
        break
    elif row.ShipCity == "Rio de Janeiro":
        output2.append(row)
print(f"2) Number of orders heading to Rio: {len(output2)}")

# Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims?

query_result2 = cursor.execute('SELECT * FROM Orders')
output3 = []
while True:
    row = query_result2.fetchone()
    if row is None:
        break
    elif row.ShipCity == "Rio de Janeiro":
        output3.append(row.OrderID)
    elif row.ShipCity == "Reims":
        output3.append(row.OrderID)

print(f"3) OrderIDs going to Rio / Reims: {output3}")

# Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers

query_result4 = cursor.execute("SELECT * FROM Customers WHERE CompanyName LIKE '%[Zz]%'")
output4 = []
while True:
    row = query_result4.fetchone()
    if row is None:
        break
    output4.append(row.CompanyName)


print(f"4) Z/z companies: {output4}")
