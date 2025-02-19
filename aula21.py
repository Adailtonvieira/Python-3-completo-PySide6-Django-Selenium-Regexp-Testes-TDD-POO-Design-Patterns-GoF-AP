#Esse codigo não verifica os numeros negativos, eles serao considerados string e nao rodará!

primeiro_numero = input('Escreva um valor: ')
segundo_numero = input('Escreva outro valor: ')
if primeiro_numero.isdigit() and segundo_numero.isdigit():
    primeiro_numero = int(primeiro_numero)
    segundo_numero = int(segundo_numero)
    if int(primeiro_numero) >int(segundo_numero):
        print(f'O primeiro valor: {int(primeiro_numero)} é maior que o segundo valor {int(segundo_numero)}.')
    elif int(primeiro_numero)==int(segundo_numero):
        print(f'O primeiro valor: {int(primeiro_numero)} e o segundo valor: {int(segundo_numero)} são iguais.')
    else:
        print(f'O segundo valor: {int(segundo_numero)} é maior que o primeiro valor: {int(primeiro_numero)}.')
else:
    print('Digite um número válido, não uma string.')