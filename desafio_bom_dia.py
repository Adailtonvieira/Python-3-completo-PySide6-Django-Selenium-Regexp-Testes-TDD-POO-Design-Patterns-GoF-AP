hora = input('Digite a hora inteira atual: ')

try: 
     hora = int(hora)
     if int(int(hora)) >= 0 and int(hora) <= 11:
          print('Bom dia!')
     elif int(hora) >= 12 and int(hora) <= 17:
          print('Boa tarde!')
     elif int(hora) >= 18 and int(hora) <= 23:
          print('Boa noite!') 
     else:
          int(hora) > 23 or int(hora) < 00
          print('Digite uma hora válida, entre 00 e 23')
except:
     print('Digite uma hora inteira (apenas 00H)')