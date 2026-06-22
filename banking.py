import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mani@1234",
    database="banking1"
)
# print("Connected successfully")
mycursor = mydb.cursor()
# mycursor.execute("Create Database Banking1")
# print("Database Created")

# mycursor.execute("Use Banking1")
# print("database is used")

# mycursor.execute("""
#     Create Table Customers1(
#         customer_id Int Auto_Increment Primary Key,
#         name varchar(100),
#         city varchar(100)
# )
# """)
# print("Table Created")

# mycursor.execute("""
#     Create Table Accounts(
#         account_id Int Auto_Increment Primary Key,
#         customer_id Int,
#         balance Decimal(10,2)
# )
# """)
# print("Accounts created")
# sql = "Insert into Customers1(customer_id, name, city) Values(%s, %s, %s)"
# val = [
#     (1, "Manisha", "Delhi"),
#     (2, "Rahul", "Pune"),
#     (3, "Sonia", "Goa")
# ]

# sql = "Insert into Accounts(account_id, customer_id, balance) Values(%s, %s, %s)"
# val = [
#     (101, 1, 5000),
#     (102, 2, 1000),
#     (103, 3, 800)
# ]

# mycursor.executemany(sql, val)
# mydb.commit()



# mycursor.execute(sql)
# mycursor.execute("Select * From Customers1")
# result = mycursor.fetchall()

# for row in result:
#     print(row)

# mycursor.execute("Select * From Accounts")
# result = mycursor.fetchall()

# for row in result:
#     print(row)


# sql = """
# Select Customers1.name, Accounts.balance
# FROM Customers1
# RIGHT JOIN Accounts
# On Customers1.customer_id = Accounts.customer_id
# """

# mycursor.execute(sql)
# result = mycursor.fetchall()

# for row in result:
#     print(row)