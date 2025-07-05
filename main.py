import hashlib
import os
import psycopg2
from dotenv import load_dotenv


def hash_password(password): 
    return hashlib.sha256(password.encode()).hexdigest()

def get_conn():
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    conn_str = f"host={host} dbname={dbname} user={user} password={password}"
    return psycopg2.connect(conn_str)

def get_all_users():
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        for result in results:
            print(f"id: {result[0]}")
            print(f"username: {result[1]}")
            print(f"password_hash: {result[2]}")
    except(Exception, psycopg2.Error) as error:
        print("there was an error trying to access the postgresDB.\n ", error)
    finally:
        cursor.close()
        conn.close()

def register(username, password):
    try:
        conn = get_conn()
        cursor = conn.cursor()
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO USERS(username, password_hash) VALUES(%s,%s)",(username, password_hash))
        conn.commit()
    except psycopg2.errors.UniqueViolation:
        print("User already exists")
    except(Exception, psycopg2.Error) as error:
        print("there was an error trying to access the postgresDB.\n ", error)
    finally:
        cursor.close()
        conn.close()

def log_in(username, password):
    conn = get_conn()
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute("SELECT password_hash from users WHERE username = %s", (username,))
    row = cursor.fetchone()

    if row[0] == password_hash:
        print("login succesful")
    else:
        print("login failue")
   

load_dotenv()



#register("test_user", "this_is_my_password")
#get_all_users()

log_in("michael", "password")
