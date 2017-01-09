import psycopg2
DB_CONTAINER='db_container'

def bar():
    """Returns 'bar' everytime..."""
    try:
        conn = psycopg2.connect("dbname='docker' user='postgres' host='{host}'".format(host=DB_CONTAINER))
        cur = conn.cursor()
        cur.execute("""SELECT bar from foobar where bar = 'bar';""")
        rows = cur.fetchall()
    except Exception as e:
        print("Couldn't execute query", e)
        rows = [('',)]
    finally:
        return "\n".join([str(row[0]) for row in rows])

def wont_run():
    """This function won't run"""
    pass
