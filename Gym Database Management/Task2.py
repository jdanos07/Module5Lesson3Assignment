from mysqlConnect import connect_database
from mysqlConnect import Error

connection = connect_database()
# def member():
if connection is not None:
    try:
        cursor = connection.cursor()
        
        new_workoutsession = (1, 1, '2024-11-25', 30, 250)

        query = 'INSERT INTO workoutsessions (workout_id, member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s, %s)'

        cursor.execute(query, new_workoutsession)
        connection.commit()
        print('Workout recorded')

    except Error as e:
        print(f'Error: {e}')
  
    finally:
        cursor.close()
        connection.close()
        print('Connection disabled')
