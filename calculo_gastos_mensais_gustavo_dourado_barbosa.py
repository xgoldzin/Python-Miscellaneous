print('----------------------------------------------------------------------------')
print('                            CALCULO DE DÍVIDAS                              ')
print('----------------------------------------------------------------------------')
print()
print()
print()
transp = []
gast_transp = 1
educ = []
gast_educa = 1
laz = []
gast_lazer = 1
cont_fix = []
gast_fix = 1
merc = []
gast_mercado = 1
while True:
    quant = int(input(f'Quantas vezes você gastou com Transporte?'))
    if quant >= 0:
        for passagem in range(quant):
            div_a = float(input(f'Insira seu {gast_transp}º gasto com Transporte:'))
            if div_a > 0:
                transp.append(div_a)
                gast_transp += 1
            while div_a <= 0:
                print('Número inválido!Insira um número maior que zero.')
                div_a = float(input(f'Insira seu {gast_transp}º gasto com Transporte:'))
                if div_a > 0:
                    transp.append(div_a)
                    gast_transp += 1
            else:
                while quant < 0:
                    print('Número Inválido!Insira um número maior ou igual a zero.')
                    quant = int(input(f'Quantas vezes você gastou com Transporte?'))
    
    print()

    quant_2 = int(input('Quantas vezes você gastou com Educação?'))
    if quant_2 >= 0:
        for passagem_2 in range(quant_2):
            div_b = float(input(f'Insira seu {gast_educa}º gasto com Educação:'))
            if div_b > 0:
                educ.append(div_b)
                gast_educa += 1
            while div_b <= 0:
                print('Número inválido!Insira um número maior que zero.')
                div_b = float(input(f'Insira seu {gast_educa}º gasto com Educação:'))
                if div_b > 0:
                    educ.append(div_b)
                    gast_educa += 1
            else:
                while quant_2 < 0:
                    print('Número Inválido!Insira um número maior ou igual zero.')
                    quant_2 = int(input(f'Quantas vezes você gastou com Educação?'))
    
    print()
       
    quant_3 = int(input('Quantas vezes você gastou com Lazer?'))
    if quant_3 >= 0:
        for passagem_3 in range(quant_3):
            div_c = float(input(f'Insira seu {gast_lazer}º gasto com Lazer:'))
            if div_c > 0:
                laz.append(div_c)
                gast_lazer += 1
            while div_c <= 0:
                print('Número inválido!Insira um número maior que zero.')
                div_c = float(input(f'Insira seu {gast_lazer}º gasto com Lazer:'))
                if div_c > 0:
                    laz.append(div_c)
                    gast_lazer += 1
            else:
                while quant_3 < 0:
                    print('Número Inválido!Insira um número maior que zero.')
                    quant_3 = int(input(f'Quantas vezes você gastou com Lazer?'))
    
    print()
            
    quant_4 = int(input('Quantas vezes você gastou com Gastos Fixos?'))
    if quant_4 >= 0:
        for passagem_4 in range(quant_4):
            div_d = float(input(f'Insira seu {gast_fix}º gasto com Gastos Fixos:'))
            if div_a > 0:
                cont_fix.append(div_d)
                gast_fix += 1
            while div_d <= 0:
                print('Número inválido!Insira um número maior que zero.')
                div_d = float(input(f'Insira seu {gast_fix}º gasto com Gastos fixos:'))
                if div_d > 0:
                    cont_fix.append(div_d)
                    gast_fix += 1

            else:
                while quant_4 < 0:
                    print('Número Inválido!Insira um número maior ou igual a zero.')
                    quant_4 = int(input(f'Quantas vezes você gastou com Gastos Fixos?'))
    
    print()
                
    quant_5 = int(input('Quantas vezes você gastou com Mercado?'))
    if quant_5 >= 0:
        for passagem_5 in range(quant_5):
            div_e = float(input(f'Insira seu {gast_mercado}º gasto com Mercado:'))
            if div_e > 0:
                merc.append(div_e)
                gast_mercado += 1
            while div_e <= 0:
                print('Número inválido!Insira um número maior que zero.')
                div_e = float(input(f'Insira seu {gast_mercado}º gasto com Mercado:'))
                if div_e > 0:
                    merc.append(div_e)
                    gast_mercado += 1
            else:
                while quant_5 < 0:
                    print('Número Inválido!Insira um número maior ou igual a zero.') 
                    quant_5 = int(input(f'Quantas vezes você gastou com Mercado?'))
                    
                        
            
    
    print()
    soma_a = sum(transp)
    soma_b = sum(educ)
    soma_c = sum(laz)
    soma_d = sum(cont_fix)
    soma_e = sum(merc)

    soma_t = soma_a + soma_b + soma_c + soma_d + soma_e
    print('RESULTADO FINAL:')
    print('_________________________________________')
    print()
    print(f'-Gastos em Transporte:R${soma_a}')
    print(f'-Gastos em Educação:R${soma_b}')
    print(f'-Gastos em Lazer:R${soma_c}')
    print(f'-Gastos em Custos Fixos:R${soma_d}')
    print(f'-Gastos em Mercado:R${soma_e}')
    print(f'-Gasto total em reais R$:{soma_t}')

    fm = input('Deseja encerrar o programa?(sim ou não)')
    if fm.lower() != 'não':
        break
    print()
