HArdware_lista={}
def menu():
    print("Menú")
    print("-------------")
    print("1. Ingresar hardware")
    print("2.Eliminar hardware de la lista")
    print("3.Mostrar inventario")
    print("4. Agregar cantidad nueva a hardware existente ")
    print("5. Salir")
    try: 
         op=int(input("Elige una opcion:"))
    except ValueError:
         print("Vuelve a elegir una opción válida")
    else:
         if op<1 or op>5:
              print("La opcion no existe")
         else :  
             return op
def ingresar_hardware(hardware):
     if hardware in HArdware_lista:
          print(f"{HArdware_lista[hardware]} ya existe")
     else:
          hardware=input("Escribe el hardware que quieres ingresar:")
          cantidad=int(input("Ingresa la cantidad que hay del hardware:"))
          HArdware_lista[hardware]=cantidad
cap=menu()
while True:
     cap
     if cap==1:
          h=ingresar_hardware