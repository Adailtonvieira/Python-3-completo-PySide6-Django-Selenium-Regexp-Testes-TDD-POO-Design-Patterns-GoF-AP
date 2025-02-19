lista_de_compras = []
escolha = 0
import os


while escolha != 4:

    escolha = input('\n\t\tMENU\n\n'
        '1- Para adicionar item á lista: \n'
        '2- Para remover item da lista: \n'
        '3- Para listar itens da lista: \n'
        '4- Para sair.\n'
        'Digite a opção desejada: ')
    
    if escolha == '1':
        add_iten = input('Digite o iten: ')
        lista_de_compras.append(add_iten)
        os.system('cls')
        print(f'Item {add_iten} adicionado à lista!\n')
        continue

    if escolha == '2':
        remover = input('Digite o iten que deseja remover da lista: ')  
        if remover in lista_de_compras:
            lista_de_compras.remove(remover)
            os.system('cls')
            print(f'Item {remover} removido da lista!\n')
            continue

        else:
            os.system('cls')
            print(f'Item {remover} não encotrado!\n')
            continue

    if escolha == '3':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Sua lista de compras esta vazia!')
            continue

        else:
            print('Sua lista de compra é:')
            for item in enumerate(lista_de_compras):
                a, b = item
                print(a, b)
        continue

    if escolha == '4':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Sua lista de compras ainda esta vazia!\n\n')
            ultimate = input('Deseja poder adicionar algo antes de sair ?\n\n'
            '[S]im  \t\t [N]ão (qq outra tecla)')
            if ultimate == 's' or ultimate == 'S':
                continue

            else:
                break

        else:
            print('Sua lista de compra é:')
            for item in enumerate(lista_de_compras):
                a, b = item
                print(a, b)
        break

    if escolha != '1' or '2' or '3' or '4':
        print('Por favor digite uma opção válida abaixo!')
    continue

