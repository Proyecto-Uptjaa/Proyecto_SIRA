from faker import Faker
import mysql.connector
import random
from datetime import date, timedelta

fake = Faker("es_ES")

# Conexión a tu BD
conexion = mysql.connector.connect(
    host="localhost",
    user="mi_user_app",
    password="SrJ$110797$",
    database="mi_proyecto"
)
cursor = conexion.cursor()

# Cantidad de empleados
NUM_EMPLEADOS = 30

# Función para generar fecha de ingreso aleatoria
def fecha_ingreso_random():
    inicio = date(2000, 1, 1)       # fecha mínima
    fin = date.today()              # fecha máxima
    dias_rango = (fin - inicio).days
    dias_random = random.randint(0, dias_rango)
    return inicio + timedelta(days=dias_random)

for i in range(NUM_EMPLEADOS):
    # Datos del empleado
    cedula = str(10000000 + i)
    nombres = fake.first_name()
    apellidos = fake.last_name()
    fecha_nac = fake.date_of_birth(minimum_age=30, maximum_age=60)
    genero = random.choice(["M", "F"])
    direccion = fake.street_address()
    num_contact = "0414" + str(random.randint(1000000, 9999999))
    correo = fake.email()
    titulo = random.choice(["T.S.U", "Bachiller", "Profesional Universitario"])
    cargo = random.choice(["COCINERA I", "COCINERA II", "DOC II", "DOC III", "DOC IV", "DOC V",
                           "DOC.(NG)/AULA", "DOC.(NG)/AULA BOLIV.", "DOC.II/AULA", "DOC. II./AULA BOLIV.",
                           "DOC. III./AULA BOLIV.", "DOC. IV/AULA BOLIV.", "DOC. V/AULA BOLIV.", "DOC. VI/AULA BOLIV.",
                           "DOC/NG", "OBRERO CERT.II", "OBRERO CERT.IV", "OBRERO GENERAL I",
                           "OBRERO GENERAL III", "PROFESIONAL UNIVERSITARIO I", "TSU", "TSU EN EDUCACIÓN",
                           "TSU EN EDUCACION BOLIV.", "TSU II"])
    fecha_ingreso = fecha_ingreso_random()
    num_carnet = str(20000 + i)
    rif = str(cedula) + "01"
    centro_votacion = fake.street_address()
    codigo_rac = str(800 + i) + "CR"

    # Insertar empleado
    cursor.execute("""
        INSERT INTO empleados
        (cedula, nombres, apellidos, fecha_nac, genero,
         direccion, num_contact, correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, codigo_rac)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (cedula, nombres, apellidos, fecha_nac, genero,
          direccion, num_contact, correo, titulo, cargo, fecha_ingreso, num_carnet, rif, centro_votacion, codigo_rac))

    id_repre = cursor.lastrowid

conexion.commit()
cursor.close()
conexion.close()

print("✅ Datos de prueba insertados correctamente.")

