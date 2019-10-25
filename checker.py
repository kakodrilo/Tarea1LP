import re

##Definición de Expresiones regulares:
#ER de estructura básica:
exHAI=re.compile("\s*HAI\s*")
exKTHXBYE= re.compile("\s*KTHXBYE\s*")
#ER de declaración e Inicialización de variables:
exDecl=re.compile("(\s*I\s+HAS\s+A\s+)([a-zA-Z]\w*)((\s+ITZ\s+)(([0-9]+(\.[0-9]+)?)|(\".*\")|(.+))\s*)?\s*")
exAsg=re.compile("(\s*[a-zA-Z]\w*)(\s+R\s+)(([a-zA-Z]\w*\s*)|([0-9]+(\.[0-9]+)?\s*)|(\".+\"\s*)|(.+\s*))")
#ER de Operadores:
opMat="(SUM\s+OF|DIFF\s+OF|PRODUKT\s+OF|QUOSHUNT\s+OF|MOD\s+OF|BIGGR\s+OF|SMALLR\s+OF|BOTH\s+OF|EITHER\s+|BOTH\s+SAEM|DIFFRINT)"
exMatBi=re.compile("(\s*"+opMat+"\s+)(([a-zA-Z]\w*)|([0-9]+(\.[0-9]+)?)|(\".+\")|(.+))(\s+AN\s+)(([a-zA-Z]\w*\s*)|([0-9]+(\.[0-9]+)?\s*)|(\".+\"\s*)|(.+\s*))")
exOpUn=re.compile("(\s*NOT\s+)(([a-zA-Z]\w*\s*)|([0-9]+(\.[0-9]+)?\s*)|(\".+\"\s*)|(.+\s*))")
#ER de Entrada y Salida:
exEn=re.compile("(\s*GIMMEH\s+)([a-zA-Z]\w*)")
exSld=re.compile("(\s*VISIBLE\s+)(([a-zA-Z]\w*\s*)|([0-9]+(\.[0-9]+)?\s*)|(\".+\"\s*)|(.+\s*))")
#ER de Loops:
exApCic=re.compile("(\s*IM\s+IN\s+YR\s+)([a-zA-Z]\w*)(\s+(NERFIN|UPPIN))((\s+YR\s+)([a-zA-Z]\w*\s*))(((\s*TIL\s*)|(\s*WILE\s+))(.+))?")
exCrcic=re.compile("(\s*IM\s+OUTTA\s+YR\s+)(([a-zA-Z]\w*)\s*)")
#ER de Condicionales:
exORLY=re.compile("\s*O\s+RLY\?\s*")
exYARLY=re.compile("\s*YA\s+RLY\s*")
exNOWAI=re.compile("\s*NO\s+WAI\s*")
exOIC=re.compile("\s*OIC\s*")

