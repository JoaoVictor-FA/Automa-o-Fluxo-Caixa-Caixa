with open("./extrato.txt", "r") as fileObj:
    x = fileObj.read().splitlines()
x = map(lambda s: s.replace('"',''), x)
retorno = []
for i in x:
    tratar = i.split(";")
    if tratar[1] == 'Data_Mov':
        continue
    data = tratar[1]
    des = tratar[3]
    valor = tratar[4]
    sentido = tratar[5]
    if des == 'REM BASICA' or des == 'CRED JUROS':
        des = "Rendimentos"
    elif des == 'CAD AGUA':
        des = "Agua"
    elif des == 'PG LUZ/GAS':
        des = "Energia"
    else:
        des = ""
    # dia = data[6:8]
    # mes = data[4:6]
    # ano = data[0:4]
    data = data[6:8] + "/" + data[4:6] + "/" + data[0:4]
    # Rendimentos no mesmo dia
    if des == "Rendimentos"and retorno != [] and retorno[-1].split(";")[1] == "Rendimentos" and retorno[-1].split(";")[0] == data:
            temp = float(retorno[-1].split(";")[2])
            temp += float(valor + "\n")
            saida = data + ";"+ des +";" + ('%.2f'%temp) + "\n"
            retorno[-1] = saida
            continue
    # Posicionando na tabela
    if sentido == 'C' and des != "":
        saida = data + ";"+ des +";"
    elif sentido == 'C':
        saida = data + ";;"
    elif sentido == 'D' and des != "":
        saida = data + ";;;;" + des +";"
    else:
        saida = data + ";;;;;" 
        
    saida += valor + "\n"
    retorno.append(saida)

with open("resultado.txt", "w") as fileObj:
    for x in retorno:
        output = x.replace('.',',')
        fileObj.write(output)
        print(x[:-1])
