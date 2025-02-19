pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Silva',
}

cantores = {
    'nome_fic': 'Luan',
    'idade': 43,
}

print(pessoa)
pessoa.popitem()
print(pessoa)
print(cantores)

pessoa.update(cantores)

print(pessoa)
print(cantores)

pessoa.update({
    'RG': 4457
})
print(pessoa)

tupla = [('nome', 'novo_nome'), ('idadesss', 30)]
pessoa.update(tupla)

print(pessoa)