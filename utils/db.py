import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="mi_user_app",
        password="SrJ$110797$",
        database="mi_proyecto",
        #connection_timeout=5  # falla rápido si no responde
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