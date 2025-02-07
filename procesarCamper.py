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

def actualizarInfo(camperNuevo):
    dicMembers["campers"].pop()
    dicMembers["campers"].append(camperNuevo)

def procesarCamper():
    camperNuevo={}
    ultimoID=dicMembers["campers"][-1]["id"]
    camperNuevo["id"]=ultimoID+1
    camperNuevo["estado"]=""
    camperNuevo["riesgo"]="Bajo"
    camperNuevo["nombres"]=input("Ingrese su/s nombre/s: ")
    camperNuevo["apellidos"]=input("Ingrese sus apellidos: ")
    camperNuevo["estado"]="En proceso de ingreso"
    dicMembers["campers"].append(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["direccion"]=input("Ingrese su dirección: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["telefono"]=input("Ingrese su número de teléfono: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["acudiente"]={}
    camperNuevo["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
    camperNuevo["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
    camperNuevo["acudiente"]["telefono"]=input("Ingrese el número de teléfono del acudiente: ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["jornada"]=input("Ingrese la jornada en la que quiera estudiar: \n1 --- 6 a.m. - 10 a.m.\n2 --- 10 a.m. - 2 p.m.\n3 --- 2 p.m. - 6 p.m.\n4 --- 6 p.m. - 10 p.m.\nEscribir: --- ")
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)
    camperNuevo["estado"]="Inscrito"
    actualizarInfo(camperNuevo)
    guardarMembersJSON(dicMembers)

def procesoDireccion(camperIncompleto):
    camperIncompleto["direccion"]=input("Ingrese su dirección: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["telefono"]=input("Ingrese su número de teléfono: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["acudiente"]={}
    camperIncompleto["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
    camperIncompleto["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
    camperIncompleto["acudiente"]["telefono"]=input("Ingrese el número de teléfono del acudiente: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["jornada"]=input("Ingrese la jornada en la que quiera estudiar: \n1 --- 6 a.m. - 10 a.m.\n2 --- 10 a.m. - 2 p.m.\n3 --- 2 p.m. - 6 p.m.\n4 --- 6 p.m. - 10 p.m.\nEscribir: --- ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["estado"]="Inscrito"
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)

def procesoTelefono(camperIncompleto):
    camperIncompleto["telefono"]=input("Ingrese su número de teléfono: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["acudiente"]={}
    camperIncompleto["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
    camperIncompleto["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
    camperIncompleto["acudiente"]["telefono"]=input("Ingrese el número de teléfono del acudiente: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["jornada"]=input("Ingrese la jornada en la que quiera estudiar: \n1 --- 6 a.m. - 10 a.m.\n2 --- 10 a.m. - 2 p.m.\n3 --- 2 p.m. - 6 p.m.\n4 --- 6 p.m. - 10 p.m.\nEscribir: --- ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["estado"]="Inscrito"
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)

def procesoAcudiente(camperIncompleto):
    camperIncompleto["acudiente"]={}
    camperIncompleto["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
    camperIncompleto["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
    camperIncompleto["acudiente"]["telefono"]=input("Ingrese el número de teléfono del acudiente: ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["jornada"]=input("Ingrese la jornada en la que quiera estudiar: \n1 --- 6 a.m. - 10 a.m.\n2 --- 10 a.m. - 2 p.m.\n3 --- 2 p.m. - 6 p.m.\n4 --- 6 p.m. - 10 p.m.\nEscribir: --- ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["estado"]="Inscrito"
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)

def procesoJornada(camperIncompleto):
    camperIncompleto["jornada"]=input("Ingrese la jornada en la que quiera estudiar: \n1 --- 6 a.m. - 10 a.m.\n2 --- 10 a.m. - 2 p.m.\n3 --- 2 p.m. - 6 p.m.\n4 --- 6 p.m. - 10 p.m.\nEscribir: --- ")
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)
    camperIncompleto["estado"]="Inscrito"
    actualizarInfo(camperIncompleto)
    guardarMembersJSON(dicMembers)

def procesarCamperIncompleto():
    print("\nEscriba el número de la inscripción incompleta que desee llenar: ")

    for i in range(len(dicMembers["campers"])):
        if dicMembers["campers"][i]["estado"]=="En proceso de ingreso":
            print(f"Archivo de inscripción incompleto #{i+1}: {dicMembers['campers'][i]['nombres']} {dicMembers['campers'][i]['apellidos']}")

    archivo=int(input("Escribir: --- "))
    if len(dicMembers["campers"][archivo-1])==5:
        procesoDireccion(dicMembers["campers"][archivo-1])
    elif len(dicMembers["campers"][archivo-1])==6:
        procesoTelefono(dicMembers["campers"][archivo-1])
    elif len(dicMembers["campers"][archivo-1])==7:
        procesoAcudiente(dicMembers["campers"][archivo-1])
    elif len(dicMembers["campers"][archivo-1])==8:
        procesoJornada(dicMembers["campers"][archivo-1])