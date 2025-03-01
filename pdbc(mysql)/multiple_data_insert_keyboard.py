import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="insert into actor(actor_id,first_name,last_name,last_update) values(%s,%s,%s,%s)"
    cursor=con.cursor()
    while True:
        actor_id=input("Enter the actor id: ")
        first_name=input("Enter the first name: ")
        last_name=input("Enter the last name: ")
        last_update=input("Enter the last update: ")
        cursor.execute(query,(actor_id,first_name,last_name,last_update))
        con.commit()
        choice=input("Do you want to continue? (y/n): ")
        if choice.lower()=="n":
            break
except mysql.connector.Error as e:
    print("Error inserting data",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()