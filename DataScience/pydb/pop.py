import pandas as pd
import psycopg2

con = psycopg2.connect(database="postgres",user="postgres", password="6522", host="127.0.0.1", port="5432")
users=pd.read_csv('500-us-users.csv');
cur = con.cursor()


for i in users.index :
    
    # print(users.at[i,'address'])
    #print(users.iat[i,1])
    #print(users.at[i,'first_name])
    cur.execute(f"""
      insert into people.person(person_id,last_name,first_name,land_line,mobile_phone,address,city,county,state,zip)
      values('{i}','{users.at[i,'last_name']}','{users.at[i,'first_name']}',
      '{users.at[i,'phone1']}','{users.at[i,'phone2']}','{users.at[i,'address']}',
      '{users.at[i,'city']}','{users.at[i,'county']}',
      '{users.at[i,'state']}','{users.at[i,'zip']}'
            )
         """)

#print(users)
con.commit()
cur.close()
con.close()