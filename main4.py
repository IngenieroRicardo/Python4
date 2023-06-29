try:
  file = open("archivo.txt", 'r')
  lineas = file.readlines()
  for linea in lineas:
    print(linea)
except:
  print("Error al abrir el archivo")
finally:
  quit()
