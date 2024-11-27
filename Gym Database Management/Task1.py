from mysqlConnect import connect_database
from mysqlConnect import Error

def add_member(id, name, age):
    connection = connect_database()

    if connection is not None:
        try:
            cursor = connection.cursor()

            new_member = (id, name, age)

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

add_member(3, 'Scott Black', 21)