import os

def Menu():

    os.system("clear")

    print("********MENU PRINCIPAL*******")
    print("1.----------Registrar Cliente")
    print("2.----------Ventas")
    print("3.----------Inventarios")
    print("4.----------Entregas")
    print("5.----------Facturacion")
    print("9.----------Salir")
    print("*****************************")

while True:
    
    Menu()
    
    opci=input("Elije una Opcion del Menu....")
    print("********************************")
    
    if opci=="1":
        nombre=str()
        nit=float()
        telefono=float()
        direccion=str()
        ciudad=str()
        guardar=str()
        print("Cual es el nombre del Cliente:")
        nombre=input()
        print("Nit de la Empresa:")
        nit=float(input())
        print("Telefono de la Empresa:")
        telefono=float(input())
        print("Direccion de la Empresa:")
        direccion=input()
        print("Ciudad:")
        ciudad=input()
        print("Desea Guardar los Datos?(si)(no)")
        guardar=input()
        print("**************************************")
        print("Los Datos de Guardaron Correctamente")
        print("\nNombre:",nombre,"\nNit:",nit,"\nTelefono:",telefono,"\nDireccion:",direccion,"\nCiudad:",ciudad)
        print("***************************************")
        print("pulsa una Tecla para Volver al Menu....")
    elif opci=="2":
        factura=int()
        nombre=str()
        nit=int()
        telefono= int()
        direccion=str()
        ciudad=str()
        codigo= int()
        descripcion=str()
        cantidad= int()
        valor= int()
        total= int()
        print("Factura Electronica de Venta N°")
        factura= int(input())
        print("Nombre:")
        nombre=input()
        print("Nit:")
        nit=int(input())
        print("Telefono:")
        telefono= int(input())
        print("Direccion:")
        direccion=input()
        print("Ciudad:")
        ciudad=input()
        print("Codigo")
        codigo= int(input())
        print("Descripcion")
        descripcion=input()
        print("Cantidad")
        cantidad= int(input())
        print("Valor")
        valor= int(input())
        total=cantidad*valor
        print("**********************************")
        print("\nFERRETERIA LA 65","\nDireccion: Calle 23 # 33a -54","\nTelefono: 3146358194","\nCiudad: Medellin","\nNit: 71217546","\nResponsable de IVA","\n**************************"
        ,"\nFactura:",factura,"\nNombre:",nombre,"\nNit:",nit,"\nTelefono:",telefono,"\nDireccion:",direccion,"\nCiudad:"
        ,ciudad,"\nCodigo",codigo,"\tDescripcion",descripcion,"\tCantidad",cantidad,"\tValor",valor,"\tTotal",total)
        print("***************************************************************************************************")
        print("pulsa una Tecla para Volver al Menu....")
    elif opci=="3":
        nombre_producto=str()
        refrerencia=str()
        cantidad= int()
        codigo=float()
        print("Digite el nombre del producto")
        nombre_producto=input()
        print("Refrerencia Asignarle al producto")
        refrerencia=input()
        print("digite la cantidad")
        cantidad=int(input())
        print("digite un codigo!")
        codigo=int(input())  
        print("*******************************************")
        print("\nProducto",nombre_producto,"\nRefrerencia:",refrerencia,"\nCantidad:",cantidad,"\nCodigo Asignado:",codigo,)  
        print("****************************************") 
        print("pulsa una tecla para Volver al Menu...") 
    elif opci=="4":
        numero_entrega=int()
        nombre_del_cliente=str()
        direccion_de_entrega=str()
        telefono=int()
        celular= int()
        nit= int()
        cantidad= int()
        descripcion=str()
        print("Numero de OT #:")
        numero_entrega=int(input())
        print("Nombre del Cliente:")
        nombre_del_cliente=input()
        print("Direccion de la Entrega:")
        direccion_de_entrega=input()
        print("Telefono:")
        telefono=int(input())
        print("Celular:")
        celular=int(input())
        print("Nit o Celular:")
        nit=int(input())
        print("cantidad:")
        cantidad=int(input())
        print("Descripcion del Producto:")
        descripcion=input()
        print("************************************************")
        print("Numero de OT:",numero_entrega,"\nNombre del Cliente:",nombre_del_cliente,"\nDireccion de la Entrega:",direccion_de_entrega,
        "\nTelefono:",telefono,"\nCelular:",celular,"\nNit:",nit,"\nCantidad:",cantidad,"\nDescripcion del Producto:",descripcion,)
        print("*************************************************")
        print("pulsa una tecla para Volver al Menu...") 
    elif opci=="9":
        break
    else:
        print("")
        input("No has pulsado una Opcion del MENU.....\nPulsa una Tecla para CONTINUAR..")
        
