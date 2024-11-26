from mysqlConnect import connect_database
from mysqlConnect import Error

connection = connect_database()
# def member():
if connection is not None:
    try:
        cursor = connection.cursor()
        
        updated_member = (22, 1)

        query = 'UPDATE members SET age = %s WHERE id = %s'

        cursor.execute(query, updated_member)
        connection.commit()
        print('Member updated')

    except Error as e:
        print(f'Error: {e}')
  
    finally:
        cursor.close()
        connection.close()
        print('Connection disabled')