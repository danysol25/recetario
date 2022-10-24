from os import system

nombre=input('Ingresar nombre: ')
edad= input('Ingresar edad: ')

system('cls') #limpia lo anterior de la consola.

print(f'Tu nombre es {nombre}, y tienes {edad} años.')


def abrir_leer(archivo):
    archivo=open(archivo)
    return archivo.read()

def sobrescribir(archivo): #sobreescribir un documento
    archivo = open(archivo, 'w')
    return archivo.write("contenido eliminado")

def registro_error(archivo): #añadir info al final
    archivo = open(archivo, 'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()




