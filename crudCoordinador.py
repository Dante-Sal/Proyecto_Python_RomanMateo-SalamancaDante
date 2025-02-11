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

    elif agregarCamperTrainer==2:
        
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

def editarCamperTrainerCoordinador():
    editarCamperTrainer=int(input("\nDeseas editar un camper o un trainer? (1/2): "))

    if editarCamperTrainer==1:

        idCamperEdit=int(input("Ingrese el ID del camper a editar: "))
        for i in range(dicMembers["campers"]):
            if dicMembers["campers"][i]["id"]==idCamperEdit:
                print("\n//////////////////////")
                print("// MENÚ DE EDICIÓN  //")
                print("//////////////////////")
                print("1. Editar estado")
                print("2. Editar nombres")
                print("3. Editar apellidos")
                print("4. Editar dirección")
                print("5. Editar teléfono")
                print("6. Editar acudiente")
                print("7. Editar jornada")
                claveEditC=int(input(f"¿Qué deseas editar del camper {dicMembers['campers'][i]['id']}?"))
                match claveEditC:
                    case 1:
                        if dicMembers["campers"][i]["estado"]=="En proceso de ingreso":
                            print("No es posible editar el estado de este camper")

                        elif dicMembers["campers"][i]["estado"]=="Inscrito":
                            aprobado=input(f"¿Cambiar estado a 'Aprobado'? (S: Sí/N: No): ").upper()
                            if aprobado=="S":
                                dicMembers["campers"][i]["estado"]="Aprobado"

                        elif dicMembers["campers"][i]["estado"]=="Aprobado" or dicMembers["campers"][i]["estado"]=="Aprobado*" or dicMembers["campers"][i]["estado"]=="Aprobado**":
                            inscrito=input(f"¿Cambiar estado a 'Inscrito'? (S: Sí/N: No): ").upper()
                            if inscrito=="S":
                                dicMembers["campers"][i]["estado"]="Inscrito"

                        elif dicMembers["campers"][i]["estado"]=="Cursando":
                            expulsado=input(f"¿Cambiar estado a 'Expulsado'? (S: Sí/N: No): ").upper()
                            if expulsado=="S":
                                dicMembers["campers"][i]["estado"]="Expulsado"
                            else:
                                retirado=input(f"¿Cambiar estado a 'Retirado'? (S: Sí/N: No): ").upper()
                                if retirado=="S":
                                    dicMembers["campers"][i]["estado"]="Retirado"
                        
                        elif dicMembers["campers"][i]["estado"]=="Graduado":
                            print("No es posible editar el estado de este camper")
                        
                        elif dicMembers["campers"][i]["estado"]=="Expulsado" or dicMembers["campers"][i]["estado"]=="Retirado":
                            cursando=input(f"¿Cambiar estado a 'Cursando'? (S: Sí/N: No): ").upper()
                            if cursando=="S":
                                dicMembers["campers"][i]["estado"]="Cursando"

                    case 2:
                        dicMembers["campers"][i]["nombres"]=input("Ingrese el/los nombre/s del camper: ")
                    case 3:
                        dicMembers["campers"][i]["apellidos"]=input("Ingrese los apellidos del camper: ")
                    case 4:
                        dicMembers["campers"][i]["direccion"]=input("Ingrese la dirección del camper: ")
                    case 5:
                        dicMembers["campers"][i]["telefono"]=input("Ingrese el teléfono del camper: ")
                    case 6:
                        print("\n/////////////////////////////")
                        print("//MENÚ DE EDICIÓN ACUDIENTE  //")
                        print("//////////////////////////////")
                        print("1. Editar nombres")
                        print("2. Editar apellidos")
                        print("3. Editar teléfono")
                        claveAcudienteEdit=int(input(f"¿Qué deseas editar del acudiente del camper {dicMembers['campers'][i]['id']}?"))
                        match claveAcudienteEdit:
                            case 1:
                                dicMembers["campers"][i]["acudiente"]["nombres"]=input("Ingrese el/los nombre/s del acudiente: ")
                            case 2:
                                dicMembers["campers"][i]["acudiente"]["apellidos"]=input("Ingrese los apellidos del acudiente: ")
                            case 3:
                                dicMembers["campers"][i]["acudiente"]["telefono"]=input("Ingrese el teléfono del acudiente: ")
                    case 7:
                        dicMembers["campers"][i]["jornada"]=input("Ingrese la jornada en la que estudiará el camper: ")

        else:
            print("El camper ingresado no existe...")

    elif editarCamperTrainer==2:

        idTrainerEdit=int(input("Ingrese el ID del trainer a editar: "))
        for i in range(dicMembers["trainers"]):
            if dicMembers["trainers"][i]["id"]==idTrainerEdit:
                print("\n//////////////////////")
                print("// MENÚ DE EDICIÓN  //")
                print("//////////////////////")
                print("1. Editar nombres")
                print("2. Editar apellidos")
                print("3. Editar jornadas disponibles")
                print("4. Editar rutas")
                claveEditT=int(input(f"¿Qué deseas editar del trainer {dicMembers['trainers'][i]['id']}?"))
                match claveEditT:
                    case 1:
                        dicMembers["trainers"][i]["nombres"]=input("Ingrese el/los nombre/s del trainer: ")
                    case 2:
                        dicMembers["trainers"][i]["apellidos"]=input("Ingrese los apellidos del trainer: ")
                    case 3:

                        dicMembers["trainers"][i]["jornadasDisponibles"]=[]
                        nuevoTrainerJornada1=input("¿El trainer tiene disponible la jornada 1? (S: Sí/N: No): ").upper()
                        if nuevoTrainerJornada1=="S":
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(1)
                        else:
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(0)
                        nuevoTrainerJornada2=input("¿El trainer tiene disponible la jornada 2? (S: Sí/N: No): ").upper()
                        if nuevoTrainerJornada2=="S":
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(2)
                        else:
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(0)
                        nuevoTrainerJornada3=input("¿El trainer tiene disponible la jornada 3? (S: Sí/N: No): ").upper()
                        if nuevoTrainerJornada3=="S":
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(3)
                        else:
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(0)
                        nuevoTrainerJornada4=input("¿El trainer tiene disponible la jornada 4? (S: Sí/N: No): ").upper()
                        if nuevoTrainerJornada4=="S":
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(4)
                        else:
                            dicMembers["trainers"][i]["jornadasDisponibles"].append(0)

                    case 4:

                        dicMembers["trainers"][i]["rutas"]=[]
                        for ruta in dicRutas:
                            rutaActual=input(f"¿El trainer dicta ruta {ruta}? (S: Sí/N: No): ").upper()
                            if rutaActual=="S":
                                dicMembers["trainers"][i]["rutas"].append(ruta)

