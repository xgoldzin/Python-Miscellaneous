print('PEDRA,PAPEL E TESOURA')
import random
lista_j = ['Pedra','Papel','Tesoura']
ganho = []
vida = [1,2,3]
empate = []
print('*' * 40)
print('REGRAS:')
print('1.Você tem 3 vidas iniciais')
print('2.A cada 3 rodadas ganhas,ganhe uma vida')
print('3.A cada dois empates,ganhe uma vida')
print('4.A cada rodada perdida perca uma vida')
print('*' * 40)
while True:
    sorteio = random.choice(lista_j)
    elem = str(input('Insira pedra,papel, ou tesoura:')).lower()
    while elem not in ('pedra','papel','tesoura'):
        print('Insira pedra papel ou tesoura!')
        print()
        elem = str(input('Insira pedra,papel, ou tesoura:')).lower()
    else:
        if elem == 'pedra' and sorteio == 'Tesoura':
            print('Pedra vence Tesoura,ganhou!')
            print('Quantidade de vidas:',len(vida))
            print()
            ganho.append(elem)
        elif elem == 'papel' and sorteio == 'Pedra':
            print('Papel vence pedra, ganhou!')
            print('Quantidade de vidas:',len(vida))
            print()
            ganho.append(elem)
        elif elem == 'tesoura' and sorteio == 'Papel':
            print('Tesoura vence papel, ganhou!')
            print('Quantidade de vidas:',len(vida))
            print()
            ganho.append(elem)
        elif elem == sorteio:
            print('Empate!Tente denovo')
            print('Quantidade de vidas:',len(vida))
            empate.append(elem)
            if len(empate) == 2:
                vida.append(elem)
                empate.clear()
                print()
        else:
            vida.pop()
            print('Você perdeu!Perca uma vida')
            print('Quantidade de vidas:',len(vida))
            if len(ganho) == 3:
                vida.append(elem)
                ganho.clear()
            print()
        if len(vida) == 0:
            print('Game Over!')
            break
        elif len(vida) == 5:
            print('Você venceu!')
            break
