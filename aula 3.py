#jogar no python console
'''
1==1 or 1==2
1!=1 and 1!=2
1<2  or 1>2
1<=2 and 1>=1
'''

# valores boolean
var_verdadeiro = True
var_false = False

print(type(var_verdadeiro),type(var_false))

#condicionais

if var_verdadeiro == True:
    print("var_verdade é verdadeiro")

if 1==1:
    print("1 é 1")

if 2>1:
    print("2 é maior que 1")

#utilizando o else

a=2
b=20

if a>b:
    print(a,'e maior do que ',b)
else:
    print(a,'nao e maior do que',b)

#utilizando and e or

c=30
d=50

if a>b and c<d:
    print(a,'e maior do que ',b )
else:
    print(a,'nao e maior do que',b,' e ',c,'é menor que ',d)

if a>b or c<d:
    print(a,'e maior do que ',b ,'ou', c,'e menor que ',d)
else:
    print(a,'nao e maior do que',b,' e ',c,'é menor que ',d)

