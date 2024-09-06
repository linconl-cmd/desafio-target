#entrada de dados 
entrada = input("Digite uma string: ")

#variavel contagem recebe a entrada com o metodo lower que transforma a letra que entrar em minuscula padronizando o dado pra ser melhor filtrado, e o count faz a contagem da letra 'a'
contagem = entrada.lower().count('a')


#verifica na variavel contagem se é maior que 0 pra poder passar a condicional ou não 
if contagem > 0:
    print(f"Foi encontrada a letra 'a' na string e ela foi digitada {contagem} vezes")

else:
    print("Não foi encontrada letra 'a' na string.")    