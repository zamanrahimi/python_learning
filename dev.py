# connect python with mysql 
# use mysql-connector plugin to do this 
# ------- pip3 install mysql-connector ---------

import mysql.connector 

mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database ="python")
if(mycon):
	print("Connected")
else:
	print("Connection denied")


# Execution section ---- list tables from python databse 

myc = mycon.cursor()
li = myc.execute("show tables")
results = myc.fetchall()
for r in results:
  print (r)
  
# --------- Insert data into the emp1 table -----------
li = myc.execute("insert into emp1 values(2, 'Khan')")
mycon.commit()




