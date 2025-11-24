import pathlib
import ast  # Necesario para convertir el texto del archivo a diccionario real

# 1. Definimos la ruta
inventario = pathlib.Path("prueba.txt")

# 2. SOLUCIÓN A LA AMNESIA: Cargar datos al iniciar
# Si el archivo existe, leemos el texto y lo convertimos a diccionario
if inventario.exists():
    try:
        contenido = inventario.read_text(encoding="utf-8")
        # ast.literal_eval convierte "{'A':1}" (texto) a {'A':1} (diccionario)
        hardware_diccionario = ast.literal_eval(contenido)
    except:
        hardware_diccionario = {}
else:
    hardware_diccionario = {}

def menu():
    print("---------")
    print("Menú")
    print("----------")
    print("1. Agregar hardware")
    print("2. Mostrar inventario")
    print("3. Eliminar Hardware")
    print("4. Salir")
    try:
        op = int(input("Elige una de las opciones: "))
        return op
    except ValueError:
        print("Opción inválida")
        return 0

def agregar(hardware, cantidad):
    hardware_diccionario[hardware] = cantidad
    # Usamos 'w' para guardar el cambio
    with open(inventario, "w", encoding="utf-8") as f:
        f.write(str(hardware_diccionario))
    print("Guardado.")

def mostrar():
    if inventario.exists():
        # Leemos directamente del archivo
        print(inventario.read_text(encoding="utf-8"))
    else:
        print("El inventario está vacío.")

def eliminar(hardware):
    if hardware in hardware_diccionario:
        del hardware_diccionario[hardware] 
        with open(inventario, "w", encoding="utf-8") as f:
            f.write(str(hardware_diccionario)) 
        print(f"{hardware} eliminado correctamente.")
    else:
        print(f"No se encontró {hardware} en el inventario.")

while True:
    rpta = menu()
    if rpta == 1:    
        hardware = input("Ingresa el hardware que deseas agregar: ").upper()
        try:
            cantidad = int(input("Ingresa la cantidad del hardware: "))
            agregar(hardware, cantidad)
        except ValueError:
            print("La cantidad debe ser un número.")
            
    elif rpta == 2:
        mostrar()
        
    elif rpta == 3:
        eliminar_hardware = input("Escribe el nombre a eliminar: ").upper()
        eliminar(eliminar_hardware)
        
    elif rpta == 4:
        break
    
    elif rpta < 1 or rpta > 4:
        print("Opción no válida")