
import os 

def Menu():
    
    os.system("clear")
    
    print("******selecciones una opcion del menu******")
    print("\t1   -------------- tipico")
    print("\t2   --------------japones")
    print("\t3   ----------------chino")
    print("\t4   ----------------arabe")
    print("\t5   ----------------turca")
    print("\t6   ----------------salir")
    
while True:
    
    Menu()
    
    opcionMenu= input("Elije la opcion del  Menu......")
    
    if opcionMenu=="1":
        num1=float()
        num2=float()
        cantidad=float()
        print("Bandeja Paisa completa \nCual es valor:")
        num1=float(input())
        print("Bebidad \nCual su Valor:")
        num2=float(input())
        cantidad=num1+num2
        print("Total a pagar:",cantidad)
        input("pulsa una Tecla para Volver al Menu....")
    elif opcionMenu=="2":
        num3=float()
        num4=float()
        cantidad1=float()
        print("Arroz Japones con pollo teriyaki \nCuan es su valos")
        num3=float(input())
        print("Bebida \nCual es su valor")
        num4=float(input())
        cantidad1=num3+num4
        print("Total a Pagar:",cantidad1)
        input("pulsa una Tecla para Volver al Menu....")
    elif opcionMenu=="3":
        num5=float()
        num6=float()
        cantidad2=float()
        print("Arroz chino con vegetales\nCual es su valor?")
        num5=float(input())
        print("Bebida\nCual es su valor?..")
        num6=float(input())
        cantidad2=num5+num6
        print("Total a pagar:",cantidad2)
        input("pulsa una Tecla para Volver al Menu....")
    elif opcionMenu=="4":
        num7=float()
        num8=float()
        cantidad3=float()
        print("chaguarma con quibe\nCual es su valor?")
        num7=float(input())
        print("Bebida \nCual es su valor?")
        num8=float(input())
        cantidad3=num7+num8
        print("Total a pagar:",cantidad3)
        input("pulsa una Tecla para Volver al Menu....")
    elif opcionMenu=="6":
	    break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
         