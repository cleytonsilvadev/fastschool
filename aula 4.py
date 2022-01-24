#aula 4 strings e lista
frase = 'oi, tudo bem?'
lista_nomes = ['Cleyton','Joao','Rodrigues']

                            #manipulando strings
#usando o type
print(type(lista_nomes))

print(lista_nomes)
print(lista_nomes[0])
print(lista_nomes[2])
print(frase[12])

#manipulando posições
print(frase[0:8:2])

#invertendo posiçoes
print(lista_nomes[-1:-4:-1])
print(frase[::-1])

#acrecentando string a lista
lista_nomes.append('geraldo')
print(lista_nomes)

#removento string da lista
lista_nomes.remove('Joao')
print(lista_nomes)

#limpando lista
lista_nomes.clear()

#add em uma posição
lista_nomes.insert(1,'eduarda')
lista_nomes.insert(4,'duda')
print(lista_nomes)

#contador
contador_a = lista_nomes.count('eduarda')
print(contador_a)
print(len(lista_nomes))

#removendo da lista no print
print(lista_nomes.pop())
print(lista_nomes)

#tudo maiúsculo
print(frase.upper())