from gestorArchivos import leerArchivo, cargarArchivo
from datetime import datetime

def registrarNuevoEmpleado(registroEmpleados):
    registroEmpleados = leerArchivo()
    identificacion = input("Escriba la identificacion del empleado: ")
    nombre = input("Escriba el nombre del empleado: ")
    apellido = input("Escriba el apelldio del empleado: ")
    cargo = input("Escriba el cargo del empleado: ")
    salario = int(input("Escriba el salario del empleado: "))
    registroEmpleados[identificacion] = {"nombre": nombre,
                                "apellido": apellido,
                                "cargo": cargo,
                                "salario": salario,
                                "registroInasistencia": {},
                                "registroBonos": []
                                }
    cargarArchivo(registroEmpleados)

def registrarInasistencia(registroEmpleados):
    registroEmpleados = leerArchivo()
    identificacion= input("Escriba el numero de identificacion del empleado: ")
    falta = int(input("Escriba la cantidad de inasistencias: "))
    fecha = str(datetime.now())
    registroEmpleados[identificacion]["registroInasistencia"] = {"falta": falta,
                                                                "fecha": fecha}
    cargarArchivo(registroEmpleados)

def registrarBonos(registroEmpleados):
    registroEmpleados = leerArchivo()
    identificacion= input("Escriba el numero de identificacion del empleado: ")
    listaBonos = registroEmpleados[identificacion]["registroBonos"]
    valor = int(input("Escriba el valor del bono: "))
    concepto = input("Escriba el concepto: ")
    fecha = str(datetime.now())
    bonos = [valor, concepto, fecha]
    listaBonos.append(bonos)
    registroEmpleados[identificacion]["registroBonos"] = listaBonos
    cargarArchivo(registroEmpleados)