from mysqlConnect import connect_database
from mysqlConnect import Error


def age_range_data(start_age, end_age):
    connection = connect_database()
    if connection is not None:
        try:
            cursor = connection.cursor()
            
            query = 'SELECT * FROM members WHERE age BETWEEN %s and %s'

            cursor.execute(query, (start_age, end_age))
            results = cursor.fetchall()

            if results:
                print('Members in age range:')
                for row in results:
                    print(row)
            
            else:
                print('No matches')
    

        except Error as e:
            print(f'Error: {e}')
    
        finally:
            cursor.close()
            connection.close()
            print('Connection disabled')

age_data = age_range_data(18, 22)