'''
*
Función declaracion:
******
* La función analiza si un string que cumple con la ER de declaración de una variable (exDecl) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def declaracion(linea):
    expresion = linea
    salida=""
    if exDecl.fullmatch(linea).group(9) == None:
        salida+= "\033[33m"+exDecl.fullmatch(linea).group(1)+"\033[00m"
        salida+= exDecl.fullmatch(linea).group(2)
        if exDecl.fullmatch(linea).group(4) != None:
            salida+= "\033[33m"+exDecl.fullmatch(linea).group(4)+"\033[00m"
            if exDecl.fullmatch(linea).group(6)!= None:
                salida+= exDecl.fullmatch(linea).group(6)
            else:
                salida+= exDecl.fullmatch(linea).group(8)
    else:
        ex=identificador_expresion(exDecl.fullmatch(linea).group(9))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[33m"+exDecl.fullmatch(linea).group(1)+"\033[00m"
            salida+= exDecl.fullmatch(linea).group(2)
            salida+= "\033[33m"+exDecl.fullmatch(linea).group(4)+"\033[00m"
            salida+= ejecutar(ex,exDecl.fullmatch(linea).group(9))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función asignacion:
******
* La función analiza si un string que cumple con la ER de asignación de una variable (exAsg) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def asignacion(linea):
    salida=""
    if exAsg.fullmatch(linea).group(8) == None :
        salida+=exAsg.fullmatch(linea).group(1)+"\033[31m"+exAsg.fullmatch(linea).group(2)+"\033[00m"+exAsg.fullmatch(linea).group(3)
    else:
        ex=identificador_expresion(exAsg.fullmatch(linea).group(8))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+=exAsg.fullmatch(linea).group(1)
            salida+="\033[31m"+exAsg.fullmatch(linea).group(2)+"\033[00m"
            salida+=ejecutar(ex,exAsg.fullmatch(linea).group(8))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función operacionBinaria:
******
* La función analiza si un string que cumple con la ER de operación binaria (exMatBi) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def operacionBinaria(linea):
    salida=""
    if (exMatBi.fullmatch(linea).group(8) == None) and (exMatBi.fullmatch(linea).group(15) == None):
        salida+="\033[34m"+exMatBi.fullmatch(linea).group(1)+"\033[00m"
        salida+=exMatBi.fullmatch(linea).group(3)
        salida+="\033[34m"+exMatBi.fullmatch(linea).group(9)+"\033[00m"
        salida+=exMatBi.fullmatch(linea).group(10)
    elif(exMatBi.fullmatch(linea).group(8) != None) and (exMatBi.fullmatch(linea).group(15) == None):
        ex=identificador_expresion(exMatBi.fullmatch(linea).group(8))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(1)+"\033[00m"
            salida+=ejecutar(ex,exMatBi.fullmatch(linea).group(8))
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(9)+"\033[00m"
            salida+=exMatBi.fullmatch(linea).group(10)
    elif(exMatBi.fullmatch(linea).group(8) == None) and (exMatBi.fullmatch(linea).group(15) != None):
        ex=identificador_expresion(exMatBi.fullmatch(linea).group(15))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(1)+"\033[00m"
            salida+=exMatBi.fullmatch(linea).group(3)
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(9)+"\033[00m"
            salida+=ejecutar(ex,exMatBi.fullmatch(linea).group(15))
    else:
        ex1=identificador_expresion(exMatBi.fullmatch(linea).group(8))
        ex2=identificador_expresion(exMatBi.fullmatch(linea).group(15))
        if (ex1 == -1) or (ex2 == -1):
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(1)+"\033[00m"
            salida+=ejecutar(ex1,exMatBi.fullmatch(linea).group(8))
            salida+="\033[34m"+exMatBi.fullmatch(linea).group(9)+"\033[00m"
            salida+=ejecutar(ex,exMatBi.fullmatch(linea).group(15))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función operacionUnitaria:
******
* La función analiza si un string que cumple con la ER de operación unitaria (exOpUn) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def operacionUnitaria(linea):
    salida=""
    if exOpUn.fullmatch(linea).group(7) == None:
        salida+="\033[34m"+exOpUn.fullmatch(linea).group(1)+"\033[00m"
        salida+=exOpUn.fullmatch(linea).group(2)
    else:
        ex = identificador_expresion(exOpUn.fullmatch(linea).group(7))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[34m"+exOpUn.fullmatch(linea).group(1)+"\033[00m"
            salida+=ejecutar(ex,exOpUn.fullmatch(linea).group(7))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función entrada:
******
* La función analiza si un string que cumple con la ER de entrada de una variable (exEn) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def entrada(linea):
    return "\033[31m"+exEn.fullmatch(linea).group(1)+"\033[00m"+exEn.fullmatch(linea).group(2)

'''
*
Función salida:
******
* La función analiza si un string que cumple con la ER de salida de una expresión (exSld) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def salida(linea):
    salida=""
    if exSld.fullmatch(linea).group(7) == None:
        return "\033[31m"+exSld.fullmatch(linea).group(1)+"\033[00m"+exSld.fullmatch(linea).group(2)
    else:
        ex=identificador_expresion(exSld.fullmatch(linea).group(7))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            salida+="\033[31m"+exSld.fullmatch(linea).group(1)+"\033[00m"
            salida+=ejecutar(ex,exSld.fullmatch(linea).group(7))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función aperturaCiclos:
******
* La función analiza si un string que cumple con la ER de apertura de un ciclo (exApCic) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
lista_ciclos=[]
def aperturaCiclos(linea):
    salida=""
    if exApCic.fullmatch(linea).group(8)==None:
        lista_ciclos.append((exApCic.fullmatch(linea).group(2),len(lista_salida),linea))
        salida+="\033[35m"+exApCic.fullmatch(linea).group(1)+"\033[00m"
        salida+=exApCic.fullmatch(linea).group(2)
        salida+="\033[35m"+exApCic.fullmatch(linea).group(3)+exApCic.fullmatch(linea).group(6)+"\033[00m"
        salida+=exApCic.fullmatch(linea).group(7)
    else:
        ex=identificador_expresion(exApCic.fullmatch(linea).group(12))
        if ex == -1:
            return "\033[41m"+linea+"\033[00m"
        else:
            lista_ciclos.append((exApCic.fullmatch(linea).group(2),len(lista_salida),"\033[41m"+linea+"\033[00m"))
            salida+="\033[35m"+exApCic.fullmatch(linea).group(1)+"\033[00m"
            salida+=exApCic.fullmatch(linea).group(2)
            salida+="\033[35m"+exApCic.fullmatch(linea).group(3)+exApCic.fullmatch(linea).group(6)+"\033[00m"
            salida+=exApCic.fullmatch(linea).group(7)
            salida+="\033[35m"+exApCic.fullmatch(linea).group(9)+"\033[00m"
            salida+=ejecutar(ex,exApCic.fullmatch(linea).group(12))
    if "\033[41m" in salida:
        return "\033[41m"+linea+"\033[00m"
    return salida

