
#import mysql.connector
#import os
# mysql -u root -p < C:\Users\wings\OneDrive\Bureau\Moduler.Akp\Modulerdb.sql
# mysql --user="root" --password="" < C:\Users\wings\OneDrive\Bureau\Moduler.Akp\Modulerdb.sql
from LibrayManager import *

def conSimpl():
	db_state = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password ="",
		#database= "python_db"
	)
	return conSimpl

def condb(ctodb):
	db_state = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password ="",
		database= ctodb
	)
	return db_state


def pycondb(ctodb):
	db_state = pymysql.connect(
		host = "localhost",
		user = "root",
		password ="",
		database= ctodb
	)
	return db_state

def conCreatDb():
	#fullreq = 
	os.system('mysql --user="root" --password="" < C:/Users/wings/OneDrive/Bureau/Moduler.Akp/Modulerdb.sql')
	return conCreatDb



def conCreatDbWith(USER, PWD, FILE):
	pass



