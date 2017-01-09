import psycopg2
DB_CONTAINER='db_container'

def foo():
    """Returns 'foo' everytime..."""
    if 1 == 2:
        pass
    try:
        conn = psycopg2.connect("dbname='docker' user='postgres' host='{host}'".format(host=DB_CONTAINER))
        cur = conn.cursor()
        cur.execute("""SELECT foo from foobar where foo = 'foo';""")
        rows = cur.fetchall()
    except Exception as e:
        print("Couldn't execute query", e)
        rows = [('',)]
    finally:
        return "\n".join([str(row[0]) for row in rows])
