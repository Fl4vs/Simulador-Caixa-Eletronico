while True:
    print('-=-'*12)
    valor = input('Digite o valor a ser sacado: R$').strip()
    enum = valor.isnumeric()
    if enum == False:
        print('Você digitou algo inválido. Tente novamente.')
    else:
        valor = int(valor)
        if valor <= 0:
            print('Você digitou algo inválido. Tente novamente.')
        else:
            print('---'*12)
            n50 = valor // 50
            n20 = valor % 50 // 20
            n10 = valor % 50 % 20 // 10
            n01 = valor % 50 % 20 % 10 // 1
            if n50 > 0:
                print(f'Total de {n50} cédulas de R$50')
            if n20 > 0:
                print(f'Total de {n20} cédulas de R$20')
            if n10 > 0:
                print(f'Total de {n10} cédulas de R$10')
            if n01 > 0:
                print(f'Total de {n01} cédulas de R$1')
            print('{:¨^40}'.format('FIM DO PROGRAMA'))
            break
