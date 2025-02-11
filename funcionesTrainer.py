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

def asignarNotasTrainer():
    for grupo in dicSalonesGrupos["grupos"]:
        print(f"Grupo {grupo}")
    opcionGrupo=input("¿A qué grupo le quieres asignar notas?: --- ")
    for i in range(len(dicSalonesGrupos["grupos"][opcionGrupo]["miembros"])):
        print(f"Camper #{i+1} del grupo {opcionGrupo}: {dicSalonesGrupos['grupos'][opcionGrupo]['miembros'][i]}")
    opcionCamper=int(input("¿A qué camper le quieres asignar notas?: --- "))
    for camper in dicNotas:
        if camper==dicSalonesGrupos["grupos"][opcionGrupo]["miembros"][opcionCamper-1]:
            for ruta in dicNotas[camper]:
                if dicSalonesGrupos["grupos"][opcionGrupo]["ruta"]==ruta:
                    c=0
                    claves=list(dicNotas[camper][ruta].keys())
                    for modulo in dicNotas[camper][ruta]:
                        claveActual=claves[c]
                        if dicNotas[camper][ruta][modulo]["proyecto"]!="" and dicNotas[camper][ruta][modulo]["filtro"]!="" and dicNotas[camper][ruta][modulo]["otros"]!="":
                            print(f"Módulo {claveActual} calificado... (Nota: {dicNotas[camper][ruta][modulo]['notaFinal']})")
                            c+=1
                        else:
                            print(f"Módulo {claveActual} sin calificar...")
                            break
                    calificarModulo=input(f"¿Calificar módulo {claveActual} del estudiante {dicSalonesGrupos['grupos'][opcionGrupo]['miembros'][opcionCamper-1]}? (Sí: S/No: N): ")
                    if calificarModulo=="S":
                        notaProyecto=int(input("Ingrese la nota del proyecto: "))
                        dicNotas[camper][ruta][modulo]["proyecto"]=notaProyecto
                        notaFiltro=int(input("Ingrese la nota del filtro: "))
                        dicNotas[camper][ruta][modulo]["filtro"]=notaFiltro
                        notaOtros=int(input("Ingrese la nota final de otras actividades: "))
                        dicNotas[camper][ruta][modulo]["otros"]=notaOtros
                        notaFinal=notaProyecto*0.6+notaFiltro*0.3+notaOtros*0.1
                        dicNotas[camper][ruta][modulo]["notaFinal"]=notaFinal
                        total=0
                        suma=0
                        for final in dicNotas[camper][ruta]:
                            if dicNotas[camper][ruta][final]["proyecto"]!="" and dicNotas[camper][ruta][final]["filtro"]!="" and dicNotas[camper][ruta][final]["otros"]!="":
                                suma+=dicNotas[camper][ruta][final]["notaFinal"]
                                total+=1
                            else:
                                break
                        promedioFinal=suma/total
                        if promedioFinal<60:
                            for j in range(len(dicMembers["campers"])):
                                if (f"{dicMembers['campers'][j]['nombres']} {dicMembers['campers'][j]['apellidos']}")==camper:
                                    dicMembers["campers"][j]["riesgo"]="Alto"
                                    print(f"Riesgo del camper {dicMembers['campers'][j]['nombres']} actualizado a {dicMembers['campers'][j]['riesgo']}")
                        elif promedioFinal<80:
                            for j in range(len(dicMembers["campers"])):
                                if (f"{dicMembers['campers'][j]['nombres']} {dicMembers['campers'][j]['apellidos']}")==camper:
                                    dicMembers["campers"][j]["riesgo"]="Medio"
                                    print(f"Riesgo del camper {dicMembers['campers'][j]['nombres']} actualizado a {dicMembers['campers'][j]['riesgo']}")
                        elif promedioFinal>80:
                            for j in range(len(dicMembers["campers"])):
                                if (f"{dicMembers['campers'][j]['nombres']} {dicMembers['campers'][j]['apellidos']}")==camper:
                                    dicMembers["campers"][j]["riesgo"]="Bajo"
                                    print(f"Riesgo del camper {dicMembers['campers'][j]['nombres']} actualizado a {dicMembers['campers'][j]['riesgo']}")
    guardarMembersJSON(dicMembers)
    guardarNotasJSON(dicNotas)