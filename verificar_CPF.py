import re

entrada = input('Digite o CPF: ')
entrada = re.sub( r'[^0-9]', '', entrada )


nove_digitos = entrada[:9] 
contador_regressivo = 10

resultado_digito_1 = 0


#PRIMEIRO DIGITO

for digito in nove_digitos:
    resultado_digito_1 += (int(digito)*contador_regressivo)
    contador_regressivo -= 1

primeiro_digito = ((resultado_digito_1 * 10) % 11)

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

#SEGUNDO DIGITO 

dez_digitos = nove_digitos + str(primeiro_digito)
contador_regressivo_2 = 11

resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += (int(digito)*contador_regressivo_2)
    contador_regressivo_2 -= 1

segundo_digito = ((resultado_digito_2 * 10) % 11)
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print(cpf_gerado)

if entrada == cpf_gerado:
    print(f'O CPF {entrada} é válido!')
else:
    print(f'O CPF {entrada} é inválido!')