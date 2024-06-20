# import mysql.connector

# # MySQL connection configuration
# config = {
#     'user': 'root',
#     'password': 'keval',
#     'host': 'localhost',   # Or your MySQL server IP address
#     'database': 'chinook',  # Your database name
#     'raise_on_warnings': True,
#     'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
# }

# def generate_create_table_query(table_name, columns, primary_key=None, foreign_keys=None):
#     query = f"CREATE TABLE {table_name} ("
    
#     # Add columns
#     column_definitions = []
#     for column_name, data_type, constraints in columns:
#         column_def = f"{column_name} {data_type}"
#         if constraints:
#             column_def += f" {constraints}"
#         column_definitions.append(column_def)
    
#     # Add primary key constraint
#     if primary_key:
#         pk_constraint = f"PRIMARY KEY ({', '.join(primary_key)})"
#         column_definitions.append(pk_constraint)
    
#     # Add foreign key constraints
#     if foreign_keys:
#         for fk in foreign_keys:
#             fk_constraint = f"FOREIGN KEY ({fk['column']}) REFERENCES {fk['ref_table']}({fk['ref_column']})"
#             column_definitions.append(fk_constraint)
    
#     query += ", ".join(column_definitions)
#     query += ");"
    
#     return query

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

#         # Get columns for the current table
#         cursor.execute(f"SHOW COLUMNS FROM {table_name}")

#         # Fetch all columns from the result set
#         columns = cursor.fetchall()

#         # Prepare column definitions
#         column_definitions = []
#         for column in columns:
#             column_name = column[0]
#             data_type = column[1]
#             constraints = ' '.join([str(c) for c in column[2:6] if c])  # Filter out None values
            
#             # Convert MySQL types to SQL Server types if necessary
#             if data_type.startswith('int'):
#                 data_type = 'INT'
#             elif data_type.startswith('varchar'):
#                 data_type = f"VARCHAR({data_type[8:-1]})"
#             elif data_type == 'datetime':
#                 data_type = 'DATETIME'

#             column_definitions.append((column_name, data_type, constraints))

#         # Generate CREATE TABLE query
#         create_table_query = generate_create_table_query(table_name, column_definitions)
#         print("Create Table Query:")
#         print(create_table_query)
#         print("")  # Empty line for separation

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     # Close cursor and connection
#     if 'cursor' in locals():
#         cursor.close()
#     if 'cnx' in locals():
#         cnx.close()

# import mysql.connector

# # MySQL connection configuration
# config = {
#     'user': 'root',
#     'password': 'keval',
#     'host': 'localhost',   # Or your MySQL server IP address
#     'database': 'chinook',  # Your database name
#     'raise_on_warnings': True,
#     'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
# }

# def generate_create_table_query(table_name, columns, primary_key=None, foreign_keys=None):
#     query = f"CREATE TABLE {table_name} (\n"
    
#     # Add columns
#     column_definitions = []
#     for column_name, data_type, constraints in columns:
#         column_def = f"    {column_name} {data_type}"
#         if constraints:
#             column_def += f" {constraints}"
#         column_definitions.append(column_def)
    
#     # Add primary key constraint
#     if primary_key:
#         pk_constraint = f"    PRIMARY KEY ({', '.join(primary_key)})"
#         column_definitions.append(pk_constraint)
    
#     # Add foreign key constraints
#     if foreign_keys:
#         for fk in foreign_keys:
#             fk_constraint = f"    FOREIGN KEY ({fk['column']}) REFERENCES {fk['ref_table']}({fk['ref_column']})"
#             column_definitions.append(fk_constraint)
    
#     query += ",\n".join(column_definitions)
#     query += "\n);"
    
#     return query

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

#         # Get columns for the current table
#         cursor.execute(f"SHOW COLUMNS FROM {table_name}")

#         # Fetch all columns from the result set
#         columns = cursor.fetchall()

#         # Prepare column definitions
#         column_definitions = []
#         for column in columns:
#             column_name = column[0]
#             data_type = column[1]
#             constraints = ' '.join([str(c) for c in column[2:6] if c])  # Filter out None values
            
#             # Convert MySQL types to SQL Server types if necessary
#             if data_type.startswith('int'):
#                 data_type = 'INT'
#             elif data_type.startswith('varchar'):
#                 data_type = f"VARCHAR({data_type[8:-1]})"
#             elif data_type == 'datetime':
#                 data_type = 'DATETIME'

#             column_definitions.append((column_name, data_type, constraints))

#         # Generate CREATE TABLE query
#         create_table_query = generate_create_table_query(table_name, column_definitions)
#         print(create_table_query)
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
    'database': 'sakila',  # Your database name
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'  # Use mysql_native_password plugin
}

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

        # Prepare column definitions
        column_definitions = []
        for column in columns:
            column_name = column[0]
            data_type = column[1]
            nullability = 'NOT NULL' if column[2] == 'NO' else ''
            default_value = f"DEFAULT '{column[4]}'" if column[4] is not None else ''
            extra = column[5]

            # Convert MySQL types to SQL Server types if necessary
            if data_type.startswith('int'):
                data_type = 'INT'
            elif data_type.startswith('varchar'):
                data_type = f"VARCHAR({data_type[8:-1]})"
            elif data_type == 'datetime':
                data_type = 'DATETIME'
            elif data_type == 'decimal':
                data_type = 'NUMERIC(10,2)'

            # Construct column definition
            column_def = f"    `{column_name}` {data_type} {nullability} {default_value} {extra}"
            column_definitions.append(column_def)

        # Generate CREATE TABLE query
        print("CREATE TABLE `{}` (".format(table_name))
        print(",\n".join(column_definitions))
        print(");")
        print("")  # Empty line for separation

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'cnx' in locals():
        cnx.close()
