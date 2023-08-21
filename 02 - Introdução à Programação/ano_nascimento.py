
# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2023).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


nome= input("Digite seu nome: ")

executar = True

while(executar == True):
  print("Digite seu ano de nascimento:")
  try:
    ano = int(input())
    if(ano < 1922) or (ano > 2022):
      print("O ano precisa ser entre 1922 a 2022")
    else:
      idade = (2023 - ano)
      print("O usuario", nome, "completou ou completará", idade, "anos de idade em 2023")
      executar = False
  except:
     print("Os anos precisam ser escritos apenas com numeros")
