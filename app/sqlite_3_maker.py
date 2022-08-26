import sqlite3
conn=sqlite3.connect("messages.db")
c=conn.cursor()

c.execute("""CREATE TABLE messages (user text,message text)""")
#c.execute("""INSERT INTO messages VALUES ("ashish","me")""")
#conn.commit()

c.execute("""SELECT * FROM messages""")
msg=c.fetchall()
print(msg)