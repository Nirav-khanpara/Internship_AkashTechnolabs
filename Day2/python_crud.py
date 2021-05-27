import mysql.connector 
mysqldb=mysql.connector.connect(host="localhost",user="root",password="1234")
c=mysqldb.cursor()
# c.execute("create database internship_python")

c.execute('use internship_python')
# c.execute("create table student(roll INT,name VARCHAR(255), marks INT)")

# c.execute("insert into student values(1,'Nirav',92),(2,'Prit',93),(3,'Keyur',91)")
# mysqldb.commit()

c.execute('select * from student')

result = c.fetchall();
print(result)







mysqldb.close()
