import json
from procesarCamper import procesarCamper, procesarCamperIncompleto
from menu import *
from funcionesCoordinador import asignarNotas, asignarGrupos
from crudCoordinador import crearCamperTrainerCoordinador, editarCamperTrainerCoordinador, agregarRutaEntrenamiento, suspenderCamperTrainer
from funcionesTrainer import asignarNotasTrainer

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
ingresoUsuario=int(input("¿Cómo deseas ingresar?: "))
match ingresoUsuario:
    case 1:
        MostrarMenudeCamper()
        eleccionCamper=int(input("\nElige una opción: "))
        match eleccionCamper:
            case 1:
                print("1. Inscribirse como usuario nuevo")
                print("2. Continuar con una inscripción en progreso")
                eleccionInscripcion=int(input("\n¿Cómo deseas inscribirte?: "))
                if eleccionInscripcion==1:
                    procesarCamper()
                elif eleccionInscripcion==2:
                    procesarCamperIncompleto()
            case 2:
                print()
    case 2:
        MostrarMenudeTrainer()
        eleccionTrainer=int(input("\nElige una opción: "))
        match eleccionTrainer:
            case 1:
                print()
            case 2:
                print()
            case 3:
                asignarNotasTrainer()
    case 3:
        MostrarMenudeCoordinador()
        eleccionCoordinador=int(input("\nElige una opción: \n"))
        match eleccionCoordinador:
            case 1:
                asignarNotas()
            case 2:
                asignarGrupos()
            case 3:
                MostrarMenuCrudCoordinador()
                eleccionCRUD=int(input("\n¿Qué deseas realizar?: "))
                match eleccionCRUD:
                    case 1:
                        print()
                    case 2:
                        print()
                        crearCamperTrainerCoordinador()
                    case 3:
                        print()
                        editarCamperTrainerCoordinador()
                    case 4:
                        print()
                        suspenderCamperTrainer()
                    case 5:
                        print()
                        agregarRutaEntrenamiento()