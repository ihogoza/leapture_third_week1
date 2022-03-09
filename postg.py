import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname='bootcamp', user='ihogoza', password='123', host='localhost')

 #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    #cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

    #cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))

    #cur.execute("SELECT * FROM student;")

    #print(cur.fetchall())
with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("SELECT * FROM student WHERE id = %s;", (5,))

        cur.execute("SELECT * FROM student;")
        print(cur.fetchall())

        # print(cur.fetchone()['name'])

        # cur.execute("INSERT INTO student (name) VALUES(%s)", ("dan",))

#conn.commit()

#cur.close()

conn.close()






# cur = conn.cursor()
# # cur.execute('CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);')
# # cur.execute('INSERT INTO student (name) VALUES(%s)', ('vava',))
# cur.execute('SELECT * FROM student;')
# print(cur.fetchall())
# conn.commit()

# conn.close()