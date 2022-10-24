archivo=open("texto1.txt",'w') #r:read , w:sobreescribir(borra lo anterior), a:escribe a partir del último carácter. 
#También genera nuevos archivos, si el nombre aún no está ocupado.

archivo.write('Soy el nuevo texto.\nHola mundo')
archivo.write('''También puedo hacer con triple comillas.
Esto sirve como los comentarios
y respeta los saltos de línea.
''')

archivo.writelines(['concatena','todas','las','lineas', 'sin','espacios.'])

lista=['concatena','todas','las','lineas','espacios.']
for palabras in lista:
    archivo.writelines(palabras+'\n')


archivo.close() #SIEMPRE CERRAR EL ARCHIVO!!!

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())
