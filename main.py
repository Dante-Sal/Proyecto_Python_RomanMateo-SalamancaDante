import json
from procesarCamper import procesarCamper

def abrirMembersJSON():
    with open("./bbdd_members.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
def guardarMembersJSON(dic):
    with open("./bbdd_members.json","w") as outFile:
        json.dump(dic,outFile)
dicMembers={}
dicMembers=abrirMembersJSON()



print(dicMembers)