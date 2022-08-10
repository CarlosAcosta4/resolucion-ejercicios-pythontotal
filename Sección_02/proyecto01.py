import os
os.system('cls')
numero = 45.66666

nombre = input('Introduce tu nombre: ')
ventas = int(input('Introduce las ventas totales del mes: '))

comisiones = round(((ventas * 13) / 100),2)

print(f'Hola {nombre},tus comisiones de este mes son de ${comisiones}')