README
============================================================

Name: Report 
Version: 1.0
Author:	Padmashri Mallapur

Description:
	It is assumed that mailing table is repopulated every day.The report will display the top 50 domain sorting with their growth percentage.

System requiremetns:
	1. python 2.7
	2. mysql (mysql-5.6)

Installation:
	1. install database on server using script.sql
	
Example of deployment:
	1. Install mysql database
		mysql -u root -p < script.sql
		

To run: 
	python report.py

sample output:

Top 50 domains of last 30 days
+--------------+-------------+
| Domain       | Growth in % |
+--------------+-------------+
| xyz.com      | 47.06       |
| test.com     | 29.41       |
| abc.com      | 23.53       |
	
============================================================

