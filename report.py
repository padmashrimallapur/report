#!/usr/local/bin/python
"""
Creating the report of top 50 domains for 30 days

It is assumed that mailing table is repopulated every day.
The report will display the top 50 domain sorting with their growth percentage.
"""

import MySQLdb
import datetime

mysqlconfig = {'host': 'localhost',
               'username': 'root',
               'password': 'mysqlroot',
               'dbName': 'indexdb'}


def __test_insert():
    conn = connection()
    cur = conn.cursor()

    cur.execute("TRUNCATE mailing")
    conn.commit()

    for i in range(0, 10):
        insert = "INSERT INTO mailing (addr) VALUES ('id%s@xyz.com')" % i
        cur.execute(insert)

    for i in range(0, 5):
        insert = "INSERT INTO mailing (addr) VALUES ('id%s@abc.com')" % i
        cur.execute(insert)

    for i in range(0, 25):
        insert = "INSERT INTO mailing (addr) VALUES ('id%s@test.com')" % i
        cur.execute(insert)

    conn.commit()


def connection():
    conn = MySQLdb.connect(mysqlconfig['host'],
                           mysqlconfig['username'],
                           mysqlconfig['password'],
                           mysqlconfig['dbName'])
    return conn


def daterange():
    previous_month_day = datetime.datetime.now() - datetime.timedelta(days=30)
    earlier = previous_month_day.strftime("%Y-%m-%d")
    current_day = datetime.datetime.now().strftime("%Y-%m-%d")
    return earlier, current_day


def updateDomains(today):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT addr FROM mailing")
    for email in cursor.fetchall():
        domain = email[0].split("@")[1]
        cursor.execute("SELECT count FROM domain_count WHERE domain = %s AND date = %s", (domain, today))
        count = cursor.fetchone()
        if count is not None:
            count = count[0] + 1
            cursor.execute("UPDATE domain_count SET count= %s WHERE domain = %s AND date = %s", (count, domain, today))
        else:
            count = 1
            cursor.execute("INSERT INTO domain_count (domain, count, date)VALUES (%s, %s, %s)", (domain, count, today))

    conn.commit()


def printReport(fromdate, todate):

    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(COUNT) FROM domain_count")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT count,domain FROM `domain_count` WHERE date> %s or date< %s ORDER BY count DESC LIMIT 50",
                   (fromdate, todate))

    total_domains = cursor.fetchall()
    if len(total_domains) > 0:
        print("Top 50 domains of last 30 days")
        fmt = "{0}{1}{0}{2}{0}".format("+", "-"*14, "-"*13)
        print fmt
        print "{0} {1:9} {0:>4} {2:>4} {0}".format("|", "Domain", "Growth in %")
        print fmt
        for row in total_domains:
            growth = (row[0] * 100) / total
            print "{0} {1:9} {0:>4} {2:>4} {0:>7}".format("|", row[1], round(growth, 2))
    else:
        print "No data available"

if __name__ == '__main__':

    #This is only for test insert...
    __test_insert()

    earlier_str, today = daterange()
    updateDomains(today)
    printReport(earlier_str, today)
