''' DESAFIO
Itere sobre a lista abaixo exibindo o número do índice + nome
da fruta. Porém quando o índice for 3, exibana 'Nº índice +
nome da fruta em promoção'''
frutas = ['Marça', 'Laranja', 'Morango', 'Limão']
for indice, fruta in enumerate(frutas):
    print(indice, fruta, "EM PROMOÇÃO")