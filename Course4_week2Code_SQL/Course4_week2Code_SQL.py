import sqlite3

conn = sqlite3.connect('emailDB.sqlite')  # make a connection
cur = conn.cursor()  # send SQL command to the cursor and get the results back through the same cursor

cur.execute('DROP TABLE IF EXISTS Counts')  # use cur.execute('') for the SQL command

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox1.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # If we just want to know the user name, use:  email.split('@')[1]

    #  this question mark is a placeholder
    #  And this is a way to basically make sure that we don't allow SQL injection
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))

    # another way to write the following code, see
    # https://www.coursera.org/learn/python-databases/lecture/18SJ4/worked-example-counting-email-in-a-database
    try:
        #  FYI: https://blog.csdn.net/Jian_Yun_Rui/article/details/73692331
        count = cur.fetchone()[0]  # take the count value, if None, then break
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    except:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email, ))
    conn.commit()


# print out contants of the table in emailDB in order

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in conn.execute(sqlstr):
    print(row[0], row[1])

conn.close()  # close the connection
