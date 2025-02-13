import json

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)
        
def abrirSalonesGruposJSON():
    with open("./bbdd_salones_grupos.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarSalonesGruposJSON(dic):
    with open("./bbdd_salones_grupos.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

def abrirNotasJSON():
    with open("./bbdd_notas.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarNotasJSON(dic):
    with open("./bbdd_notas.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicMembers={}
dicMembers=abrirMembersJSON()

dicSalonesGrupos={}
dicSalonesGrupos=abrirSalonesGruposJSON()

dicNotas={}
dicNotas=abrirNotasJSON()

def moduloReportes ():
    print("\n//////////////////////")
    print("// Reportes  //")
    print("//////////////////////")
    print("1. Ver campers en estado inscrito")
    print("2. Ver campers que aprobaron el examen inicial")
    print("3. Ver trainers que se encuentran trabajando con CampusLands")
    print("4. Ver campers con bajo rendimiento")
    print("5. Ver campers y trainers asociados a una ruta")
    print("6. Ver campers aprobados y desaprobados de un módulo")
    eleccionReportes = int(input("\n¿Qué deseas ver?: "))
    match eleccionReportes:
        case 1:
            for camperInscrito in dicMembers["campers"]:
                if camperInscrito["estado"]=="Inscrito":
                    print (f"Nombre: {camperInscrito['nombres']} {camperInscrito['apellidos']}, Estado {camperInscrito['estado']}")
        case 2:
            for camperAprobado in dicMembers["campers"]:
                if camperAprobado["estado"]=="Aprobado":
                    print(f"Nombre: {camperAprobado['nombres']} {camperAprobado['apellidos']}, Estado {camperAprobado['estado']}")
        case 3:
            for trainerCampuslands in dicMembers["trainers"]:
                print(f"Nombre: {trainerCampuslands['nombres']} {trainerCampuslands['apellidos']}")
        case 4:
            for camperBajoRendimiento in dicMembers["campers"]:
                if camperBajoRendimiento["riesgo"]=="Alto":
                    print (f"Nombre: {camperBajoRendimiento['nombres']} {camperBajoRendimiento['apellidos']}, muestra un bajo rendimiento con un riesgo {camperBajoRendimiento['riesgo']}")
        case 5:
            rutaAsociada=input("\n¿A qué ruta quieres acceder para ver los campers y trainers asociados a ella?: ")
            
            miembrosPorSalon={}
           
            for salon,datos_salon in dicSalonesGrupos['grupos'].items():
                if datos_salon['ruta']==rutaAsociada:
                    miembrosPorSalon[salon]=datos_salon['miembros']
    
            if miembrosPorSalon:
                print(f"\nMiembros asociados a la ruta '{rutaAsociada}':")
                for salon,miembros in miembrosPorSalon.items():
                    print(f"\nGrupo {salon}:")
                    for miembro in miembros:
                        print(f"- {miembro}")
            else:
                print(f"\nNo se encontraron miembros asociados a la ruta '{rutaAsociada}'")
        case 6:
            rutaAsociada=input("\n¿A qué ruta quieres acceder para ver los campers aprobados y desaprobados?: ")
            
            miembrosPorRuta={}
            
            for ruta,datos_ruta in dicSalonesGrupos['grupos'].items():
                if datos_ruta['ruta']==rutaAsociada:
                    miembrosPorRuta[ruta]=datos_ruta['miembros']
            
            moduloAsociado=input("\n¿A qué módulo quieres acceder para ver los campers aprobados y desaprobados?: ")
    
            if miembrosPorRuta:
                print(f"Miembros aprobados y desaprobados del módulo '{moduloAsociado}' de la ruta '{rutaAsociada}':")
                for salon,miembros in miembrosPorRuta.items():       
                    print(f"\nTrainer encargado: {dicSalonesGrupos["grupos"][salon]["trainer"]} / Grupo: {salon}")
                    for miembro in miembros:
                        for camperAprobadoReprobado in dicNotas:
                            if camperAprobadoReprobado==miembro:
                                if "notaFinal" in dicNotas[camperAprobadoReprobado][rutaAsociada][moduloAsociado]:
                                    if dicNotas[camperAprobadoReprobado][rutaAsociada][moduloAsociado]["notaFinal"]<60:
                                        print(f"- {miembro} / Reprobado en el módulo: '{moduloAsociado}'")
                                    else:
                                        print(f"- {miembro} / Aprobado en el módulo: '{moduloAsociado}'")
                                else:
                                    print(f"- {miembro} / Sin nota final asignada")