from json import *

def leerArchivo():
    try:
        with open("empleados.json", "r") as file:   
            return load(file)
    except:
        return {}

def cargarArchivo(empleado):
    with open("empleados.json", "w") as file:
        dump(empleado, file, indent=4)
