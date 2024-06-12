import csv
lista[]
def sep():
    print("")
    print("-.-.-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("")
def menu():
    sep()
    print("-.-.-.-.-M E N Ú-.-.-.-.-")
    print("")
    print("1.-Agregar producto")
    print("2.-Listar todos los productos")
    print("3.-Eliminar producto por id")
    print("4.-Generar archivo csv")
    print("5.-Cargar datos csv")
    print("6.-Estadisticas")
    print("0.-Salir")
    print("")
    sep()
while (True):
    menu()
    op=int(input("Ingrese una opción"))
    if op==1:
        sep()
        lista_chica=[]
        print("-.-.-.-.-AGREGAR PRODUCTO-.-.-.-.-")
        print("")
        id=int(input("Ingrese el id del producto : \n"))
        nombre=int(input("Ingrese el nombre del producto : \n"))
        precio=int(input("Ingrese el precio del producto : \n"))
        lista_chica=[id,nombre,precio]
        lista.append(lista_chica)
    elif op==2:
        sep()
        print("-.-.-.-.-LISTA PRODUCTOS-.-.-.-.-")
        print("")
        for x in lista:
            print(x)
    elif op==3:
        sep()
        encontrado=False
        print("-.-.-.-.-ELIMINAR PRODUCTO-.-.-.-.-")
        print("")
        producto=int(input("Ingrese el id del producto que desea eliminar: \n"))
        for x in lista:
            if x[0]==producto:
                encontrado=True
                lista.remove(x)
                print("Producto eliminado correctamente :)") 
                break
        if encontrado==False:
            print("id no encontrado")               
    elif op==4:
        sep()
        print("-.-.-.-.-GENERAR ARCHIVO CSV-.-.-.-.-")
        print("")
        with open ('productos_csv.csv','w',newline='') in producto_csv:
            escribir_csv=csv.writer(producto_csv)
    elif op==5:
        sep()
        print("")
    elif op==6:
        sep()
        print("")
    elif op==0:
        sep()
        print("Adios......")
        sep()
        break
    else:
        sep()
        print("Opción invalida, porfavor ingrese una de las opciones del menú")