from faker import Faker
import mysql.connector
import random
from datetime import date

fake = Faker("es_ES")

# Conexión a tu BD
conexion = mysql.connector.connect(
    host="localhost",
    user="mi_user_app",
    password="SrJ$110797$",
    database="mi_proyecto"
)
cursor = conexion.cursor()

# Cantidad de representantes y estudiantes
NUM_REPRESENTANTES = 200
MAX_HIJOS_POR_REPRE = 3

for i in range(NUM_REPRESENTANTES):
    # Datos del representante
    cedula_repre = str(10000000 + i)
    nombres_repre = fake.first_name()
    apellidos_repre = fake.last_name()
    fecha_nac_repre = fake.date_of_birth(minimum_age=30, maximum_age=60)
    genero_repre = random.choice(["M", "F"])
    direccion_repre = fake.street_address()
    num_contact_repre = "0414" + str(random.randint(1000000, 9999999))
    correo_repre = fake.email()

    # Insertar representante
    cursor.execute("""
        INSERT INTO representantes
        (cedula_repre, nombres_repre, apellidos_repre, fecha_nac_repre, genero_repre,
         direccion_repre, num_contact_repre, correo_repre)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (cedula_repre, nombres_repre, apellidos_repre, fecha_nac_repre, genero_repre,
          direccion_repre, num_contact_repre, correo_repre))

    id_repre = cursor.lastrowid

    # Cada representante tendrá entre 1 y 3 hijos
    for j in range(random.randint(1, MAX_HIJOS_POR_REPRE)):
        cedula_est = str(20000000 + i*10 + j)
        nombres = fake.first_name()
        apellidos = fake.last_name()
        fecha_nac_est = fake.date_of_birth(minimum_age=6, maximum_age=17)
        city = random.choice(["PLC", "BNA", "LCH"])
        genero = random.choice(["M", "F"])
        direccion = fake.street_address()
        num_contact = "0412" + str(random.randint(1000000, 9999999))
        correo_estu = fake.email()
        grado = random.choice(["1", "2", "3", "4", "5", "6"])
        seccion = random.choice(["A", "B", "C"])
        docente = "Prof. " + fake.last_name()
        TallaC = random.choice(["S", "M", "L"])
        TallaP = str(random.randint(28, 36))
        TallaZ = str(random.randint(34, 42))

        # Campos padre/madre ficticios
        padre = fake.first_name_male()
        padre_ci = str(30000000 + random.randint(0, 9999))
        madre = fake.first_name_female()
        madre_ci = str(31000000 + random.randint(0, 9999))

        cursor.execute("""
            INSERT INTO estudiantes
            (cedula, nombres, apellidos, fecha_nac_est, city, genero,
             direccion, num_contact, correo_estu, grado, seccion, docente,
             TallaC, TallaP, TallaZ, padre, padre_ci, madre, madre_ci, representante_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (cedula_est, nombres, apellidos, fecha_nac_est, city, genero,
              direccion, num_contact, correo_estu, grado, seccion, docente,
              TallaC, TallaP, TallaZ, padre, padre_ci, madre, madre_ci, id_repre))

conexion.commit()
cursor.close()
conexion.close()

print("✅ Datos de prueba insertados correctamente.")