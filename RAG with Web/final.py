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

def get_foreign_keys(table_name, cursor):
    # Query to fetch foreign key constraints for a given table
    query = f"""
        SELECT
            CONSTRAINT_NAME,
            COLUMN_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM
            INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE
            TABLE_NAME = '{table_name}'
            AND REFERENCED_TABLE_NAME IS NOT NULL
            AND CONSTRAINT_SCHEMA = '{config['database']}'
    """

    cursor.execute(query)
    foreign_keys = cursor.fetchall()
    return foreign_keys

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

        # Get foreign key constraints for the current table
        foreign_keys = get_foreign_keys(table_name, cursor)

        # Generate CREATE TABLE query
        print("CREATE TABLE `{}` (".format(table_name))
        print(",\n".join(column_definitions))

        # Add primary key constraint if available
        primary_key_query = f"    CONSTRAINT `PK_{table_name}` PRIMARY KEY (`{table_name}Id`)"
        print(primary_key_query)

        # Add foreign key constraints
        for fk in foreign_keys:
            fk_constraint = f"    CONSTRAINT `FK_{table_name}_{fk[2]}` " \
                            f"FOREIGN KEY (`{fk[1]}`) " \
                            f"REFERENCES `{fk[2]}` (`{fk[3]}`)"
            print(fk_constraint)

        print(");")
        print("")  # Empty line for separation

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'cnx' in locals() and cnx:
        cnx.close()
