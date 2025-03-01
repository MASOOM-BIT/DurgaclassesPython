import mysql.connector
#fetchall() is used to return list all the data from the table
try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="select * from actor"
    cursor=con.cursor()
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        print('actor_id:',row[0])
        print('first_name:',row[1])
        print('last_name:',row[2])
        print('last_update:',row[3])
        print('--------------------------------')
        
except mysql.connector.Error as e:
    print("Error selecting data",e)
finally:
    if con.is_connected():
        cursor.close()