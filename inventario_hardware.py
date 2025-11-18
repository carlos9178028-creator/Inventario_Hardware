hardware_diccionario={}
while True :
    print("\nMenú de Inventario de Hardware")
    print("1. Agregar hardware")
    print("2. Mostrar inventario")
    print("3. Salir")
    try :
        opcion=int(input("Elige una opcion del menú:"))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    else:
        if opcion>=1 and opcion<=3:
            if opcion==1:
                i=-1
                for clave,valor in hardware_diccionario.items():
                    while hardware==clave:
                        print("El hardware ya existe en el inventario.")
                        hardware=input("Ingresa el nombre del hardware:")
                hardware=input("Ingresa el nombre del hardware:")
            cantidad=input("Ingresa la cantidad de hardware:")
            hardware_diccionario[hardware]=cantidad
            print(f"Se ha agregado {hardware} con cantidad {cantidad} al inventario.")
            print(hardware_diccionario)
                
