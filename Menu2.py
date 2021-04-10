import os

def Menu():
    
    os.system("clear")
    
    print("******selecciones una opcion del menu******")
    print("1   --------------Registrar Alumno")
    print("2   -------- Solicitud de Uniforme")
    print("9   --------------Salir")
    
while True:
    Menu()
    
    opcion= input("Elije la opcion del  Menu......")
    
    if opcion=="1":
        nombre=str()
        apellido=str()
        direccion=str()
        nota1=float()
        nota2=float()
        totalnota=float()
        print("nombre del Alumno:")
        nombre=input()
        print("Apellido del Alumno:")
        apellido=input()
        print("cual es su direccion:")
        direccion=input()
        print("digite su primera nota:")
        nota1=float(input())
        print("digite su segunda nota:")
        nota2=float(input())
        totalnota=nota1+nota2
        print("nombre del Alumno",nombre,"\nApellido",apellido,"\nDireccion",direccion,"\nNota Total...",totalnota)
        print("pulsa una Tecla para Volver al Menu....")
    elif opcion=="2":
        camisa=str()
        pantalon=str()
        medias=str()
        camiseta=str()
        sudadera=str()
        buso=str()
        cantidad1=float()
        cantidad2=float()
        cantidad3=float()
        cantidad4=float()
        cantidad5=float()
        cantidad6=float()
        totalvalor=float()
        print("color de la camisa?..")
        camisa=input()
        print("cantidad:")
        cantidad1=float(input())
        print("color del pantalon?..")
        pantalon= input()
        print("cantidad:")
        cantidad2=float(input())
        print("color de las medias")
        medias=input()
        print("cantidad")
        cantidad3= float(input())
        print("color de la camiseta?..")
        camiseta=input()
        print("cantidad")
        cantidad4=float(input())
        print("color de la sudadera?..")
        sudadera=input()
        print("cantidad")
        cantidad5=float(input())
        print("color del buso?..")
        buso=input()
        print("cantidad")
        cantidad6=float(input())
        totalvalor=cantidad1+cantidad2+cantidad3+cantidad4+cantidad5+cantidad6
        print("\ncamisa:",camisa,"\npantalon:",pantalon,"\nmedias:",medias,"\ncamiseta:",camiseta,"\nsudadera:",sudadera,"\nbuso:",buso,"\ntota de los articulos...",totalvalor)
        print("pulsa una Tecla para Volver al Menu....") 
    elif opcion=="3":
        zapatos=str() 
    elif opcion=="9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
         
        