# Load the postgres module
import psycopg2
 
# Create a connection object
con = psycopg2.connect(database="postgres",user="postgres", password="6522", host="127.0.0.1", port="5432")
 #database="postgres",
# Create a cursor via the connection
cur = con.cursor()
#ex="create schema people;"
schemaString= """
                CREATE TABLE people.person(
               person_id         varchar(11) CONSTRAINT UPKCL_peopId PRIMARY KEY,
               last_name       varchar(40)       NOT NULL,
               first_name       varchar(20)       NOT NULL,
               land_line         char(12)          NOT NULL DEFAULT ('UNKNOWN'),
               mobile_phone         char(12)          NOT NULL DEFAULT ('UNKNOWN'),
               address        varchar(40)           NULL,
               city           varchar(20)           NULL,
               county          varchar(20)           NULL,
               state          char(2)               NULL,
               zip            char(5)               NULL );"""

# Query via the cursor
cur.execute(schemaString)
con.commit()
cur.close()
con.close()

# rows = cur.fetchall()
# for row in rows:
#    print(row)
 
# Alternatively, set the 'search_path' to set the schema search path (prefix)
# cur.execute("SET search_path TO pubs2")
# cur.execute("select * from authors")
# rows = cur.fetchall()
# for row in rows:
#    print(row)