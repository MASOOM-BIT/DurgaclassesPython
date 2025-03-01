import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="select * from actor"
    cursor=con.cursor()
    cursor.execute(query)
    n=int(input("Enter the number of rows to fetch: "))
    rows=cursor.fetchmany(n)
    with open("RESOURCES/actor.txt","w") as file:
            for row in rows:
                file.write(str(row))
except mysql.connector.Error as e:
    print("Error selecting data",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
