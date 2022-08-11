import os
os.system('cls')

print('----------ANALIZADOR DE TEXTO----------')
texto = input('Ingresa un texto:\n ')
texto = texto.lower()
letras = []

letras.append(input('Ingresa la 1era letra: ').lower())
letras.append(input('Ingresa la 2da letra: ').lower())
letras.append(input('Ingresa la 3era letra: ').lower())

cantLetras1 = texto.count(letras[0])
cantLetras2 = texto.count(letras[1])
cantLetras3 = texto.count(letras[2])

print('')
print('==========Contador de Letras===========')
print(f"La letra '{letras[0]}' aparece {cantLetras1} veces")
print(f"La letra '{letras[1]}' aparece {cantLetras2} veces")
print(f"La letra '{letras[2]}' aparece {cantLetras3} veces")

print('')

listaTexto = texto.split()
letra_inicio = texto[0]
letra_final = texto[-1]
textoInvertido = texto[::-1] 

print('=========Analizando el texto===========')
print(f'El texto tiene {len(listaTexto)} palabras')
print(f"La primera letra es '{letra_inicio}'")
print(f"La ultima letra es '{letra_final}'")
print(f"El orden inverso del texto es:\n'{textoInvertido}'")

print('')
encontrarPalabra = 'python' in texto
diccionario = {True: 'si aparece en el texto', False:'no aparece en el texto',}
verificacion = diccionario[encontrarPalabra]
print(f'La palabra python {verificacion}')
print('=======================================')