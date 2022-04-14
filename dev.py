# connect python with mysql 
# use mysql-connector plugin to do this 
# ------- pip3 install mysql-connector ---------

import mysql.connector 

mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database ="python")
if(mycon):
	print("Connected")
else:
	print("Connection denied")
