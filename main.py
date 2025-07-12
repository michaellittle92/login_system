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
    all_users = []
    try:
        conn = get_conn()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        for result in results:
            all_users.append(result)
    except(Exception, psycopg2.Error) as error:
        print("there was an error trying to access the postgresDB.\n ", error)
    finally:
        cursor.close()
        conn.close()
        return all_users

def register_user(username, password) -> str:
    output = ""
    try:
        conn = get_conn()
        cursor = conn.cursor()
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO USERS(username, password_hash) VALUES(%s,%s)",(username, password_hash))
        conn.commit()
        return "User registered successfully"
    except psycopg2.errors.UniqueViolation:
        return "User already exists"
    except (Exception, psycopg2.Error) as error:
        return f"Database error: {error}"
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def authenticate_user(username, password) -> bool:
    conn = get_conn()
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute("SELECT password_hash from users WHERE username = %s", (username,))
    row = cursor.fetchone()

    if row and row[0] == password_hash:
        return True
    return False
   

load_dotenv()
