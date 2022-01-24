#estrutura de laço for and while

#for
nomes=['cleyton','rodrigues','silva','luiz','alberto','filho']
print(nomes)

for nome in nomes:
    print(nome)

lista_de_numeros=range (5,10)

for item in lista_de_numeros:
    print(item)

'''
lista_de_numeros= range(0,100,2)

for par in lista_de_numeros:
    print(par)
    
ou 

for par in range(0,100,2):
    print(par)

'''

for i in range(len(nomes)):
    print(nomes[i])

palavras ='cleyton rodrigues'
for letra in palavras:
    print(letra)

#while

x = 0
while x < 10:
    print('i ainda é menor que 10: ',x)
    x = x + 1
print('acabou o while: ',x)

# tome cuidado com loops
y=0
while True:
    print('loop infinito: ',y)
    if y == 10:
        break
    y+=1
print('saiu do while')
