def multi(*args):
    numeros = (1, 2, 3, 4, 5)
    total = 1
    for numero in args:
        total *= numero
    return total

def numero(numero):
    if multiplicar % 2 == 0:
        return (f'O numero {multiplicar} é par.')
    return (f'O numero {multiplicar} é impar.')

multiplicar = multi(1, 3, 3)
print(multiplicar)

impar_par = numero(multiplicar)
print(impar_par)