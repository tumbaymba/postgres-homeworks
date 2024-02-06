"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

file_emp = 'north_data/employees_data.csv'
file_cust = 'north_data/customers_data.csv'
file_ord = 'north_data/orders_data.csv'

emp = []
cust = []
ord = []

with open(file_ord, newline='') as orders_file:
    reader = csv.DictReader(orders_file)
    for row in reader:
        row_list_orders = list(row.values())
        ord.append(row_list_orders)

with open(file_emp, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row_list = list(row.values())
        emp.append(row_list)

with open(file_cust, newline='') as cust_file:
    reader = csv.DictReader(cust_file)
    for row in reader:
        row_list_cust = list(row.values())
        cust.append(row_list_cust)

conn = psycopg2.connect(host="localhost", dbname="north", user="postgres", password="Rhts1428")

cur = conn.cursor()
cur.executemany("INSERT INTO employees VALUES(%s,%s,%s,%s,%s,%s)", emp)
cur.executemany("INSERT INTO customers VALUES(%s,%s,%s)", cust)
cur.executemany("INSERT INTO orders VALUES(%s,%s,%s,%s,%s)", ord)
conn.commit()

cur.close()
conn.close()


