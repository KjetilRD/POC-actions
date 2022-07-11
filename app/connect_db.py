import os
import psycopg2


def connect():

    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute(
          "Select * from test_01")
        res = cur.fetchall()
        conn.commit()
        print(res)
        return res


def connect_ins_sel():

    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        res = cur.fetchall()
        conn.commit()
        print(res)
        cur.execute(
          "create table if not exists test_01 ( col1 int)")
        cur.execute(
          "Insert into test_01 select 10")
        cur.execute(
          "Insert into test_01 select 20")
        cur.execute(
          "Select * from test_01")
        res = cur.fetchall()
        conn.commit()
        print(res)
        return res


def log():

    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute(
          "create table if not exists log_msg  (log_time timestamp, log_message varchar(2000))")
        cur.execute(
          "Insert into log_msg select now(), 'Test log'")
        conn.commit()
        print(res)
        return res


def print_log:

    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    with conn.cursor() as cur:
        cur.execute("SELECT * from log_msg")
        res = cur.fetchall()
        conn.commit()
        print(res)


log()
connect()
log()
print_log()