'''
*
Función cierreCiclos:
******
* La función analiza si un string que cumple con la ER de cierre de un ciclo (exCrcic) está completamente correcto.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
def cierreCiclos(linea):
    if len(lista_ciclos)!= 0 and (exCrcic.fullmatch(linea).group(3) == lista_ciclos[-1][0]) and not(exApCic.fullmatch(lista_programa[len(lista_salida)-2])):
        del lista_ciclos[-1]
        return "\033[35m"+exCrcic.fullmatch(linea).group(1)+"\033[00m"+exCrcic.fullmatch(linea).group(2)
    else:
        return "\033[41m"+linea+"\033[00m"

'''
*
Función identificador_expresion:
******
* La función devuelve la posición en la lista_expresiones correspondiente a la expresión con la que el string hizo fullmatch, o -1 si no hace fullmatch con ninguna.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna un int.
'''
lista_expresiones=[exDecl,exAsg,exMatBi,exOpUn,exEn,exSld]
def identificador_expresion(linea):
    for expresion in lista_expresiones:
        if expresion.fullmatch(linea):
            return lista_expresiones.index(expresion)
    return -1

'''
*
Función ejecutar:
******
* La función ejecuta, según el int recibido, una función específica que procesa el string linea.
******
Input:
* linea : string a analizar.
* pos: int que indica qué función se debe ejecutar (pos proviene de la función identificador_expresion).
******
Returns:
* Retorna la línea que recibe, luego de aplicarle la función específica.
'''
def ejecutar(pos,linea):
    if pos == 0:
        return declaracion(linea)
    elif pos == 1:
        return asignacion(linea)
    elif pos == 2:
        return operacionBinaria(linea)
    elif pos == 3:
        return operacionUnitaria(linea)
    elif pos == 4:
        return entrada(linea)
    elif pos == 5:
        return salida(linea)

'''
*
Función identificador_ciclos:
******
* La función analiza si un string cumple con la ER de apertura (exApCic) o cierre (exCrcic) de ciclos, y procesa el string según corresponda.
******
Input:
* linea : string a analizar.
******
Returns:
* Retorna la línea analizada con los colores correspondientes, dependiendo si está completamente correcta o no.
'''
lista_cond_loops=[exApCic,exCrcic]
def identificador_ciclos(linea):
    ex=-1
    for expresion in lista_cond_loops:
        if expresion.fullmatch(linea):
            ex= lista_cond_loops.index(expresion)
    if ex == -1:
        return "\033[41m"+linea+"\033[00m"
    if ex == 0:
        return aperturaCiclos(linea)
    if ex == 1:
        return cierreCiclos(linea)

## Comienzo del Programa Principal:

lista_archivo=[]
lista_salida=[]
lista_condicionales=[]
lista_condicionales_completos=[]

posicion_ultimo_HAI=""
posicion_primer_KTHXBYE=""


nombre_archivo=input("ingrese nombre de archivo: ")
archivo = open(nombre_archivo,"r")
# Recorremos el archivo, y guardamos cada una de sus líneas en la lista lista_archivo,
#e identificamos entre qué posiciones se encuentra el programa principal.
for linea in archivo:
    linea=linea.strip()
    if exHAI.fullmatch(linea) and posicion_primer_KTHXBYE=="":
        posicion_ultimo_HAI = len(lista_archivo)
    elif exKTHXBYE.fullmatch(linea) and posicion_primer_KTHXBYE == "" :
        posicion_primer_KTHXBYE=len(lista_archivo)
    lista_archivo.append(linea)

archivo.close()

#Si no hay programa principal, entonces arrojamos todas las líneas a la lista antes_del_HAI, para imprimir todas las líneas como error.
if posicion_ultimo_HAI=="" or posicion_primer_KTHXBYE =="":
    antes_del_HAI=lista_archivo
    despues_del_KTHXBYE=[]
    lista_programa=[]
#Si es que hay programa principal, entonces guardamos las líneas que están antes del
#programa principal en la lista antes_del_HAI y las que están después del programa principal
#en la lista despues_del_KTHXBYE, para imprimirlas como error, y las lineas del programa principal en
#la lista lista_programa, para analizarlas.
elif posicion_ultimo_HAI < posicion_primer_KTHXBYE:
    antes_del_HAI=lista_archivo[0:posicion_ultimo_HAI]
    despues_del_KTHXBYE=lista_archivo[posicion_primer_KTHXBYE+1:]
    lista_programa=lista_archivo[posicion_ultimo_HAI:(posicion_primer_KTHXBYE+1)]
#Si es que el KTHXBYE está antes que el HAI, entonces arrojamos todas las líneas a la lista antes_del_HAI,
#para imprimir todas las líneas como error.
else:
    antes_del_HAI=lista_archivo
    despues_del_KTHXBYE=[]
    lista_programa=[]
#Buscamos todos los O RLY? y OIC dentro del programa que se correspondan, para guardar sus posiciones
#respecto a la lista_programa, en la lista_condicionales_completos.
cont=0
for linea in lista_programa:
    if exORLY.fullmatch(linea):
        lista_condicionales.append((linea,cont))
    if exOIC.fullmatch(linea) and len(lista_condicionales)!=0 :
        lista_condicionales_completos.append((lista_condicionales[-1][1],cont))
        del lista_condicionales[-1]
    cont+=1
#Analizamos línea por línea de la lista_programa, y guardamos las líneas procesadas en la lista_salida.
#Este análicis no incluye los condicionales, por lo que los marca a todos como error, para ser analizados luego.
if len(lista_programa)!=0:
    lista_salida.append("\033[32m"+lista_programa[0])
    del lista_programa[0]
    a="\033[32m"+lista_programa[-1]+"\033[00m"
    del lista_programa[-1]
    for linea in lista_programa:
        ex = identificador_expresion(linea)
        if ex != -1:
            lista_salida.append(ejecutar(ex,linea))
        else:
            lista_salida.append(identificador_ciclos(linea))
    for linea in lista_ciclos:
        lista_salida[linea[1]]=linea[2]
    lista_salida.append(a)
#Analizamos los condicionales. Si es que alguna de las palabras claves de los condicionales resulta correcta,
#la reemplazamos en la lista_salida.
#Analizamos condicional por condicional completo de la lista_condicionales_completos:
for pos1,pos2 in lista_condicionales_completos:
    ciclos_anteriores = []
    for pos11,pos22 in lista_condicionales_completos:
        if pos1<pos11 and pos2>pos22:
            ciclos_anteriores += range(pos11,pos22+1)
    flag=0
    pos_anterior = 0
    lista_reemplazo=[]
    if  not("[41m" in lista_salida[pos1-1] or "[35m" in lista_salida[pos1-1]):
        lista_reemplazo.append(("\033[36m"+lista_salida[pos1][5:-5]+"\033[00m",pos1))
    cont=pos1
    for linea in lista_salida[pos1:pos2+1]:
    #Analizamos línea por línea del condicional completo, vale decir, que tiene O RLY? y OIC,
    #para ver si alguna palabra clave resulta correcta:
        if cont not in ciclos_anteriores:
            if exYARLY.fullmatch(linea[5:-5]):
                if  flag == 0:
                    if cont == pos1+1:
                        lista_reemplazo.append(("\033[36m"+linea[5:-5]+"\033[00m",cont))
                    flag = 1
                    pos_anterior = cont
            if exNOWAI.fullmatch(linea[5:-5]):
                if flag==1:
                    if cont-1 != pos_anterior:
                        lista_reemplazo.append(("\033[36m"+linea[5:-5]+"\033[00m",cont))
                    flag = 2
                    pos_anterior = cont
                elif flag == 0:
                    flag = 5
            if exOIC.fullmatch(linea[5:-5]):
                if flag==2:
                    if cont-1 != pos_anterior:
                        lista_reemplazo.append(("\033[36m"+linea[5:-5]+"\033[00m",cont))
                else:
                    lista_reemplazo = []
        cont+=1
    #Reemplazamos las palabras claves correctas del ciclo analizado en la lista_salida:
    for linea,pos in lista_reemplazo:
        lista_salida[pos] = linea
#Finalmente, imprimimos las líneas del archivo ya analizadas:
for linea in antes_del_HAI:
    print("\033[41m"+linea+"\033[00m")
for linea in lista_salida:
    print(linea)
for linea in despues_del_KTHXBYE:
    print("\033[41m"+linea+"\033[00m")
