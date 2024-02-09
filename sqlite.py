import sqlite3


## Connectt to SQlite
connect = sqlite3.connect('marks.db')



# Create a cursor object to insert record,create table
cursor=connect.cursor()


## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""


cursor.execute(table_info)



## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Subbu','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Raghu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Vikas','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Mahesh','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('pavan','DEVOPS','A',35)''')



## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
## Commit your changes int he databse
connect.commit()
connect.close()
