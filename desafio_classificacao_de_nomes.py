nome = input('Digite seu primeiro nome: ')

if len(nome)>1:
     if len(nome) <= 4:
          print(f'Seu nome é {nome.capitalize()}, ele é curto e contém:', len(nome), 'letras.')
     elif len(nome) >= 5 and len(nome) <= 6:
          print(f'Seu nome é {nome.capitalize()}, ele é normal e contém:', len(nome), 'letras.')
     else:
          print(f'Seu nome é {nome.capitalize()}, e ele é longo e contém:', len(nome), 'letras.')
else: 
     print('Digite pelo menos duas letras!')