import os
from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    counter = Counter()
    counter.increment()
    return 'Hello, world! I have been visited {0} times\n'.format(counter.get())

class Counter():
    def __init__(self):
        self.db = MySQLdb.connect(
            user = os.getenv('MYSQL_USER'),
            passwd = os.getenv('MYSQL_PASS'),
            db = 'mysql',
            host = os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
            port = int(os.getenv('MYSQL_PORT_3306_TCP_PORT'))
        )

        cur = self.db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS counters(id INT, counter INT)")

    def get(self):
        cur = self.db.cursor()
        cur.execute("SELECT * FROM counters")
        row = cur.fetchone()
        if not row:
            cur.execute("INSERT INTO counters (id, counter) VALUES (0, 0)")
            self.db.commit()
            return 0
        else:
            return row[1]

    def increment(self):
        value = self.get()
        value += 1
        cur = self.db.cursor()
        cur.execute("UPDATE counters SET counter={0} WHERE id=0".format(value))
        self.db.commit()

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)