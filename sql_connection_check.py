# import mysql.connector


# # Connecting to the database while making the MySQL connection
# mydb = mysql.connector.connect(
#                                 host='10.56.64.4',
#                                 user="dsathyan",
#                                 password="ZPhUghIOCIY38PaV",
#                                 database='backend'
#                               )

# mycursor = mydb.cursor()

# # VIEW TABLES IN A DATABASE
# # mycursor.execute("SHOW TABLES")
# # for x in mycursor:
# #     print(x[0].decode())



# # SELECT STATEMENT
# mydb = mysql.connector.connect(
#                                 host='10.56.64.4',
#                                 user="dsathyan",
#                                 password="ZPhUghIOCIY38PaV",
#                                 database='backend'
#                               )

# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# tables = []
# for table in mycursor:
#     print(table)
#     table_name = table[0].decode()
#     tables.append(table_name)

# print(tables)

# for table in tables[1:]:
#     # print(table)
#     # table = 'backend_license'
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT COUNT(*) FROM {}".format(table))
#     myresult1 = mycursor.fetchall()

#     for x in myresult1:
#         print(x[0], f' ({table})')


# import pandas as pd
# from sqlalchemy import create_engine
# # import pymysql

# host = '10.56.64.40'
# database = 'backend'

# user="dsathyan"
# password="ZPhUghIOCIY38PaV"

# query = 'SELECT COUNT(*) FROM backend.backend_license'

# # db_connection_str = 'mysql+pymysql://mysql_user:{password}@{host}/{database}'
# engine = create_engine('mysql+mysqlconnector://[{user}]:[{password}]@[host]:[3306]/[{databse}]', echo=False)

# cnx = engine.raw_connection()
# data = pd.read_sql(query, cnx)
# data.to_sql(name='sample_table2', con=cnx, if_exists = 'append', index=False)


# # df = pd.read_sql(query, con=db_connection)
# print(df)


import pandas as pd
from sqlalchemy import create_engine
import pymysql

host='10.80.144.42',
user="dsathyan",
password="IZWevixF2plPmzpV",
database='safehouse_db'


# engine = create_engine('mysql+pymysql://{user}:{password}@:3306/{database}')

# query = "SELECT * FROM {database}.backend_sendgridgeneral"

# df = pd.read_sql(query, engine)
# print(df.head())



####################################################################################################################

# # # Connect to the database
connection = pymysql.connect(   host='10.80.144.42',
                                user="dsathyan",
                                password="IZWevixF2plPmzpV",
                                database='safehouse_db')    

# create cursor
cursor= connection.cursor()

# # Execute query
sql = "SELECT * FROM backend_sendgridgeneral"
cursor.execute(sql)

# # Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
