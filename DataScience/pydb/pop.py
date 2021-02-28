import pandas as pd
import psycopg2

con = psycopg2.connect(database="postgres",user="postgres", password="6522", host="127.0.0.1", port="5432")
users_df=pd.read_csv('500-us-users.csv');
cur = con.cursor()


for i in users_df.index :
    print(users_df.at[i,'address'])
    #print(users_df.iat[i,1])
    #print(users_df.at[i,'first_name])
    cur.execute(f"""
      insert into people.person(person_id,last_name,first_name,land_line,mobile_phone,address,city,county,state,zip)
      values('{i}','{users_df.at[i,'last_name']}','{users_df.at[i,'first_name']}',
      '{users_df.at[i,'phone1']}','{users_df.at[i,'phone2']}','{users_df.at[i,'address']}',
      '{users_df.at[i,'city']}','{users_df.at[i,'county']}',
      '{users_df.at[i,'state']}','{users_df.at[i,'zip']}'
            )
         """)

#print(users_df)
con.commit()
cur.close()
con.close()