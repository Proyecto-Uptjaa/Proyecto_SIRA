import db
from security import hash_password

def crear_usuario_inicial():
    username = "jorgeDev"   # cámbialo si quieres
    password = "jdjd1997"  # cámbiala por algo fuerte
    rol = "super_admin"

    # Generar hash
    hashed = hash_password(password)

    # Insertar en la BD
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s, %s, %s)",
        (username, hashed, rol)
    )
    conn.commit()
    cursor.close()
    conn.close()

    print(f"Usuario {username} creado con rol {rol}")

if __name__ == "__main__":
    crear_usuario_inicial()