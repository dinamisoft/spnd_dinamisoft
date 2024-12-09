# Archivo principal para el proyecto de Dinamisoft

#Librerías para importar
import sys # Esta librería es para los acentos y caracteres especiales
sys.stdout.reconfigure(encoding='utf-8') # formato para mostrar caracteres espciales y acentos

import os

# variables y listados para pruebas unitarias
#pacientes = [72293057,"Juan Gabriel","Serrano Anaya","Barranquilla"]


# 01. Sección de Creación de Pacientes
def registro_pacientes():
    global id, nombres, apellidos, direccion, telefono, barrio, ciudad, departamento
    print("Digite sus datos personales a continuacion")
    id = int(input("Ingrese su numero de documento: "))
    nombres = str(input("Ingrese sus nombres: "))
    apellidos = str(input("Ingrese sus apellidos: "))
    direccion = str(input("Ingrese su direccion: "))
    telefono = int(input("Ingrese su numero de telefono: "))
    barrio = str(input("Ingrese el nombre de su barrio: "))
    ciudad = str(input("Ingrese la ciudad: "))
    departamento = str(input("Ingrese el departamento: "))
    print()
    print("La persona registrada es",nombres, "con apellidos",apellidos, "y documento", id) 
    print ("con direccion", direccion, "telefono", telefono, "del barrio", barrio, "de la ciudad" , ciudad, "y departamento del ", departamento)



# 02. Sección Ingresar datos de nivel de glucosa
def clasificar_presion():
  #datos fecha hora
  global fecha, hora, ayuna, sistolica, diastolica
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


# 03. Sección Consultar registros de glucosa

# Inicio del módulo de consultas
def consultar_registros():
  print("*********************")
  print(" Módulo de Consultas")
  print("*********************")
  print("\nSeleccione la consulta que va a realizar")
  consulta_cedula = int(input("Digite la cédula del paciente: "))
  if(consulta_cedula == id):
    print("Información del Paciente")
    print("\nIdentificación: ",id,"\nNombres: ", nombres,'\nApellidos: ',apellidos)
    print("Dirección: ",direccion,"\nTeléfono: ",telefono,"\nBarrio: ",barrio,"\nCiudad: ",ciudad,"\nDepartamento: ",departamento)
    print("\nREGISTRO DE NIVELES DE GLUCOSA")
    print("\nFECHA: ",fecha,"\nHORA: ",hora,"\nEN AYUNAS: ",ayuna)
    print("\nVALORESPRESIÓN SISTÓLICA: ",sistolica,"\nPRESIÓN DIASTÓLICA: ", diastolica)
  else:
    print("No se encuentra información con la cédula ingresada.")



# 04 Sección Generar Reporte de niveles de glucosa por mes

def reportes():
  print("Sección de reportes")



# Sección del menú Principal

# Función para mostrar el menú principal con las opciones disponibles
def menu():
        print("\n******************** Bienvenido a S.P.D.N ********************")
        print("\nA continuación, por favor elige una opción: ")
        print("1). Registrar paciente.")  
        print("2). Ingresar datos de nivel de Presion: ")  
        print("3). Consultar mis registros de Presion: ")  
        print("4). Generar un reporte de niveles de Presion por mes")  
        print("5). Salir del sistema.")  

# Función principal para manejar el menú
def menu_principal():

        while True:  # Bucle  para mostrar el menú hasta que el usuario decida salir
                menu()  # Llama a la función menu para mostrar las opciones
                try:
                        opcion = int(input("Elige una opción del 1 al 5: "))  
                except ValueError:  # Maneja el error si el usuario no ingresa un número válido
                        print ("Por favor ingresa un número válido")
                        continue  # Regresa al inicio del bucle para mostrar el menú nuevamente
                if (opcion == 1):
                                registro_pacientes()  # Llama a la función para registrar pacientes
                elif (opcion == 2):
                                clasificar_presion()  # Llama a la función para ingresar datos de presión
                elif (opcion == 3):
                                consultar_registros()  # Llama a la función para consultar registros de presión
                elif (opcion == 4):
                                reportes()  # Llama a la función para generar reportes
                elif (opcion == 5):
                                print ("Saliendo del sistema!")  # Mensaje de salida
                                break  # Rompe el bucle para terminar el programa
                else:
                                print ("Solo hay opciones del 1 al 5")  # Mensaje de error para opciones fuera de rango



# Llama a la función principal para iniciar el programa
menu_principal()


# 05. Sección Salir del Sistema
print("Gracias por utilizar nuestro sistema")


