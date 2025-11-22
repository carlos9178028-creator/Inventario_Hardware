HArdware_lista={}
def menu():
    print("Menú")
    print("-------------")
    print("1. Ingresar hardware")
    print("2. Mostrar inventario")
    print("3.Eliminar hardware existente")
    print("4. Agregar cantidad nueva a hardware existente ")
    print("5. Salir")
    try: 
         op=int(input("Elige una opcion:"))
    except ValueError:
         print("Vuelve a elegir una opción válida")
    else:
         if op<1 or op>5:
              print("La opcion no existe")
              return menu()
         return op 
def ingresar_hardware(hardware):
     if hardware in HArdware_lista:
          print(f"{HArdware_lista[hardware]} ya existe")
     else:
          cantidad=int(input("Ingresa la cantidad que hay del hardware:"))
          HArdware_lista[hardware]=cantidad
def mostrar():
     x=0
     for clave, valor in HArdware_lista.items():
          print(f"{x+1}.-{clave}:{valor}")
def eliminar(hardware):
    if hardware in HArdware_lista:
            del HArdware_lista[hardware]
     
while True:
    cap=menu()
    if cap==1:
          hardware=input("Ingresa el hardware:")
          h=ingresar_hardware(hardware)
    elif cap==2:
         mostrar()
    elif cap==3:
        if not HArdware_lista:
              print("Está vació el inventario")
        else:
         hardware_del=input("Escribe el hardware que desea eliminar:")
         elim=eliminar(hardware_del)

         
         