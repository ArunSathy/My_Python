import pymysql

mydb=pymysql.connect(host='localhost',user='root',password='Arun23@1998',database='python')

x=mydb.cursor()

x.execute(' create table data(name varchar(20),age int)')

x.close()