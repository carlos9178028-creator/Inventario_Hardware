import pathlib
hardware_diccionario={}
def menu():
    print("---------")
    print("Menú")
    print("----------")
    print("1. Agregar hardware")
    print("2. Mostrar inventario")
    print("3.Eliminar Hardware")
    print("4. Salir")
hardware=input("Ingresa el hardware que deseas agregar:")
cantidad=int(input("Ingresa la cantidad del hardware:"))
hardware_diccionario[hardware]=cantidad
print(hardware_diccionario)
inventario=pathlib.Path("prueba.txt")
if inventario.exists():
    print("Existe")
    with open(inventario,"w",encoding="utf-8") as f :
        f.write(f"{hardware_diccionario}")
else:
    print("No existe")
         
         