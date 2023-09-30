# filter
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
def pessoas_aprovadas(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False
print(list(filter(pessoas_aprovadas, nomes)))
print(list(map(pessoas_aprovadas, nomes)))

pinturas = [
    ['Pintura Classica', 'Azul', 1857], 
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]
def eh_antguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False

print(list(filter(eh_antguidade, pinturas)))
print(list(map(eh_antguidade, pinturas)))