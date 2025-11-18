hardware_diccionario={}
while True :
    print("\nMenú de Inventario de Hardware")
    print("1. Agregar hardware")
    print("2. Mostrar inventario")
    print("3. Agregar cantidad a hardware existente")
    print("4. Eliminar hardware")
    print("5. Salir")
    try :
        opcion=int(input("Elige una opcion del menú:"))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    else:
        if opcion>=1 and opcion<=3:
            if opcion==1:
                hardware=input("Ingresa el nombre del hardware:").upper()
                cantidad=input("Ingresa la cantidad de hardware:")
                if hardware in hardware_diccionario:
                    print(f"El hardware {hardware} ya existe en el inventario con cantidad {hardware_diccionario[hardware]}.")       
                else:
                  hardware_diccionario[hardware]=cantidad     
                  print(f"Se ha agregado {hardware} con cantidad {cantidad} al inventario.")
            elif opcion==2:
                if hardware_diccionario=={}:
                    print("El inventario está vacío.")
                else:
                    print("Inventario de Hardware:")
                    print("---------------------------")
                    for hardware, cantidad in hardware_diccionario.items():
                        print(f"{hardware}: {cantidad}")
                    print("---------------------------")
            elif opcion==3:
                hardware=input("Ingresa el nombre del hardware al que deseas agregar cantidad:").upper()
                if hardware in hardware_diccionario:
                    try:
                        cantidad_adicional=int(input("Ingresa la cantidad adicional a agregar:"))
                        cantidad_actual=int(hardware_diccionario[hardware])
                        nueva_cantidad=cantidad_actual+cantidad_adicional
                        hardware_diccionario[hardware]=str(nueva_cantidad)
                        print(f"La nueva cantidad de {hardware} es {nueva_cantidad}.")
                    except ValueError:
                        print("Por favor, ingresa un número válido para la cantidad.")
                else:
                    print(f"El hardware {hardware} no existe en el inventario.")
            elif opcion==4:
                hardware=input("Ingresa el nombre del hardware que desea eliminar:").upper()
                if hardware in hardware_diccionario:
                    del hardware_diccionario[hardware]
                    print(f"El hardware {hardware} ha sido eliminado del inventario.")
                else:
                    print(f"El hardware {hardware} no existe en el inventario.")
            elif opcion==5:
                print("Saliendo del programa...")
                break