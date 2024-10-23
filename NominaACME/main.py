from gestorArchivos import *
from registros import *
from nomina import crearNomina

def menu():
    print
    print("Bienvenido al gestor de nomina de ACME")
    print("Menu")
    print("(1) Registro de empleados")
    print("(2) Registro de inasistencia")
    print("(3) Registro de bonos extra-legales")
    print("(4) Calculo de la nomina")
    opc = input("Escriba la opcion que desea realizar: ")
    print
    return opc

opc = ""
registroEmpleados = {}

while opc != "0":
    opc = menu()
    match opc:
        case "1":
            registrarNuevoEmpleado(registroEmpleados)

        case "2":
            registrarInasistencia(registroEmpleados)

        case "3":
            registrarBonos(registroEmpleados)

        case "4":
            crearNomina()
            
        case "0":
            opc = "0"
            print("Saliendo del programa...")
        case _:
            print("Dato invalido, intentelo de nuevo")

