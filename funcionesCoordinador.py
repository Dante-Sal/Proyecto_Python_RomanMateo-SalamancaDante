import json
from random import *
from datetime import datetime

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

dicMembers={}
dicMembers=abrirMembersJSON()

dicSalonesGrupos={}
dicSalonesGrupos=abrirSalonesGruposJSON()

def asignarNotas(): 
    for i in range(len(dicMembers["campers"])):
        if dicMembers["campers"][i]["estado"]=="Inscrito":
            print(f"Camper inscrito #{i+1}: {dicMembers['campers'][i]['nombres']} {dicMembers['campers'][i]['apellidos']}")
    idCamper=int(input("Escribir: --- "))
    notaAsignar=int(input(f"Escriba la nota a asignar al camper #{dicMembers['campers'][idCamper-1]['id']} ({dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']}): --- "))
    if notaAsignar >= 60:
        dicMembers['campers'][idCamper-1]['estado']="Aprobado"
        print(f"Camper {dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']} aprobado")
    else:
        print(f"Camper {dicMembers['campers'][idCamper-1]['nombres']} {dicMembers['campers'][idCamper-1]['apellidos']} no aprobado")
    guardarMembersJSON(dicMembers)

#Crea función
def asignarGrupos():
    o=False
    now=datetime.now()
    #Crea grupos vacíos para guardar las jornadas
    w=[];x=[];y=[];z=[]
    #Recorre las jornadas
    for p in range(4):
        #En cada jornada recorre los campers
        for q in range(len(dicMembers["campers"])):
            #Creo los grupos con cada jornada vacíos
            if q==0 and p==0:
                dicSalonesGrupos["grupos"]["w"]={}
            elif q==0 and p==1:
                dicSalonesGrupos["grupos"]["x"]={}
            elif q==0 and p==2:
                dicSalonesGrupos["grupos"]["y"]={}
            elif q==0 and p==3:
                dicSalonesGrupos["grupos"]["z"]={}
            
            for grupo in dicSalonesGrupos["grupos"]:
                if len(grupo)==2 and len(dicSalonesGrupos["grupos"][grupo]["miembros"])<33 and dicSalonesGrupos["grupos"][grupo]["jornada"]==1:
                    w.extend(dicSalonesGrupos["grupos"][grupo]["miembros"])
                    dicSalonesGrupos["grupos"]["w"]=dicSalonesGrupos["grupos"][grupo]
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                    jornadaGrupo=dicSalonesGrupos["grupos"][grupo]["jornada"]
                    if len(dicSalonesGrupos["grupos"][grupo]["trainer"].split(" "))==3:
                        nombresTrainer=dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[0]
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[1],dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[2]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    elif len(dicSalonesGrupos["grupos"][grupo]["trainer"].split(" "))==4:
                        nombresTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[0],dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[1]]
                        nombresTrainer=" ".join(nombresTrainer)
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[2],dicSalonesGrupos["grupos"][grupo]["trainer"].split(" ")[3]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    for m in range(len(dicMembers["trainers"])):
                        if dicMembers["trainers"][m]["nombres"]==nombresTrainer and dicMembers["trainers"][m]["apellidos"]==apellidosTrainer:
                            dicMembers["trainers"][m]["jornadasDisponibles"][jornadaGrupo-1]=jornadaGrupo
                            guardarMembersJSON(dicMembers)
                    if grupo in dicSalonesGrupos["salones"]["Artemis"]:
                        dicSalonesGrupos["salones"]["Artemis"][0]="w"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Sputnik"]:
                        dicSalonesGrupos["salones"]["Sputnik"][0]="w"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Apolo"]:
                        dicSalonesGrupos["salones"]["Apolo"][0]="w"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    del(dicSalonesGrupos["grupos"][grupo])
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                break
            for grupo in dicSalonesGrupos["grupos"]:
                if len(grupo)==2 and len(dicSalonesGrupos["grupos"][grupo]["miembros"])<33 and dicSalonesGrupos["grupos"][grupo]["jornada"]==2:
                    x.extend(dicSalonesGrupos["grupos"][grupo]["miembros"])
                    dicSalonesGrupos["grupos"]["x"]=dicSalonesGrupos["grupos"][grupo]
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                    jornadaGrupo=dicSalonesGrupos["grupos"][grupo]["jornada"]
                    if len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==3:
                        nombresTrainer=dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0]
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    elif len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==4:
                        nombresTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1]]
                        nombresTrainer=" ".join(nombresTrainer)
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[3]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    for m in range(len(dicMembers["trainers"])):
                        if dicMembers["trainers"][m]["nombres"]==nombresTrainer and dicMembers["trainers"][m]["apellidos"]==apellidosTrainer:
                            dicMembers["trainers"][m]["jornadasDisponibles"][jornadaGrupo-1]=jornadaGrupo
                            guardarMembersJSON(dicMembers)
                    if grupo in dicSalonesGrupos["salones"]["Artemis"]:
                        dicSalonesGrupos["salones"]["Artemis"][1]="x"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Sputnik"]:
                        dicSalonesGrupos["salones"]["Sputnik"][1]="x"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Apolo"]:
                        dicSalonesGrupos["salones"]["Apolo"][1]="x"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    del(dicSalonesGrupos["grupos"][grupo])
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                break
            for grupo in dicSalonesGrupos["grupos"]:
                if len(grupo)==2 and len(dicSalonesGrupos["grupos"][grupo]["miembros"])<33 and dicSalonesGrupos["grupos"][grupo]["jornada"]==3:
                    y.extend(dicSalonesGrupos["grupos"][grupo]["miembros"])
                    dicSalonesGrupos["grupos"]["y"]=dicSalonesGrupos["grupos"][grupo]
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                    jornadaGrupo=dicSalonesGrupos["grupos"][grupo]["jornada"]
                    if len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==3:
                        nombresTrainer=dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0]
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    elif len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==4:
                        nombresTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1]]
                        nombresTrainer=" ".join(nombresTrainer)
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[3]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    for m in range(len(dicMembers["trainers"])):
                        if dicMembers["trainers"][m]["nombres"]==nombresTrainer and dicMembers["trainers"][m]["apellidos"]==apellidosTrainer:
                            dicMembers["trainers"][m]["jornadasDisponibles"][jornadaGrupo-1]=jornadaGrupo
                            guardarMembersJSON(dicMembers)
                    if grupo in dicSalonesGrupos["salones"]["Artemis"]:
                        dicSalonesGrupos["salones"]["Artemis"][2]="y"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Sputnik"]:
                        dicSalonesGrupos["salones"]["Sputnik"][2]="y"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Apolo"]:
                        dicSalonesGrupos["salones"]["Apolo"][2]="y"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    del(dicSalonesGrupos["grupos"][grupo])
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                break
            for grupo in dicSalonesGrupos["grupos"]:
                if len(grupo)==2 and len(dicSalonesGrupos["grupos"][grupo]["miembros"])<33 and dicSalonesGrupos["grupos"][grupo]["jornada"]==4:
                    z.extend(dicSalonesGrupos["grupos"][grupo]["miembros"])
                    dicSalonesGrupos["grupos"]["z"]=dicSalonesGrupos["grupos"][grupo]
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                    jornadaGrupo=dicSalonesGrupos["grupos"][grupo]["jornada"]
                    if len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==3:
                        nombresTrainer=dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0]
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    elif len(dicSalonesGrupos["grupos"][grupo]["trainer"].split())==4:
                        nombresTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[0],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[1]]
                        nombresTrainer=" ".join(nombresTrainer)
                        apellidosTrainer=[dicSalonesGrupos["grupos"][grupo]["trainer"].split()[2],dicSalonesGrupos["grupos"][grupo]["trainer"].split()[3]]
                        apellidosTrainer=" ".join(apellidosTrainer)
                    for m in range(len(dicMembers["trainers"])):
                        if dicMembers["trainers"][m]["nombres"]==nombresTrainer and dicMembers["trainers"][m]["apellidos"]==apellidosTrainer:
                            dicMembers["trainers"][m]["jornadasDisponibles"][jornadaGrupo-1]=jornadaGrupo
                            guardarMembersJSON(dicMembers)
                    if grupo in dicSalonesGrupos["salones"]["Artemis"]:
                        dicSalonesGrupos["salones"]["Artemis"][3]="z"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Sputnik"]:
                        dicSalonesGrupos["salones"]["Sputnik"][3]="z"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    elif grupo in dicSalonesGrupos["salones"]["Apolo"]:
                        dicSalonesGrupos["salones"]["Apolo"][3]="z"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        o=True
                    del(dicSalonesGrupos["grupos"][grupo])
                    guardarSalonesGruposJSON(dicSalonesGrupos)
                break
            
            guardarSalonesGruposJSON(dicSalonesGrupos)
            #Si el camper está aprobado y su jornada coincide con la actual...
            if dicMembers["campers"][q]["estado"]=="Aprobado" and dicMembers["campers"][q]["jornada"]==p+1:
                #Si es la jornada 1, añade el camper a w, si w tiene menos o igual a 33 campers
                if p==0:
                    if len(w)<33:
                        w.append(f"{dicMembers['campers'][q]['nombres']} {dicMembers['campers'][q]['apellidos']}")
                        dicMembers["campers"][q]["estado"]="Aprobado**"
                        guardarMembersJSON(dicMembers)
                        #Le asignamos los miembros y la jornada al grupo w
                        dicSalonesGrupos["grupos"]["w"]["miembros"]=w
                        dicSalonesGrupos["grupos"]["w"]["jornada"]=1
                        dicSalonesGrupos["grupos"]["w"]["fechaDeInicio"]=f"{now.day}/{now.month}/{now.year}"
                        dicSalonesGrupos["grupos"]["w"]["fechaDeFinalizacion"]=f"{now.day}/{now.month+10}/{now.year}"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                #Si es la jornada 2, añade el camper a x, si x tiene menos o igual a 33 campers
                elif p==1:
                    if len(x)<33:
                        x.append(f"{dicMembers['campers'][q]['nombres']} {dicMembers['campers'][q]['apellidos']}")
                        dicMembers["campers"][q]["estado"]="Aprobado**"
                        guardarMembersJSON(dicMembers)
                        #Le asignamos los miembros y la jornada al grupo x
                        dicSalonesGrupos["grupos"]["x"]["miembros"]=x
                        dicSalonesGrupos["grupos"]["x"]["jornada"]=2
                        dicSalonesGrupos["grupos"]["x"]["fechaDeInicio"]=f"{now.day}/{now.month}/{now.year}"
                        dicSalonesGrupos["grupos"]["x"]["fechaDeFinalizacion"]=f"{now.day}/{now.month+10}/{now.year}"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                #Si es la jornada 3, añade el camper a y, si y tiene menos o igual a 33 campers
                elif p==2:
                    if len(y)<33:
                        y.append(f"{dicMembers['campers'][q]['nombres']} {dicMembers['campers'][q]['apellidos']}")
                        dicMembers["campers"][q]["estado"]="Aprobado**"
                        guardarMembersJSON(dicMembers)
                        #Le asignamos los miembros y la jornada al grupo y
                        dicSalonesGrupos["grupos"]["y"]["miembros"]=y
                        dicSalonesGrupos["grupos"]["y"]["jornada"]=3
                        dicSalonesGrupos["grupos"]["y"]["fechaDeInicio"]=f"{now.day}/{now.month}/{now.year}"
                        dicSalonesGrupos["grupos"]["y"]["fechaDeFinalizacion"]=f"{now.day}/{now.month+10}/{now.year}"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                #Si es la jornada 4, añade el camper a z, si z tiene menos o igual a 33 campers
                elif p==3:
                    if len(z)<33:
                        z.append(f"{dicMembers['campers'][q]['nombres']} {dicMembers['campers'][q]['apellidos']}")
                        dicMembers["campers"][q]["estado"]="Aprobado**"
                        guardarMembersJSON(dicMembers)
                        #Le asignamos los miembros y la jornada al grupo z
                        dicSalonesGrupos["grupos"]["z"]["miembros"]=z
                        dicSalonesGrupos["grupos"]["z"]["jornada"]=4
                        dicSalonesGrupos["grupos"]["z"]["fechaDeInicio"]=f"{now.day}/{now.month}/{now.year}"
                        dicSalonesGrupos["grupos"]["z"]["fechaDeFinalizacion"]=f"{now.day}/{now.month+10}/{now.year}"
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                
        #Si la jornada es la 1...
        if p==0:

            if dicSalonesGrupos["salones"]["Artemis"][p]=="" or dicSalonesGrupos["salones"]["Sputnik"][p]=="" or dicSalonesGrupos["salones"]["Apolo"][p]=="":

                for s in range(len(dicMembers["campers"])):
                    if dicMembers["campers"][s]["estado"]=="Aprobado**":
                        dicMembers["campers"][s]["estado"]="Aprobado*"
                        guardarMembersJSON(dicMembers)
            
                #Si el Artemis está vacío...
                if dicSalonesGrupos["salones"]["Artemis"][p]=="":
                    #Le asigna el grupo w a Artemis y le asigna el salón a w
                    if o==False:
                        dicSalonesGrupos["salones"]["Artemis"][p]="w"
                        dicSalonesGrupos["grupos"]["w"]["salon"]="Artemis"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Sputnik está vacío...
                elif dicSalonesGrupos["salones"]["Sputnik"][p]=="":
                    #Le asigna el grupo w a Sputnik y le asigna el salón a w
                    if o==False:
                        dicSalonesGrupos["salones"]["Sputnik"][p]="w"
                        dicSalonesGrupos["grupos"]["w"]["salon"]="Sputnik"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Apolo está vacío...
                elif dicSalonesGrupos["salones"]["Apolo"][p]=="":
                    #Le asigna el grupo w a Apolo y le asigna el salón a w
                    if o==False:
                        dicSalonesGrupos["salones"]["Apolo"][p]="w"
                        dicSalonesGrupos["grupos"]["w"]["salon"]="Apolo"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Recorre los trainers
                for i in range(len(dicMembers["trainers"])):
                    #Si la jornada actual (1) está entre los espacios vacíos en el calendario del trainer actual...
                    if p+1 in dicMembers["trainers"][i]["jornadasDisponibles"]:

                        for r in range(len(dicMembers["campers"])):
                            if dicMembers["campers"][r]["estado"]=="Aprobado*":
                                dicMembers["campers"][r]["estado"]="Cursando"
                                guardarMembersJSON(dicMembers)

                        #Extrae los nombres y apellidos del trainer en una lista
                        nombreTrainer=[dicMembers["trainers"][i]["nombres"],dicMembers["trainers"][i]["apellidos"]]
                        #Le asigna el trainer a w uniendo la lista del nombre en una sola cadena de texto
                        dicSalonesGrupos["grupos"]["w"]["trainer"]=" ".join(nombreTrainer)
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        dicMembers["trainers"][i]["jornadasDisponibles"][0]=0
                        guardarMembersJSON(dicMembers)
                        #De las rutas que dicta el trainer le asigna una aleatoria
                        dicSalonesGrupos["grupos"]["w"]["ruta"]=choice(dicMembers["trainers"][i]["rutas"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Extrae la primera letra del nombre del trainer
                        primeraLetra=dicMembers["trainers"][i]["nombres"][0]
                        #Crea un nuevo diccionario exactamente igual al w; pero con el nombre "primeraLetraDelNombreDelTrainer + Jornada actual (1)"
                        dicSalonesGrupos["grupos"][primeraLetra+(str(p+1))]=dicSalonesGrupos["grupos"]["w"]
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Borra el grupo w
                        del(dicSalonesGrupos["grupos"]["w"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)

                        #Recorre cada uno de los salones
                        for salon in dicSalonesGrupos["salones"]:
                            #Si la lista del salón actual posee un valor llamado "w"...
                            if "w" in dicSalonesGrupos["salones"][salon]:
                                #Calcula el índice de "w"
                                indiceW=dicSalonesGrupos["salones"][salon].index("w")
                                #Cambia "w" por el nombre definitivo del grupo: "primeraLetraDelNombreDelTrainer + Jornada actual (1)"
                                dicSalonesGrupos["salones"][salon][indiceW]=primeraLetra+(str(p+1))
                                guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Si encuentra un trainer disponible rompe el ciclo
                        break

                    else:
                        if i==len(dicMembers["trainers"])-1:
                            del(dicSalonesGrupos["grupos"]["w"])

            else:
                del(dicSalonesGrupos["grupos"]["w"])

        #Si la jornada es la 2...        
        elif p==1:

            if dicSalonesGrupos["salones"]["Artemis"][p]=="" or dicSalonesGrupos["salones"]["Sputnik"][p]=="" or dicSalonesGrupos["salones"]["Apolo"][p]=="":

                for s in range(len(dicMembers["campers"])):
                    if dicMembers["campers"][s]["estado"]=="Aprobado**":
                        dicMembers["campers"][s]["estado"]="Aprobado*"
                        guardarMembersJSON(dicMembers)

                #Si el Artemis está vacío...
                if dicSalonesGrupos["salones"]["Artemis"][p]=="":
                    #Le asigna el grupo x a Artemis y le asigna el salón a x
                    if o==False:
                        dicSalonesGrupos["salones"]["Artemis"][p]="x"
                        dicSalonesGrupos["grupos"]["x"]["salon"]="Artemis"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Sputnik está vacío...
                elif dicSalonesGrupos["salones"]["Sputnik"][p]=="":
                    #Le asigna el grupo x a Sputnik y le asigna el salón a x
                    if o==False:
                        dicSalonesGrupos["salones"]["Sputnik"][p]="x"
                        dicSalonesGrupos["grupos"]["x"]["salon"]="Sputnik"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Apolo está vacío...
                elif dicSalonesGrupos["salones"]["Apolo"][p]=="":
                    #Le asigna el grupo x a Apolo y le asigna el salón a x
                    if o==False:
                        dicSalonesGrupos["salones"]["Apolo"][p]="x"
                        dicSalonesGrupos["grupos"]["x"]["salon"]="Apolo"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Recorre los trainers
                for i in range(len(dicMembers["trainers"])):
                    #Si la jornada actual (2) está entre los espacios vacíos en el calendario del trainer actual...
                    if p+1 in dicMembers["trainers"][i]["jornadasDisponibles"]:

                        for r in range(len(dicMembers["campers"])):
                            if dicMembers["campers"][r]["estado"]=="Aprobado*":
                                dicMembers["campers"][r]["estado"]="Cursando"
                                guardarMembersJSON(dicMembers)

                        #Extrae los nombres y apellidos del trainer en una lista
                        nombreTrainer=[dicMembers["trainers"][i]["nombres"],dicMembers["trainers"][i]["apellidos"]]
                        #Le asigna el trainer a x uniendo la lista del nombre en una sola cadena de texto
                        dicSalonesGrupos["grupos"]["x"]["trainer"]=" ".join(nombreTrainer)
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        dicMembers["trainers"][i]["jornadasDisponibles"][1]=0
                        guardarMembersJSON(dicMembers)
                        #De las rutas que dicta el trainer le asigna una aleatoria
                        dicSalonesGrupos["grupos"]["x"]["ruta"]=choice(dicMembers["trainers"][i]["rutas"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Extrae la primera letra del nombre del trainer
                        primeraLetra=dicMembers["trainers"][i]["nombres"][0]
                        #Crea un nuevo diccionario exactamente igual al x; pero con el nombre "primeraLetraDelNombreDelTrainer + Jornada actual (2)"
                        dicSalonesGrupos["grupos"][primeraLetra+(str(p+1))]=dicSalonesGrupos["grupos"]["x"]
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Borra el grupo x
                        del(dicSalonesGrupos["grupos"]["x"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)

                        #Recorre cada uno de los salones
                        for salon in dicSalonesGrupos["salones"]:
                            #Si la lista del salón actual posee un valor llamado "x"...
                            if "x" in dicSalonesGrupos["salones"][salon]:
                                #Calcula el índice de "x"
                                indiceX=dicSalonesGrupos["salones"][salon].index("x")
                                #Cambia "x" por el nombre definitivo del grupo: "primeraLetraDelNombreDelTrainer + Jornada actual (2)"
                                dicSalonesGrupos["salones"][salon][indiceX]=primeraLetra+(str(p+1))
                                guardarSalonesGruposJSON(dicSalonesGrupos)      
                        #Si encuentra un trainer disponible rompe el ciclo
                        break

                    else:
                        if i==len(dicMembers["trainers"])-1:
                            del(dicSalonesGrupos["grupos"]["x"])
            
            else:
                del(dicSalonesGrupos["grupos"]["x"])

        #Si la jornada es la 3...             
        elif p==2:

            if dicSalonesGrupos["salones"]["Artemis"][p]=="" or dicSalonesGrupos["salones"]["Sputnik"][p]=="" or dicSalonesGrupos["salones"]["Apolo"][p]=="":

                for s in range(len(dicMembers["campers"])):
                    if dicMembers["campers"][s]["estado"]=="Aprobado**":
                        dicMembers["campers"][s]["estado"]="Aprobado*"
                        guardarMembersJSON(dicMembers)
            
                #Si el Artemis está vacío...
                if dicSalonesGrupos["salones"]["Artemis"][p]=="":
                    #Le asigna el grupo y a Artemis y le asigna el salón a y
                    if o==False:
                        dicSalonesGrupos["salones"]["Artemis"][p]="y"
                        dicSalonesGrupos["grupos"]["y"]["salon"]="Artemis"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Sputnik está vacío...
                elif dicSalonesGrupos["salones"]["Sputnik"][p]=="":
                    #Le asigna el grupo y a Sputnik y le asigna el salón a y
                    if o==False:
                        dicSalonesGrupos["salones"]["Sputnik"][p]="y"
                        dicSalonesGrupos["grupos"]["y"]["salon"]="Sputnik"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Apolo está vacío...    
                elif dicSalonesGrupos["salones"]["Apolo"][p]=="":
                    #Le asigna el grupo y a Apolo y le asigna el salón a y
                    if o==False:
                        dicSalonesGrupos["salones"]["Apolo"][p]="y"
                        dicSalonesGrupos["grupos"]["y"]["salon"]="Apolo"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Recorre los trainers
                for i in range(len(dicMembers["trainers"])):
                    #Si la jornada actual (3) está entre los espacios vacíos en el calendario del trainer actual...
                    if p+1 in dicMembers["trainers"][i]["jornadasDisponibles"]:

                        for r in range(len(dicMembers["campers"])):
                            if dicMembers["campers"][r]["estado"]=="Aprobado*":
                                dicMembers["campers"][r]["estado"]="Cursando"
                                guardarMembersJSON(dicMembers)

                        #Extrae los nombres y apellidos del trainer en una lista
                        nombreTrainer=[dicMembers["trainers"][i]["nombres"],dicMembers["trainers"][i]["apellidos"]]
                        #Le asigna el trainer a y uniendo la lista del nombre en una sola cadena de texto
                        dicSalonesGrupos["grupos"]["y"]["trainer"]=" ".join(nombreTrainer)
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        dicMembers["trainers"][i]["jornadasDisponibles"][2]=0
                        guardarMembersJSON(dicMembers)
                        #De las rutas que dicta el trainer le asigna una aleatoria
                        dicSalonesGrupos["grupos"]["y"]["ruta"]=choice(dicMembers["trainers"][i]["rutas"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Extrae la primera letra del nombre del trainer
                        primeraLetra=dicMembers["trainers"][i]["nombres"][0]
                        #Crea un nuevo diccionario exactamente igual al y; pero con el nombre "primeraLetraDelNombreDelTrainer + Jornada actual (3)"
                        dicSalonesGrupos["grupos"][primeraLetra+(str(p+1))]=dicSalonesGrupos["grupos"]["y"]
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Borra el grupo y
                        del(dicSalonesGrupos["grupos"]["y"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)

                        #Recorre cada uno de los salones
                        for salon in dicSalonesGrupos["salones"]:
                            #Si la lista del salón actual posee un valor llamado "y"...
                            if "y" in dicSalonesGrupos["salones"][salon]:
                                #Calcula el índice de "y"
                                indiceY=dicSalonesGrupos["salones"][salon].index("y")
                                #Cambia "y" por el nombre definitivo del grupo: "primeraLetraDelNombreDelTrainer + Jornada actual (3)"
                                dicSalonesGrupos["salones"][salon][indiceY]=primeraLetra+(str(p+1))
                                guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Si encuentra un trainer disponible rompe el ciclo
                        break

                    else:
                        if i==len(dicMembers["trainers"])-1:
                            del(dicSalonesGrupos["grupos"]["y"])
            
            else:
                del(dicSalonesGrupos["grupos"]["y"])

        #Si la jornada es la 4...          
        elif p==3:

            if dicSalonesGrupos["salones"]["Artemis"][p]=="" or dicSalonesGrupos["salones"]["Sputnik"][p]=="" or dicSalonesGrupos["salones"]["Apolo"][p]=="":

                for s in range(len(dicMembers["campers"])):
                    if dicMembers["campers"][s]["estado"]=="Aprobado**":
                        dicMembers["campers"][s]["estado"]="Aprobado*"
                        guardarMembersJSON(dicMembers)
            
                #Si el Artemis está vacío...
                if dicSalonesGrupos["salones"]["Artemis"][p]=="":
                    #Le asigna el grupo z a Artemis y le asigna el salón a z
                    if o==False:
                        dicSalonesGrupos["salones"]["Artemis"][p]="z"
                        dicSalonesGrupos["grupos"]["z"]["salon"]="Artemis"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Sputnik está vacío...
                elif dicSalonesGrupos["salones"]["Sputnik"][p]=="":
                    #Le asigna el grupo z a Sputnik y le asigna el salón a z
                    if o==False:
                        dicSalonesGrupos["salones"]["Sputnik"][p]="z"
                        dicSalonesGrupos["grupos"]["z"]["salon"]="Sputnik"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Si el Apolo está vacío...    
                elif dicSalonesGrupos["salones"]["Apolo"][p]=="":
                    #Le asigna el grupo z a Apolo y le asigna el salón a z
                    if o==False:
                        dicSalonesGrupos["salones"]["Apolo"][p]="z"
                        dicSalonesGrupos["grupos"]["z"]["salon"]="Apolo"
                    guardarSalonesGruposJSON(dicSalonesGrupos)

                #Recorre los trainers
                for i in range(len(dicMembers["trainers"])):
                    #Si la jornada actual (4) está entre los espacios vacíos en el calendario del trainer actual...
                    if p+1 in dicMembers["trainers"][i]["jornadasDisponibles"]:

                        for r in range(len(dicMembers["campers"])):
                            if dicMembers["campers"][r]["estado"]=="Aprobado*":
                                dicMembers["campers"][r]["estado"]="Cursando"
                                guardarMembersJSON(dicMembers)

                        #Extrae los nombres y apellidos del trainer en una lista
                        nombreTrainer=[dicMembers["trainers"][i]["nombres"],dicMembers["trainers"][i]["apellidos"]]
                        #Le asigna el trainer a z uniendo la lista del nombre en una sola cadena de texto
                        dicSalonesGrupos["grupos"]["z"]["trainer"]=" ".join(nombreTrainer)
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        dicMembers["trainers"][i]["jornadasDisponibles"][3]=0
                        guardarMembersJSON(dicMembers)
                        #De las rutas que dicta el trainer le asigna una aleatoria
                        dicSalonesGrupos["grupos"]["z"]["ruta"]=choice(dicMembers["trainers"][i]["rutas"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Extrae la primera letra del nombre del trainer
                        primeraLetra=dicMembers["trainers"][i]["nombres"][0]
                        #Crea un nuevo diccionario exactamente igual al z; pero con el nombre "primeraLetraDelNombreDelTrainer + Jornada actual (4)"
                        dicSalonesGrupos["grupos"][primeraLetra+(str(p+1))]=dicSalonesGrupos["grupos"]["z"]
                        guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Borra el grupo z
                        del(dicSalonesGrupos["grupos"]["z"])
                        guardarSalonesGruposJSON(dicSalonesGrupos)

                        #Recorre cada uno de los salones
                        for salon in dicSalonesGrupos["salones"]:
                            #Si la lista del salón actual posee un valor llamado "z"...
                            if "z" in dicSalonesGrupos["salones"][salon]:
                                #Calcula el índice de "z"
                                indiceZ=dicSalonesGrupos["salones"][salon].index("z")
                                #Cambia "z" por el nombre definitivo del grupo: "primeraLetraDelNombreDelTrainer + Jornada actual (4)"
                                dicSalonesGrupos["salones"][salon][indiceZ]=primeraLetra+(str(p+1))
                                guardarSalonesGruposJSON(dicSalonesGrupos)
                        #Si encuentra un trainer disponible rompe el ciclo
                        break

                    else:
                        if i==len(dicMembers["trainers"])-1:
                            del(dicSalonesGrupos["grupos"]["z"])
            
            else:
                del(dicSalonesGrupos["grupos"]["z"])
    
    #Vacía los grupos w, x, y, z
    w=[];x=[];y=[];z=[]
    #Guarda los datos en la base de datos
    guardarSalonesGruposJSON(dicSalonesGrupos)

def inicio_sesion_coordinador():
    usuario=input("Indica tu usuario de coordinador: ")
    contrasena=input("Indica tu contraseña: ")

    for i in range(len(dicMembers["coordinadores"])):
            
        if dicMembers["coordinadores"][i]["usuario"] == usuario and dicMembers["coordinadores"][i]["contrasena"] == contrasena:
            print("Inicio de sesión exitoso ✅")
            return True
        else:
            print("Usuario o contraseña incorrecta ❌")
            return False