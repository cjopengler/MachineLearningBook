# coding:utf-8

import MySQLdb


cxn = MySQLdb.connect(user='root', passwd='1qaz2wsx', db='test')

cur = cxn.cursor()

cur.execute('''CREATE TABLE users (login VARCHAR(8), uid INT)''')
cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('jane', 7001)")
cur.execute("INSERT INTO users VALUES('bob', 7200)")

cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")

for data in cur.fetchall():
    print '%s\t%s' % data
    
cxn.close()
