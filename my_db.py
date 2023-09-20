import pymysql
def mysql_conn():
    dataBase = pymysql.connect(
        host = 'localhost',
        user = 'root', 
        password = 'arin'
    )

    cur = dataBase.cursor()
    cur.execute('create database crm_db')
    print("all done")


if __name__ == "__main__":
    mysql_conn()

