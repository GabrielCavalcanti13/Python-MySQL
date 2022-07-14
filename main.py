import MySQLdb

host = "localhost"
user = "aplication"
password = "123456"
db = "school"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)


def select(cursor, fields, tables, where=None):
    query = "SELECT {} FROM {}".format(fields, tables)
    if where:
        query = "{} WHERE {}".format(query, where)
    cursor.execute(query)
    return cursor.fetchall()


def insert(cursor, connection, values, table, fields=None):
    query = "INSERT INTO {} ".format(table)
    if fields:
        query = "{} ({})".format(query, fields)
    query = "{} VALUES {}".format(query, ",".join(["(" + i + ")" for i in values]))

    cursor.execute(query)
    connection.commit()


def update(cursor, connection, sets, table, where=None):
    query = "UPDATE {}".format(table)
    query = "{} SET {}". format(query, ",".join([field + "= '" + value + "'" for field, value in sets.items()]))
    if where:
        query = "{} WHERE {}".format(query, where)

    cursor.execute(query)
    connection.commit()


def delete(cursor, connection, table, where):
    query = "DELETE FROM {} WHERE {}".format(table, where)
    cursor.execute(query)
    connection.commit()

