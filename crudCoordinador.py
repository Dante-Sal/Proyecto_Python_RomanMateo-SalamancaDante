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

def abrirSalonesGruposJSON():
    with open("./bbdd_salones_grupos.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarSalonesGruposJSON(dic):
    with open("./bbdd_salones_grupos.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicMembers={}
dicMembers=abrirMembersJSON()

dicRutas={}
dicRutas=abrirRutasJSON()

dicSalonesGrupos={}
dicSalonesGrupos=abrirSalonesGruposJSON()

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
    nuevaRuta=input("Escribe el nombre de la ruta que deseas agregar: ")
    dicRutas[nuevaRuta]={}
    szRuta=int(input("Escribe la cantidad de módulos de la ruta que deseas agregar: "))
    for i in range(szRuta):
        nuevoModulo=input(f"Escribe el nombre del módulo #{i+1}: ")
        dicRutas[nuevaRuta][nuevoModulo]={"proyecto": "",
                                          "filtro": "",
                                          "otros": ""}
        guardarRutasJSON(dicRutas)
    print("\nRuta agregada con exito.")

def eliminarCamperTrainer ():
    print("\n1. Eliminar camper")
    print("2. Eliminar trainer")
    delCampTrainer=int(input("Elige la opción a realizar: "))
    match delCampTrainer:
        case 1:
            r=True
            while r==True:
                IDcamper=int(input("\nIngresa el ID del camper a eliminar: "))
                for i in range (len(dicMembers["campers"])):
                    if i==IDcamper-1:
                        print (f"¿Estás seguro de eliminar a {dicMembers['campers'][i]['nombres']} {dicMembers['campers'][i]['apellidos']} de ID: {dicMembers['campers'][i]['id']}?")
                        print("\n1. Sí, estoy seguro")
                        print("2. No, deseo eliminar a otro camper")
                        print("3. No, deseo salir del programa")
                        confirmacionEliminarCamper=int(input("Confirma la opción: "))

                        if confirmacionEliminarCamper==1:
                            for camper in dicMembers["campers"]:
                                if camper["id"]==IDcamper:
                                    dicMembers["campers"].pop(IDcamper-1)
                                    print("Camper eliminado")
                                    guardarMembersJSON(dicMembers)
                                    r=False
                        elif confirmacionEliminarCamper==2:
                            r=True
                        else:
                            r=False
        case 2:
            r=True
            while r==True:
                IDtrainer=int(input("\nIngresa el ID del trainer a eliminar: "))
                for i in range (len(dicMembers["trainers"])):
                    if i==IDtrainer-1:
                        print (f"¿Estás seguro de eliminar a {dicMembers['trainers'][i]['nombres']} {dicMembers['trainers'][i]['apellidos']} de ID: {dicMembers['trainers'][i]['id']}?")
                        print("\n1. Sí, estoy seguro")
                        print("2. No, deseo eliminar a otro trainer")
                        print("3. No, deseo salir del programa")
                        confirmacionEliminarTrainer=int(input("Confirma la opción: "))

                        if confirmacionEliminarTrainer==1:
                            for trainer in dicMembers["trainers"]:
                                if trainer["id"]==IDtrainer:
                                    dicMembers["trainers"].pop(IDtrainer-1)
                                    print("Trainer eliminado")
                                    guardarMembersJSON(dicMembers)
                                    r=False
                        elif confirmacionEliminarTrainer==2: 
                            r=True
                        else:
                            r=False
                            
def verCampersTrainers():
    print("1. Ver listado de campers")
    print("2. Ver listado de trainers")
    eleccionVerCamperTrainer=int(input("\n¿Qué deseas ver?: "))
    match eleccionVerCamperTrainer:
        case 1:
            print("\n1. Buscar un camper segun su ID")
            print("2. Mostrar los campers cursando en un grupo")
            eleccionVerCamper=int(input("\n¿Qué quieres hacer?: "))
            if eleccionVerCamper==1:
                idCamperBuscar=int(input("Ingresa el ID del camper: "))
                for camper in dicMembers["campers"]:
                    if camper["id"]==idCamperBuscar:
                        print(f"Nombre: {camper['nombres']} {camper['apellidos']} / ID: {camper['id']}")
                        print(f"Dirección: {camper['direccion']} / Teléfono: {camper['telefono']}")
                        print(f"Estado: {camper['estado']} / Riesgo: {camper['riesgo']}")
                        print(f"Jornada: {camper['jornada']}")
            if eleccionVerCamper==2:
                for grupo in dicSalonesGrupos["grupos"]:
                    print(f"Grupo {grupo}")
                verCursoCampers=input("Ingresa el curso del cual quieres ver los campers: ")
                print("\nCampers:\n")
                for miembro in dicSalonesGrupos['grupos'][verCursoCampers]['miembros']:
                    print(f"- {miembro}")
        case 2:
            for trainer in dicMembers['trainers']:
                indiceTrainer=dicMembers["trainers"].index(trainer)
                print(f"\nNombre: {trainer['nombres']} {trainer['apellidos']} / ID: {trainer['id']}")
                print("Jornadas Disponibles: ", end="")
                contCero=0
                for jornada in dicMembers["trainers"][indiceTrainer]["jornadasDisponibles"]:
                    if jornada==0:
                        contCero+=1
                if contCero==4:
                    print("Ninguna")
                else:
                    contCero=0
                    jornadas=[]
                    for jornada in dicMembers["trainers"][indiceTrainer]["jornadasDisponibles"]:
                        if jornada!=0:
                            jornadas.append(jornada)
                    for j in range(len(jornadas)):
                        if j==len(jornadas)-1:
                            print(jornadas[j])
                        else:
                            print(jornadas[j], end=", ")
                print(f"Este trainer dicta: {','.join(trainer['rutas'])}")
                            
                
                            