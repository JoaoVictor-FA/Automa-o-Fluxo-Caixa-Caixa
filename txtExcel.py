from decimal import Decimal


def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

x = readFile("extrato.txt")
retorno = []
for i in x:
    saida = ""
    tratar = i.split(";")
    tratar.pop(0)
    tratar.pop(1)
    rende = False
    if tratar[1] == '"REM BASICA"' or tratar[1] == '"CRED JUROS"':
        rende = True
        des = "Rendimentos"
    tratar.pop(1)
    if tratar[0] == '"Data_Mov"':
        continue
    tratar[0] = tratar[0].replace('"','')
    ano = ""
    mes = ""
    dia = ""
    i = 0
    for n in tratar[0]:
        if i<4:
                ano += n
        elif i<6:
                mes += n
        else:
                dia += n
        i += 1
    data = dia + "/" + mes + "/" + ano
    if len(retorno) > 0 and rende and retorno[len(retorno)-1].split(";")[1] == "Rendimentos" and retorno[len(retorno)-1].split(";")[0] == data:
        temp = Decimal(retorno[len(retorno)-1].split(";")[2])
        temp += Decimal(tratar[1].replace('"','') + "\n")
        saida = data + ";"+ des +";" + str(temp) + "\n"
        retorno[len(retorno)-1] = saida
        continue
            
    elif tratar[2].replace('"','') == "C" and rende:
        saida += data + ";"+ des +";"
    elif tratar[2].replace('"','') == "C":
        saida += data + ";;"
    else:
        saida += data + ";;;;;" 
        
    saida += tratar[1].replace('"','') + "\n"
    saida = saida.replace('"','')
    retorno.append(saida)
output = ""
for x in retorno:
    x = x.replace('.',',')
    output += x
print(output)
f = open("resultado.txt", "w")
f.write(output)
f.close()