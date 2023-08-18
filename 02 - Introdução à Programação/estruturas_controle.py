# PESSOAS ENTREVISTADAS IBGE

# Estruturas de Repetição com teste no início:

quantidade: int
contador: int

contador = 1

# Converte a entrada de dados para inteiro
quantidade = int(input("Quantas pessoas entrevistou hoje?"))


while contador <= quantidade:
	
	print ("Você entrevistou a pessoa de código 00", contador)
	contador +=1


# Estruturas de Repetição com variável de controle:

quantidade: int
contador: int

contador = 1

# Converte a entrada de dados para inteiro
quantidade = int(input("Quantas pessoas entrevistou hoje?"))


for contador in range(quantidade):
    contador +=1
    print ("Você entrevistou a pessoa de código 00", contador)