perguntas = [
    {
        'Pergunta': 'Quantos é 2+2 ?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quantos é 5*5 ?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quantos é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for i, opcao in (pergunta['Opções']):

        print(opcao)

    escolha = input('Escolha uma opção: ')
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        ...

    if escolha_int == enumerate(pergunta['Resposta']):
        print('Voce acertou!')
    else:
        print('Você errou!')