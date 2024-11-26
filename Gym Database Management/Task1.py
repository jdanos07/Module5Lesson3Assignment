from mysqlConnect import connect_database
from mysqlConnect import Error

connection = connect_database()
# def member():
if connection is not None:
    try:
        cursor = connection.cursor()

        new_member = (2,'Jane Smith', '18')

        query = 'INSERT INTO members (id, name, age) VALUES (%s, %s, %s)'

        cursor.execute(query, new_member) 
        connection.commit()
        print('New member has been enrolled.')

    except Error as e:
        print(f'Error: {e}')
        
    finally:
        cursor.close()
        connection.close()
        print('Connection disabled')