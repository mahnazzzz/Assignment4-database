import sys
import mysql.connector

def myconnect(root, password):
        conn = mysql.connector.connect( host='127.0.0.1', database='classicmodels',user=root, password=password)
        conn.autocommit = True
        return conn

rootconn = myconnect('root','deterentysker!42snapsnap')

def sqlQuery(sqlString, conn=rootconn):
    try:
        cursor = conn.cursor()
        cursor.execute(sqlString)
        res = cursor.fetchall()
        return res
    except Exception as ex:
        print(str(ex), file=sys.stderr)
    finally:
        cursor.close()

def sqlDo(sqlString, conn=rootconn):
    try:
        cursor = conn.cursor()
        cursor.execute(sqlString)
        res = cursor.fetchwarnings()
        return res
    except Exception as ex:
        print(str(ex), file=sys.stderr)
    finally:
        cursor.close()

"Done"
