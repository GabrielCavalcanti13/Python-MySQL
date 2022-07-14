import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port = 3306

connection = MySQLdb.connect(host, user, password, db, port)
cursor = connection.cursor(MySQLdb.cursors.DictCursor)


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select('fields','table', 'id=1')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
