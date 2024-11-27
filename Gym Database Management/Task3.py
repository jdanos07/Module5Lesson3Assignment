from mysqlConnect import connect_database
from mysqlConnect import Error

def age_update(age, id):
    connection = connect_database()

    if connection is not None:
        try:
            cursor = connection.cursor()
            
            updated_member = (age, id)

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

age_update(19, 2)