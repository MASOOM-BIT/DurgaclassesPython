import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",user="root",password="root",database="sakila")
    query="insert into actor(actor_id,first_name,last_name,last_update) values(%s,%s,%s,%s)"
    cursor=con.cursor()
    data=[
        (202,"ray","Doe","2021-01-01 00:00:00"),
        (203,"Jane","Doe","2021-01-01 00:00:00"),
        (204,"Jim","Beam","2021-01-01 00:00:00")
    ]
    cursor.executemany(query,data)
    con.commit()
    print("Data inserted successfully")
except mysql.connector.Error as e:
    print("Error inserting data",e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
