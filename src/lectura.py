import pandas as pd
import re
import os

#Listado de archivos
def listadoArchivos():
    return os.listdir('./files')

def formatoArchivos():
    lista = listadoArchivos()
    for i in range(len(lista)):
        print(str(i + 1) + '.- ' + lista[i])

#Seleccionador de archivo
def elegirArchivoXLSX(archivo):
    #print(archivo)
    return pd.read_excel(archivo)

#Convertir descripcion en diccionario
"""Descripcion general de las columnas
Si es de strings, regresa count, unique, top, freq
Si es numero, regresa count, mean, std, min, 25, 50, 75, max
"""
def decripcionDiccionario(campo , df):
    return descripcionColumna(campo, df).to_dict()

#Da una descripción general de la columna
def descripcionColumna(campo, df):
    #print(df[campo].describe())
    return df[campo].describe()

#Devuelve el renglón basado en un patrón, utilicese para palabras nada mas
def busquedaRenglonesPalabrasRegex(palabra, df, campo, listaCamposAmostrar):
    '''
    Busca con expresiones regulares con re.search
    '''
    for i in df.index:
        if re.search(palabra , df[campo][i]):
            aux = ''
            for j in listaCamposAmostrar:
                aux = aux + str(df[j][i]) + '| ' # se deciden campos a imprimir
            print(aux)    
    #aux = df[df['Word'].str.contains('abeja')] #busca la palabra completa en Word

#Devuelve un renglón basado en uan condición de un número, utilicese para números nada más
def busquedaRenglonesNumeros(decision ,df, valor_a_comparar, campo, listaCamposAmostrar):
    for i in df.index:
        if decisionNumeroRenglon(decision, df[campo][i], valor_a_comparar):
            aux = ''
            for j in listaCamposAmostrar:
                aux = aux + str(df[j][i]) + '| ' # se deciden campos a imprimir
            print(aux)

#Diferentes decisione para la busqueda por numero
def decisionNumeroRenglon(decision, renglon, valor_a_comparar):
    if decision == 0: # ==
        if renglon == valor_a_comparar:
            return True
        else:
            return False
    elif decision == 1: # >
        if renglon > valor_a_comparar:
            return True
        else:
            return False
    elif decision == 2: # >=
        if renglon >= valor_a_comparar:
            return True
        else:
            return False
    elif decision == 3: # <
        if renglon < valor_a_comparar:
            return True
        else:
            return False
    elif decision == 4: # <=
        if renglon <= valor_a_comparar:
            return True
        else:
            return False
    else:
        return True

#Seleccionador de archivos csv
def elegirArchivoCSV(archivo):
    #print(archivo)
    return pd.read_csv(archivo)

#Eleccion de archivo
def seleccionArchivoALeer(lista, eleccion):
    aux = os.path.splitext(lista[eleccion-1])
    #print(aux)
    if aux[1] == '.xls' or aux[1] == '.xlsx' or aux[1] == '.xlsm' or aux[1] == '.xlsb' or aux[1] == '.odf' or aux[1] == '.ods' or aux[1] == '.odt':#xls, xlsx, xlsm, xlsb, odf, ods and odt 
        print('./files/' + lista[eleccion - 1])
        return elegirArchivoXLSX('./files/' + lista[eleccion - 1])
    elif aux[1] == '.csv':
        print('./files/' + lista[eleccion - 1])
        return elegirArchivoCSV('./files/' + lista[eleccion - 1])
    else:
        print('Archivo no válido')

formatoArchivos()
input1 = int(input())
df = seleccionArchivoALeer(listadoArchivos(), input1)

print(df)

#df = elegirArchivoXLSX('./files/13428_2013_403_MOESM1_ESM.xlsx')

#df = elegirArchivoCSV('./files/simon-task_109.csv')

#df = elegirArchivo('../files/13428_2015_684_MOESM1_ESM.xlsx')
#busquedaRenglonesNumeros(1, df, 27, 'VAL_N' , ['Word','VAL_M' , 'VAL_SD', 'VAL_N'])
#aux = descripcionColumna('VAL_M', df)
#aux = descripcionColumna('Word', df).to_dict()
#print(aux)




#new_dict = df.to_dict()
#print(df.columns)

#guarda = descripcionColumna('AVA_N')
#aux = df['AVA_N'].tolist()      #Con esto cohnviertes una columna en una lista
#print(aux)
#print(type(guarda))
#print(df['Word'].describe())
#print(df.dtypes)
'''
Los strings los cuenta como  object
enteros son int64
flotantes son float64
'''