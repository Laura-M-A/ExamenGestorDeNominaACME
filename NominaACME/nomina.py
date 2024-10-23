#Al generar la nómina se debe generar un archivo por cada colaborador, 
# siendo el nombre del archivo el número de identificación del colaborador. 
# El archivo debe contener la siguiente información: Identificación, nombre, 
# apellido, cargo, salario; descuento por salud, pensión y faltas al trabajo; 
# bonos extralegales y el total a pagar.
from gestorArchivos import *
from csv import *

def crearNomina():
    sumaBonos = 0

    registroEmpleados = leerArchivo()
    print("Creando Nomina para todos los empleados")
    mes = input("¿De que mes es la nomina?: ")
    for identificacion in registroEmpleados:
        try:
            faltas = registroEmpleados[identificacion]["registroInasistencia"]["falta"]
        except KeyError:
            faltas = 0
        salario = registroEmpleados[identificacion]["salario"]
        descuentoSalud = (salario * 0.04)
        descuentoPension = (salario * 0.04)
        if salario < 2000000:
            auxilioTransporte = salario - (salario * 0.1)
        else:
            auxilioTransporte = 0

        # Se descuenta el valor de un dia de trabajo, que es 1000000/30, eso da 33333,333333333 periodico.
        # Para fines practicos ese valor se redondeara a 33000, porque es mas bonito ese numero.
        descuentoFaltas = 33000 * faltas
        
        bonos = registroEmpleados[identificacion]["registroBonos"]
        for cadaBono in bonos:
            if cadaBono != []:
                sumaBonos += cadaBono[0]
            else:
                sumaBonos = 0
            print(cadaBono)
            print(sumaBonos)

        pagoTotal = salario + sumaBonos - descuentoFaltas - descuentoSalud - descuentoPension
        if pagoTotal < 0:
            pagoTotal = 0

        encabezado = ["Identificacion", "Nombre", "Apellido", "Cargo", "Salario", "Descuento por salud", "Descuento por pension", "Descuento por faltas", "Bonos", "Total a pagar"]
        nomina = [identificacion, registroEmpleados[identificacion]["nombre"], registroEmpleados[identificacion]["apellido"], registroEmpleados[identificacion]["cargo"], registroEmpleados[identificacion]["salario"], descuentoSalud, descuentoPension, descuentoFaltas, pagoTotal]

        with open(f"carpetaNomina/nominaDe{identificacion}Mes{mes}", "w") as file:
            escribirArchivo = writer(file)
            escribirArchivo.writerow(encabezado)
            escribirArchivo.writerow(nomina)
        

