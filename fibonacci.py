#entrada de dados
numero = int(input("Informe um número que deseja verificar se pertence à sequência fibonacci: "))

#declarando os dois valores iniciais
a = 0 
b = 1

#fazendo a primeira verificação se o número é 0 ou 1
if numero == 0 or numero == 1:
    print(f'O número {numero} pertence a sequência de fibonacci')

else:
    #laço de repetição que faz a verificação : soma os valores até dar o total do número digitado e verifica se o mesmo pertence a sequência ou não
    i = a + b 
    while i <= numero:
        if i == numero:
            print(f'o número {numero} pertence a sequência de fibonacci.')
            break   

        a = b
        b = i
        print(a,'+',b)
        i = a + b
        print('=',i)

    if i > numero:
        print(f'o número {numero} não pertence a sequência de fibonacci.')        