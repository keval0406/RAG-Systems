# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost", 
#     port=3306,user="root",
#     password="keval",
#     database="mydatabase"
#     )

# cur = mydb.cursor()

# s = "insert into book values (%s, %s, %s)"
# books = [(2, "PHP",500),(3, "JAVA",120),(4, "HTML",200)]
# cur.executemany(s,books)
# mydb.commit()

# print()

# import mysql.connector

# # MySQL connection configuration
# config = {
#   'user': 'root',
#   'password': 'keval',
#   'host': 'localhost',   # Or your MySQL server IP address
#   'database': 'information_schema',  # Default MySQL schema containing metadata
#   'raise_on_warnings': True,
#   'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
# }

# try:
#     # Establish a connection to the MySQL server
#     cnx = mysql.connector.connect(**config)

#     # Create a cursor object using the connection
#     cursor = cnx.cursor()

#     # Execute a query to fetch schema names
#     cursor.execute("SELECT * FROM information_schema.schemata where schema_name = 'chinook'")

#     # Fetch all rows (schemas) from the result set
#     schemas = cursor.fetchall()

#     # print(schemas)
#     # Print the list of schemas
#     for schema in schemas:
#         print(schema[1])
#         pass

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # Close cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if 'cnx' in locals():
#         cnx.close()

# WOrking 
# import mysql.connector

# # MySQL connection configuration
# config = {
#   'user': 'root',
#   'password': 'keval',
#   'host': 'localhost',   # Or your MySQL server IP address
#   'database': 'chinook',  # Your database name
#   'raise_on_warnings': True,
#   'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
# }

# try:
#     # Establish a connection to the MySQL server
#     cnx = mysql.connector.connect(**config)

#     # Create a cursor object using the connection
#     cursor = cnx.cursor()

#     # Example: Get table structure (columns and types) in the chinook database
#     cursor.execute("SHOW TABLES")

#     # Fetch all tables from the result set
#     tables = cursor.fetchall()

#     # Loop through each table
#     for table in tables:
#         table_name = table[0]
#         print(f"Table: {table_name}")
#         print("Columns:")

#         # Get columns for the current table
#         cursor.execute(f"SHOW COLUMNS FROM {table_name}")

#         # Fetch all columns from the result set
#         columns = cursor.fetchall()

#         # Print each column name and type
#         for column in columns:
#             print(f"{column[0]} - {column[1]}")

#         print("")  # Empty line for separation

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # Close cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if 'cnx' in locals():
#         cnx.close()

import mysql.connector

# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'keval',
    'host': 'localhost',   # Or your MySQL server IP address
    'database': 'chinook',  # Your database name
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
}

def generate_select_query(table_name):
    return f"SELECT * FROM {table_name};"

def generate_insert_query(table_name, columns, values):
    columns_str = ', '.join(columns)
    values_str = ', '.join([f"'{value}'" for value in values])
    return f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});"

def generate_update_query(table_name, update_dict, condition):
    set_clause = ', '.join([f"{key} = '{value}'" for key, value in update_dict.items()])
    return f"UPDATE {table_name} SET {set_clause} WHERE {condition};"

def generate_delete_query(table_name, condition):
    return f"DELETE FROM {table_name} WHERE {condition};"

try:
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(**config)

    # Create a cursor object using the connection
    cursor = cnx.cursor()

    # Example: Get table structure (columns and types) in the chinook database
    cursor.execute("SHOW TABLES")

    # Fetch all tables from the result set
    tables = cursor.fetchall()

    # Loop through each table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")

        # Get columns for the current table
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")

        # Fetch all columns from the result set
        columns = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns]

        # Generate SQL queries based on table structure
        select_query = generate_select_query(table_name)
        insert_query = generate_insert_query(table_name, column_names, ['value1', 'value2'])
        update_query = generate_update_query(table_name, {'column1': 'value1', 'column2': 'value2'}, "condition")
        delete_query = generate_delete_query(table_name, "condition")

        # Print generated queries
        print("Select Query:")
        print(select_query)
        print("Insert Query:")
        print(insert_query)
        print("Update Query:")
        print(update_query)
        print("Delete Query:")
        print(delete_query)
        print("")  # Empty line for separation

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals():
        cnx.close()
