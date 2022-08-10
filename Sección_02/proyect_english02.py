import os
os.system('cls')

num = 45.66666

name = input('Introduce your name: ')
sales = int(input('Enter the total sales for the month: '))

commissions = round(((sales * 13) / 100),2)

print(f'Hello {name},your commissions this month are ${commissions}')