import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='gw2246fx',
                             password='9Astronaut',
                             db='gw2246fx_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        user_input = input("enter a student name: ")
        sql = "SELECT * from Student where firstname = %s"
        
        # execute the SQL command
        cursor.execute(sql, (user_input))
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
