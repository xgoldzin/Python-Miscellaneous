print('TABUADA')
print()
print()
n1 = int(input('Insira um valor para saber a tabuada: '))
print()
n2 = int(input('Operação será de que valor(1 até 10)?'))
print()
n3 = int(input('Operação será até que valor(1 até 10)?'))
if n2 <= 0 or n3 > 10:
    print('NUMERO INVÁLIDO')

else:
    for x in range(n2, n3 +1):
        print(f'{n1} * {x} =', (n1 * x))
print()
if n2 <= 0 or n3 > 10:
    print('NUMERO INVÁLIDO')

else:
    for x in range(n2, n3 +1):
        print(f'{n1} / {x} =', (n1 / x))
print()
if n2 <= 0 or n3 > 10:
    print('NUMERO INVÁLIDO')

else:
    for x in range(n2, n3 +1):
        print(f'{n1} - {x} =', (n1 - x))
print()
if n2 <= 0 or n3 > 10:
    print('NUMERO INVÁLIDO')

else:
    for x in range(n2, n3 +1):
        print(f'{n1} + {x} =', (n1 + x))
