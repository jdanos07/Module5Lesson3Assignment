from mysqlConnect import connect_database
from mysqlConnect import Error

def remove_workout(workout_id):
    connection = connect_database()

    if connection is not None:
        try:
            cursor = connection.cursor()
            
            remove_workout = (workout_id,)

            query = 'DELETE FROM workoutsessions WHERE workout_id = %s'

            cursor.execute(query, remove_workout)
            connection.commit()
            print('Workout removed')

        except Error as e:
            print(f'Error: {e}')
    
        finally:
            cursor.close()
            connection.close()
            print('Connection disabled')

remove_workout(2)