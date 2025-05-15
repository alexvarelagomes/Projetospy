#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

Lista2 = []

while True:
    n = input('Fale um numero:').strip() # ".strip() serve para remover os espaços em branco (e outros caracteres invisíveis, como quebras de linha.
    if n == '':
        print('Por gentileza digite um número:')
        continue
    if not n.isdigit(): # ".isdigit" verifica se todos os caracteres da string são dígitos númericos. Ex: 12a5 e/ou 12 3.
        print('Por gentileza digite um número:')
        continue

    
    if n not in Lista2:
            Lista2.append(n) # Adiciona elementos na lista.
        
    continuar= input('Você quer continuar? S/N: ').strip().upper()
    
    if continuar == 'N':
        break
    elif continuar in ['',' ']:
        print('Por gentileza, digite S ou N:')
        continue

Lista2.sort() #.Sort" coloca os números em ordem.
repeat = set(Lista2) # "Set" remove repetições.
print(f'Essa é a lista dada pelo usuário: {Lista2}')
print('OI')

    



