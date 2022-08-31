import os
from flask import Flask
import psycopg

app = Flask("ridiculosity")
host = None


@app.route('/')
def bloop():
    with psycopg.connect(f"host={host} port=5432 dbname=salt user=postgres") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                SELECT
                    *
                FROM vmware_explore.example
                ORDER BY last_stamp DESC
            ''')
            res = cur.fetchone()
            cur.execute('''INSERT INTO vmware_explore.example VALUES (CURRENT_TIMESTAMP);''')

    return "Hello dude {}".format(res)


if __name__ == "__main__":
    host=os.environ.get('DB_HOST', 'db.example.com')
    app.run('0.0.0.0', debug=True)
