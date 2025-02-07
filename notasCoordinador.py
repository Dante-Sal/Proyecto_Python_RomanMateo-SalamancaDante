import json

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicMembers={}
dicMembers=abrirMembersJSON()

def asignarNotas():
    dicMembers = abrirMembersJSON()
    for i in range(len(dicMembers["campers"])):
        if dicMembers["campers"][i]["estado"]=="Inscrito":
            print(f"Estudiante inscrito #{i+1}: {dicMembers['campers'][i]['nombres']} {dicMembers['campers'][i]['apellidos']}")
    idCamper=int(input("Escribir: --- "))
    notaAsignar=int(input(f"Escriba la nota a asignar al estudiante #{dicMembers['campers'][idCamper-1]['id']} ({dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']}): --- "))
    if notaAsignar >= 60:
        dicMembers['campers'][idCamper-1]['estado']="Aprobado"
        print(f"Estudiante {dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']} aprobado")
    else:
        print(f"Estudiante {dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']} no aprobado")
    guardarMembersJSON(dicMembers)

#def asignarGrupos():
