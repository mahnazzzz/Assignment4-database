import sys
import mysql.connector

def myconnect(user, pw):
        conn = mysql.connector.connect( host='localhost', database='world',user=user, password=pw)
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