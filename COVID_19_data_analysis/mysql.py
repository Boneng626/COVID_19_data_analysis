import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='626626626',
                             db='User')

# 获取游标
cursor = connection.cursor()

# 创建数据表


cursor.execute("drop table if exists users")
table = cursor.execute('''
CREATE TABLE `Users` (
  `id` CHAR(32),
  `user_name` CHAR(32),
  `password` CHAR(32),
  PRIMARY KEY (`user_name`)
)
''')

sql = """INSERT INTO Users (id, user_name, password)VALUES
                  (1, 'A', 'aaa'),
                  (2, 'B', 'bbb'),
                  (3, 'C', 'ccc');"""
cursor.execute(sql)
connection.commit()

# 增
def insertData(id, user_name, password):
    sql = "INSERT INTO Users VALUES(%(id)s,%(user_name)s, %(password)s)"
    value = {"id":id,
             "user_name":user_name,
             "password":password,
            }
    cursor.execute(sql, value)
    connection.commit()
    print("successfully insert")

# 删
def deleteData(user_name):
    sql = "DELETE FROM Users WHERE user_name = '%s'" % (user_name)
    cursor.execute(sql)
    connection.commit()
    print("successfully delete")


# 查
def findData(user_name):
   sql = "SELECT * FROM Users \
       WHERE user_name = '%s'" % (user_name)
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      ID = row[0]
      name = row[1]
      password = row[2]
       # 打印结果
      print ("id=%s,user_name=%s,password=%s" % \
             (ID, name, password ))
#改
def resetPasswprd(user_name):
    sql = "UPDATE Users SET password = 'default' WHERE user_name = '%s'" % (user_name)
    cursor.execute(sql)
    connection.commit()
    print('Successfully reset password')

'''
if __name__ == '__main__':
    #insertData(cursor, '1', 'A', '001')
    #insertData(cursor, '2', 'B', '002')
    insertData( '3', 'C', 'ccc')
    deleteData('B')
    findData('A')
    resetPasswprd('A')
    findData('A')

    cursor.close()
    connection.close()
'''
