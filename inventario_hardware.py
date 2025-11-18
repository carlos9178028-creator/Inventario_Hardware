hardware_diccionario={}
while True :
    print("\nMenú de Inventario de Hardware")
    print("1. Agregar hardware")
    print("2. Mostrar inventario")
    print("3. Salir")
    try :
        opcion=int("Elige una opcion del menú:")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    else:
        if opcion>=1 or opcion<=3:
            if opcion==1:
                for valor, clave in hardware_diccionario.items():
                    
                hardware=input("EScribe el componente del hardware que deseas agregar:")
                
