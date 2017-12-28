
#an Example of how to create  MYSQL function using Python MYSQL DB connector
#another usefull tool to work with DBS is SQL ALCHEMY just for notice

import MySQLdb

db = MySQLdb.connect(host="My Host",    # your host, usually localhost
                     user="My User",         # your username
                     passwd="My PAss",  # your password
                     db="DB name ASK your DBA")        # na

cursor = db.cursor()

#creating function
cursor.execute(" CREATE FUNCTION GETFULLNAME(fname CHAR(250),lname CHAR(250))     RETURNS CHAR(250)    BEGIN         DECLARE fullname CHAR(250);        SET fullname=CONCAT(fname,' ',lname);        RETURN fullname;    END  ;")

db.commit()

#executing the functions
cursor.execute("SELECT GETFULLNAME("'"avi "'","'"grainik"'") as myname;")

result=cursor.fetchall()
for x in result:
    print(x)


