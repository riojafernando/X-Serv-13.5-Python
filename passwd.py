#!usr/bin/python
# Abrimos el fichero
fd = open("/etc/passwd", "r")
# Leemos las lineas del fichero y creamos un diccionario vacio
lineas = fd.readlines()
dicc = {}

for linea in lineas:
    conf = linea.split(":")
    name = conf[0]
    shell = conf[-1]
    dicc[name] = shell
    
#Nos tenemos que quedar con el primer y ultimo elemento
print dicc["root"]
print len(dicc)


try:
    print dicc["Imaginario"]
except KeyError:
    print "Este usuario no existe"
