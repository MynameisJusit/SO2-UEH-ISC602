# Rango de tareas
# Iggnorar este .py
inicio = 16
fin = 43

for i in range(inicio, fin + 1):
    nombre_archivo = f"Tarea_{i}.html"
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("")  # Archivo vacío

print("Archivos generados correctamente.")