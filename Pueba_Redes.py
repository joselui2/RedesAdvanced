import os
import getpass
usuarios = {
    'admin': 'cisco123'
}
def login():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso!")
        return True    
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return False
while not login():
    pass
def menuPrincipal():
    continuar = True
    while (continuar):
       opcionCorrecta = False
       while(not opcionCorrecta):
         print("=========== DOCUMENTACION DE RED ==========")
         print("1- Nombres de los Dispositivos ")
         print("2- Vlans configuradas ")
         print("3- Servicios de red comprometidos y Modelo Jerárquico")
         print("4- Campus ")
         print("5- Salir")
         print("========")
         opcion = int(input("Seleccione una Opcion Correcta: "))
         if opcion < 1 or opcion > 5:
             print("Opcion incorrecta, ingrese nuevamente...")
             os.system('clear')
         elif opcion == 5:
             continuar = False
             print("Fin de la documentacion")
             break
             os.system('clear')
         else:
             opcionCorrecta = True
             ejecutarOpcion(opcion)           
def ejecutarOpcion(opcion): 
    if opcion == 1:
        dispositivos=[]
        file=open ("dispositivos.txt", "r")
        for item in file:
            item=item.strip ()
            print(item)
        file.close()
        print("\n")
        opc = input("¿Quiere agregar un nuevo dispositivo Si = 1 o No = 2 ""\n")
        if opc == "1":
         file = open ("dispositivos.txt", "a")
         while True:
                print("Para Salir Escribir exit")
                newItem = input("\n" + "Ingrese el Nombre del nuevo dispositivo: ")
                if newItem == "exit":
                 print("Se Guardo Correctamente!")
                 break
                 os.system('clear')
                file.write("NOMBRE DEL DISPOSITIVO: " + newItem + "\t" + "\t" )
                newItem = input("Campus al que pertenese: ")
                file.write("CAMPUS: " + newItem + "\t" + "\t")
                newItem = input("Direcciones IPv4: ")
                file.write("Direcciones IPv4: " + newItem + "\t")
                newItem = input("Direcciones IPv6: ")
                file.write("Direcciones IPv6: " + newItem + "\n")
         file.close()
         os.system('clear')
        elif opc == "2":
         os.system('clear')
    elif opcion == 2:
        Vlans=[]
        file=open ("Vlans.txt", "r")
        for item in file:
            item=item.strip ()
            print(item)
        file.close()
        print("\n")
        opc = input("¿Quiere agregar un nuevo dispositivo Si = 1 o No = 2 ""\n")
        if opc == "1":
         file = open ("Vlans.txt", "a")
         while True:
                print("Para Salir Escribir exit")
                newItem = input("\n" + "NOMBRE DEL DISPOSITIVO Y CAMPUS: ")
                if newItem == "exit":
                 print("Se Guardo Correctamente!")
                 break
                 os.system('clear')
                file.write("NOMBRE DEL DISPOSITIVO / CAMPUS: " + newItem + "\t" + "\t" )
                newItem = input("INGRESA EL NUMERO DE VLANS: ")
                file.write("VLANS: " + newItem + "\t" + "\t")
                newItem = input("Direcciones IPv4: ")
                file.write("Direcciones IPv4: " + newItem + "\n")
         file.close() 
         os.system('clear')
        elif opc == "2":
            os.system('clear')
    elif opcion == 3:
        jerarquia=[]
        file=open ("jerarquia.txt", "r")
        for item in file:
            item=item.strip ()
            print(item)
        file.close()
        opc = input("¿Quiere agregar un nuevo dispositivo Si = 1 o No = 2 ""\n")
        if opc == "1":
         file = open ("jerarquia.txt", "a")
         while True:
                print("Para Salir Escribir exit")
                newItem = input("\n" + "INGRESE EL NOMBRE DEL DISPOSITIVO Y CAMPUS: ")
                if newItem == "exit":
                 print("Se Guardo Correctamente!")
                 break
                 os.system('clear')
                file.write("NOMBRE DEL DISPOSITIVO Y CAMPUS: " + newItem + "\t" + "\t" )
                newItem = input("INGRESE LA CAPA Y LA DISTRIBUCION JERARQUICA: ")
                file.write("CAPA Y JERARQUIA: " + newItem + "\t")
                newItem = input("INGRESE SERVICIOS COMPROMETIDOS: ")
                file.write("SERVICIO COMPROMETIDOS: " + newItem + "\n")
         file.close()    
         os.system('clear')
        elif opc == "2":
         os.system('clear')
    elif opcion == 4:
        campues=[]
        file=open ("campus.txt", "r")
        for item in file:
            item=item.strip ()
            print(item)
        file.close()
        opc = input("¿Quiere agregar un nuevo campus Si = 1 o No = 2 ""\n")
        if opc == "1":
         file = open ("campus.txt", "a")
         while True:
                print("Para Salir Escribir exit")
                newItem = input( "Inrese el nombre del nuevo campus: ")
                if newItem == "exit":
                 print("Se Guardo Correctamente!")
                 break
                 os.system('clear')
                file.write("Campus: " + newItem +  "\n")
         file.close()    
         os.system('clear')
        elif opc == "2":
            os.system('clear')
menuPrincipal()   