def agregarRutaEntrenamiento():
    nuevaRutaEntrenamiento=input("Escribe el nombre de la ruta que deseas agregar: ")
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

def suspenderCamperTrainer ():
    print("\n1. Suspender Camper.")
    print("2. Suspender Trainer.")
    suspCampTrainer = int(input("Elige la opcion a realizar: "))
    match suspCampTrainer:
        case 1:
            bul = True
            while bul == True:
                IDcamperTrainer = int(input("\nIngresa el ID del camper a suspender: "))
                for i in range (len(dicMembers["campers"])):
                    if i == IDcamperTrainer:
                        print (f"Estas segur@ de suspender a {dicMembers['campers'][i-1]['nombres']} {dicMembers['campers'][i-1]['apellidos']} de ID: {dicMembers['campers'][i-1]['id']}?")
                        print("\n1. Si, estoy seguro.")
                        print("2. No, deseo suspender a otro camper.")
                        confirmacionSuspenderCamper = input("Confirma la opcion: ")

                        if confirmacionSuspenderCamper == 1: 
                            for camper in dicMembers["campers"]:
                                if camper["id"] == IDcamperTrainer:
                                    camper["estado"] = "suspendido"
                                    bul = False
                        elif confirmacionSuspenderCamper == 2:
                            IDcamperTrainer = int(input("\nIngresa el ID del camper a suspender: "))
                            bul = True
                        else:
                            print("Solo puedes elegir una de las opciones anteriores")
                            bul = True
                            
                
                           