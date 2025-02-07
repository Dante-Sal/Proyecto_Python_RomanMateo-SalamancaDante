import json

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile)

dicMembers={}
dicMembers=abrirMembersJSON()

def actualizarInfo(camperNuevo):
    dicMembers["campers"].pop()
    dicMembers["campers"].append(camperNuevo)

def procesarCamper():
    camperNuevo={}
    camperNuevo["estado"]=""
    camperNuevo["nombres"]=input("Ingrese su/s nombre/s: ")
    camperNuevo["estado"]="En proceso de ingreso"
    dicMembers["campers"].append(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["apellidos"]=input("Ingrese sus apellidos: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["direccion"]=input("Ingrese su dirección: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["telefono"]=input("Ingrese su número de teléfono: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["acudiente"]={}
    camperNuevo["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["acudiente"]["telefono"]=input("Ingrese el número de teléfono del acudiente: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["riesgo"]="Bajo"
    camperNuevo["estado"]="Inscrito"
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
