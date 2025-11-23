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
    try:
     op=int(input("Elige una de las opciones:"))
    except ValueError:
       print(f"{op} invalido")
    else:
       if op<1 or op>4:
          print("No se encuentra la opcion")
          return menu()
       else:
          return op
while True:
   rpta=menu()
   if rpta==1:    
    hardware=input("Ingresa el hardware que deseas agregar:")
    cantidad=int(input("Ingresa la cantidad del hardware:"))
    hardware_diccionario[hardware]=cantidad
    inventario=pathlib.Path("prueba.txt")
    if inventario.exists():
      with open(inventario,"w",encoding="utf-8") as f :
         f.write(f"{hardware_diccionario}")
   else:
     print("No existe")
         
         