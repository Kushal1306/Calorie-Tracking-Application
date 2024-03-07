import psycopg2
import os

def connect_db():
    try:
        return psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="123456", port=5432)
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise

def execute_query(query, values=None):
    try:
        conn = connect_db()
        cur = conn.cursor()
        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def execute_query2(query, values=None):
    try:
        conn = connect_db()
        cur = conn.cursor()
        if values:
            cur.execute(query, values)
        else:
            cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

def execute_query3(query, values=None):
    # query="select calories,meal_type,entry_date from calorie_entries where userid=2 order by entry_date"
      
    try:
        conn = connect_db()
        cur = conn.cursor()
        # if values:
        #     cur.execute(query, values)
        # else:
        cur.execute(query)
        #result = cur.fetchall()
        file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\output.csv'
        if os.path.exists(file_path):
           os.remove(file_path)
        with open(file_path, "w") as csv_file:
            cur.copy_expert(f"COPY ({query}) TO STDOUT WITH CSV HEADER;", csv_file)
        #csv_file_path = "/path/to/your/output.csv"
        # conn.commit()
        cur.close()
        conn.close()
        # return result
    except psycopg2.Error as e:
        print("Error executing query:", e)
        raise

