import json
from procesarCamper import procesarCamper,procesarCamperIncompleto
from menu import *
from notasCoordinador import asignarNotas

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicMembers={}
dicMembers=abrirMembersJSON()
MostrarMenudeIngreso()
ingresoUsuario = int(input("Como deseas ingresar?: "))
match ingresoUsuario:
    case 1:
        MostrarMenudeCamper()
        eleccionCamper = int(input("\nElige una opcion: "))
        match eleccionCamper:
            case 1:
                print("1. Inscribirse como usuario nuevo.")
                print("2. Continuar con una inscripcion en progreso. ")
                eleccionInscripcion = int(input("\nComo deseas inscribirte?: "))
                if eleccionInscripcion == 1:
                    procesarCamper()
                elif eleccionInscripcion == 2:
                    procesarCamperIncompleto()

                
            case 2:
                print
    
    case 2:
        MostrarMenudeTrainer()        
    case 3:
        MostrarMenudeCoordinador()
        eleccionCoordinador = int(input("\nElige una opcion: "))
        match eleccionCoordinador:
            case 1:
                asignarNotas()