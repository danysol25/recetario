mi_archivo = open('prueba.txt')

print(mi_archivo.readlines(2)) #lee la primer línea
print(mi_archivo.readline()) #lee lo siguiente.

eliminar_saltos_de_linea = mi_archivo.readline()
print(eliminar_saltos_de_linea.rstrip()) 

todo_el_contenido = mi_archivo.read()
print(todo_el_contenido) #lee todo el contenido




















mi_archivo.close()