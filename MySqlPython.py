#!/usr/bin/python

#an Example of how to interact with MYSQL DB using Python MYSQL DB connector
#another usefull tool to work with DBS is SQL ALCHEMY just for notice

#import module to connect
import MySQLdb

#connection PArams
db = MySQLdb.connect(host="My Host",    # your host, usually localhost
                     user="My User",         # your username
                     passwd="My PAss",  # your password
                     db="DB name ASK your DBA")        # na
#set cursor
cursor = db.cursor()

#execute create query
cursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20))")

#execute create query
cursor.execute('CREATE TABLE person (person_id SMALLINT UNSIGNED,  '
               'fname VARCHAR(20), '
               ' lname VARCHAR(20), '
               ' gender CHAR(1), '
               ' birth_date DATE,'
               '  street VARCHAR(30),'
               '  city VARCHAR(20),  '
               'state VARCHAR(20), '
               ' country VARCHAR(20),'
               '  postal_code VARCHAR(20), '
               ' CONSTRAINT pk_person PRIMARY KEY (person_id) ); ')


#get input from db and print it
cursor.execute('desc person')
result=cursor.fetchall()
for x in result:
    print(x)

cursor.execute('CREATE TABLE favorite_food    '
               '(person_id SMALLINT UNSIGNED,'
               '      food VARCHAR(20),'
               '      CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),'
               '      CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)'
               '        REFERENCES person (person_id)     ); ')






#examples of using query execute using arguments
query="insert into person (person_id,fname,lname,gender,birth_date) VALUES(%s,%s,%s,%s,%s)"

args=('1','avi','grainik','M', '1972-05-27')


query="insert into person (person_id,fname,lname,gender,birth_date) VALUES(%s,%s,%s,%s,%s)"

args=('2','natan','alterman','F', '1972-05-27')

query="INSERT INTO favorite_food (person_id, food) VALUES(%s,%s) "

args=('1','pizza')


query="INSERT INTO favorite_food (person_id, food) VALUES(%s,%s) "

args=('2','falafel')


cursor.execute(query=query,args=args)
cursor.execute('select * from person')

#dont forget to commit
db.commit()

result=cursor.fetchall()
for x in result:
    print(x)

