import mysql.connector
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        # connection_timeout=5
    )

def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, username, password_hash, estado, rol
        FROM usuarios
        WHERE username=%s
    """, (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def insert_user(username, password_hash, rol="empleado"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s, %s, %s)",
        (username, password_hash, rol)
    )
    conn.commit()
    cursor.close()
    conn.close()