'''
Cree un menu para una empresa que permita guardar autos
un auto tiene una patente, un modelo y una marca
El menu debe tener las siguientes opciones :
1.- agregar auto
2.- imprimir todos los autos
3.- buscar auto por patente
4.- eliminar auto
5.- Modificar modelo por patente
0.- salir
se espera crear una lista con diccionarios de autos.'''

lista=[]
while(True):
    print("\n"*3)
    print(".-"*25)
    print(".-.- M E N U   P R I N C I P A L .-.-")
    print("")
    print("1.- Agregar auto")
    print("2.- Imprimir todos los autos")
    print("3.- buscar auto(por patente)")
    print("4.- Eliminar auto")
    print("5.- modificar modelo por patente")
    print("6.-Crear archivo csv")
    print("7.-Cargar archivo csv")
    print("0.- Salir")
    print("")
    op=int(input("Ingrese una opción : \n"))
    if op==1:
        lista_chica=[]
        print("-.-.-AGREGAR AUTO-.-.-")
        patente=input("Ingrese la patente: \n")
        modelo=input("Ingrese el modelo \n")
        marca=input("Ingrese la marca\n")
        lista_chica=[patente, modelo,marca]
        lista.append(lista_chica)
    elif op==2:
        print("-.-.-AUTOS AGREGADOS-.-.-")
        for x in lista:
            print(x)
    elif op==3:
        print("-.-.-BUSCAR AUTO-.-.-")
        auto=input("ingrese la patente del auto que desea buscar\n")
        for x in lista:
            if x[0]==auto:
                print ("Patente encontrada")
                print (f"Patente: {x[0]}  Modelo: {x[1]} Marca: {x[2]}")
    elif op==4:
        encontrado=False
        print("-.-.-ELIMINAR AUTO-.-.-")
        auto=input("ingrese la patente del auto que desea eliminar\n")
        for x in lista:
            if x[0]==auto:
                encontrado=True
                lista.remove(x)
                print ("Patente eliminada correctamente")
                break
        if encontrado==False:
            print("auto no encontrado")
    elif op==5:
        encontrado=False
        print("-.-.-MODIFICAR MODELO-.-.-")
        auto=input("ingrese la patente del auto que desea modificar\n")
        for x in lista:
            if x[0]==auto:
                print ("Patente encontrada")
                modelo_nuevo=input("Ingrese el nuevo modelo")
                x[1]=modelo_nuevo
                print("modelo modificado")
                encontrado=True
                break
        if encontrado==False:
            print("auto no encontrado")
    elif op==6:
        print("")
        print("GENERANDO ARCHIVO DE DATOS")
        print("")
        import csv
        with open('archivo_csv.csv','w',newline='') as archivo_csv:
            escribir_csv=csv.writer(archivo_csv)
            escribir_csv.writerow(['patente','modelo','marca'])
            escribir_csv.writerows(lista)
        print("")
        print("Archivo creado correctamente")
        print("")
    elif op==7:
        print("")
        print("CARGAR ARCHIVO DE DATOS")
        print("")
        import csv
        lista.clear()
        with open ('archivo_csv.csv','r',newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila)
                lista.append(fila)
        lista.pop(0)
    elif op==0:
        print("Adios...")
        break
    else:
        print("opcion invalida, ingrese una opcion valida")
        
        
