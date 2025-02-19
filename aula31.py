#usa-se None quando se cria uma variavel mas no momento nao é possivel designar um valor a ela
#None significa vázio. Sempre é escrito com N maiusculos.

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Não faça nada')
print(id(passou_no_if)) #endereço em que a variavel esta alocada na memória

if passou_no_if is None:
    print('Passou no IF')
else:
    print('Não passou no IF..')