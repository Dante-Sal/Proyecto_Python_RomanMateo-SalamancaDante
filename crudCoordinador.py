import json

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

def abrirRutasJSON():
    with open("./rutasModulos.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarRutasJSON(dic):
    with open("./rutasModulos.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicRutas={}
dicRutas=abrirRutasJSON()
        
dicMembers={}
dicMembers=abrirMembersJSON()

def crearCamperTrainerCoordinador():
    agregarCamperTrainer=int(input("\nDeseas agregar un camper o un trainer? (1/2): "))
    if agregarCamperTrainer==1:
        nuevoCamperNombre=input("Indica el nombre del camper nuevo: ")
        nuevoCamperApellido=input("Indica los apellidos del camper nuevo: ")
        nuevoCamperDireccion=input("Indica la direccion del camper nuevo: ")
        nuevoCamperTelefono=input("Indica el telefono del camper nuevo: ")
        nuevoCamperJornada=input("Indica la jornada en la que estará el camper nuevo: ")

        nuevoCamperAcudienteN=input("Indica el nombre del acudiente: ")
        nuevoCamperAcudienteA=input("Indica los apellidos del acudiente: ")
        nuevoCamperAcudienteT=input("Indica el telefono del acudiente: ")

        nuevoID=len(dicMembers["campers"])

        nuevoAcudiente={
            "nombres": nuevoCamperAcudienteN,
            "apellidos": nuevoCamperAcudienteA,
            "telefono": nuevoCamperAcudienteT
        }

        nuevoCamper={
            "id": nuevoID+1,
            "estado": "Inscrito",
            "riesgo": "Bajo",
            "nombres": nuevoCamperNombre,
            "apellidos": nuevoCamperApellido,
            "direccion": nuevoCamperDireccion,
            "telefono": nuevoCamperTelefono,   
            "acudiente": nuevoAcudiente,
            "jornada": nuevoCamperJornada
        }

        dicMembers["campers"].append(nuevoCamper)
        guardarMembersJSON(dicMembers)

    if agregarCamperTrainer==2:
        
        nuevoTrainerNombre=input("Indica el nombre del trainer nuevo: ")
        nuevoTrainerApellido=input("Indica los apellidos del trainer nuevo: ")
        jornadasDispo=[]
        nuevoTrainerJornada1=input("¿El trainer tiene disponible la jornada 1? (S: Sí/N: No): ").upper()
        if nuevoTrainerJornada1=="S":
            jornadasDispo.append(1)
        else:
            jornadasDispo.append(0)
        nuevoTrainerJornada2=input("¿El trainer tiene disponible la jornada 2? (S: Sí/N: No): ").upper()
        if nuevoTrainerJornada2=="S":
            jornadasDispo.append(2)
        else:
            jornadasDispo.append(0)
        nuevoTrainerJornada3=input("¿El trainer tiene disponible la jornada 3? (S: Sí/N: No): ").upper()
        if nuevoTrainerJornada3=="S":
            jornadasDispo.append(3)
        else:
            jornadasDispo.append(0)
        nuevoTrainerJornada4=input("¿El trainer tiene disponible la jornada 4? (S: Sí/N: No): ").upper()
        if nuevoTrainerJornada4=="S":
            jornadasDispo.append(4)
        else:
            jornadasDispo.append(0)

        rutasNuevo=[]
        for ruta in dicRutas:
            rutaActual=input(f"¿El trainer dicta ruta {ruta}? (S: Sí/N: No): ").upper()
            if rutaActual=="S":
                rutasNuevo.append(ruta)

        nuevoID=len(dicMembers["trainers"])

        nuevoTrainer={
            "id": nuevoID+1,
            "nombres": nuevoTrainerNombre,
            "apellidos": nuevoTrainerApellido,
            "jornadasDisponibles": jornadasDispo,
            "rutas": rutasNuevo
        }

        dicMembers["trainers"].append(nuevoTrainer)
        guardarMembersJSON(dicMembers)
        print ("Trainer agregado con exito :)")

"""def editarCamperTrainerCoordinador():
    editarCamperTrainer=int(input("\nDeseas editar un camper o un trainer? (1/2): "))
    if editarCamperTrainer==1:
        idCamperEdit=int(input("Ingrese el ID del camper a editar: "))
        for i in range(dicMembers["camper"]):
            if dicMembers["campers"][i]["id"]==idCamperEdit:"""

def agregarRutaEntrenamiento():
    abrirRutasJSON
    nuevaRutaEntrenamiento = input("Escribe el nombre de la ruta que deseas agregar: ")
    nuevoModulo1 = input("Escribe el primer modulo de esta ruta: ")
    nuevoModulo2 = input("Escribe el segundo modulo de la ruta: ")
    tercerModuloeleccion = input("Hay un tercer modulo?(S/N): ")
    match tercerModuloeleccion:
        case "S":
            nuevoModulo3 = input("Escribe el tercer modulo de la ruta: ")

            nuevaRuta = {nuevaRutaEntrenamiento: [
                nuevoModulo1, nuevoModulo2, nuevoModulo3
            ]}
            
            dicRutas["rutas"].append(nuevaRuta)
            print ("\nRuta agregada con exito.")
        case "N":
            nuevaRuta = {nuevaRutaEntrenamiento: [
                nuevoModulo1, nuevoModulo2
            ]}

            dicRutas["rutas"].append(nuevaRuta)
            print ("\nRuta agregada con exito.")
    guardarRutasJSON(dicRutas)
    return ""