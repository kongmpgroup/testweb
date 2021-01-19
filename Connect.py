import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                 password="SSVqpk94182",
                                 host="node8616-advweb-24.app.ruk-com.cloud:11070",
                                 port="11070",
                                 database="CloudDB" )
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), "/n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to -", record, "/n")

except(Exception, psycopg2.Error) as error:
    print("Error while connecting to ppstgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


