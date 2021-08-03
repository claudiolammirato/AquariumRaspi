import mysql.connector as mysql
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import pass

def connection():
    # enter your server IP address/domain name
    HOST = "remotemysql.com" # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = pass.database
    # this is the user you create
    USER = pass.username
    # user password
    PASSWORD = pass.password
    # connect to MySQL server
    connection.db = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    print("Connected to:", connection.db.get_server_info())
    # enter your code here!)

def close():
    connection.db.close()


def createTable():
    connection()
    DB_NAME = pass.database

    TABLES = {}
    TABLES['employees'] = (
        "CREATE TABLE `employees` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ") ENGINE=InnoDB")
    cursor = connection.db.cursor()
    try:
        print("Creating table {}: ".format('employees'), end='')
        cursor.execute(TABLES['employees'])
    except mysql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    cursor.close()
    close()

def addItem():
    connection()
    cursor = connection.db.cursor()
    tomorrow = datetime.now().date() + timedelta(days=1)
    add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")

    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid
    

    # Make sure data is committed to the database
    connection.db.commit()

    cursor.close()
    close()
    
def retrieveData():
    connection()

    cursor = connection.db.cursor()

    query = ("SELECT first_name, last_name, hire_date FROM employees "
            "WHERE hire_date BETWEEN %s AND %s")

    hire_start = date(1999 , 1, 1)
    hire_end = date(2030 , 12, 31)

    cursor.execute(query, (hire_start, hire_end))

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))

    cursor.close()
    close()

