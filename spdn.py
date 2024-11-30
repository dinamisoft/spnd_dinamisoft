# Archivo principal para el proyecto de Dinamisoft

#Librerías para importar
from ast import If
import os


# variables y listados para pruebas unitarias
pacientes = [72293057,"Juan Gabriel","Serrano Anaya","Barranquilla"]



# Sección del menú Principal





# 01. Sección de Creación de Pacientes




# 02. Sección Ingresar datos de nivel de glucosa
def clasificar_presion():
  fecha = input("Ingrese la fecha (dd/mm/aaa): ")
  hora = input("Ingrese la hora (hh:mm): ")
  ayuna = input("¿Se encuentra en ayuna?: ")
  #variables para pedir los niveles de presión
  sistolica = float(input("Ingrese el nivel de presión sistólica: "))
  diastolica = float(input("Ingrese el nivel de presión diastólica: "))

  #Rangos de valores de presión para saber si es hipotensión
  if sistolica < 91 and diastolica < 63:
    print("Hipotensión\n¿Se programa la entrega? si")

  #Rangos de valores de presión para saber si es ideal
  elif 91 <= sistolica <= 134 and 63 <= diastolica <= 77:
    print("Ideal\n¿Se programa la entrega? no")

  #Rangos de valores de presión para saber si es normal
  elif 134 <= sistolica <= 162 and 77 <= diastolica <= 105:
    print("Normal\n¿Se programa la entrega? no")

  #Rangos de valores de presión para saber si es normal-alta  
  elif 162 <= sistolica <= 188 and 105 <= diastolica <= 119:
    print("Normal-alta\n¿Se programa la entrega? si")

  #Rangos de valores de presión para saber si es grado 1  
  elif 188 <= sistolica <= 201 and 119 <= diastolica <= 126:
    print("HTA Grado 1\n¿Se programa la entrega? si")

  #Rangos de valores de presión para saber si es grado2
  elif 201 <= sistolica <= 214 and 126 <= diastolica <= 146:
    print("HTA Grado 2\n¿Se programa la entrega? si")

  #Rangos de valores de presión para saber si es grado 3  
  elif sistolica >= 214 and diastolica >= 146:  
    print("HTA Grado 3\n¿Se programa la entrega? si")

  #Rangos de valores de presión para saber si es hipertencio solo sitolica  
  elif sistolica >= 152 and diastolica < 77:
    print("Hipertensión Solo Sistólica\n¿Se programa la entrega? si")
  else:
    return "Valores fuera de rango"
clasificar_presion()



# 03. Sección Consultar registros de glucosa

# Inicio del módulo de consultas
print("*********************")
print(" Módulo de Consultas")
print("*********************")
print("\nSeleccione la consulta que va a realizar")
consulta_cedula = int(input("Digite la cédula del paciente: "))
If (consulta_cedula = pacientes):
    print(pacientes)
else:
    print("No se encuentra información con la cédula ingresada.")










# 04 Sección Generar Reporte de niveles de glucosa por mes






# 05. Sección Salir del Sistema




