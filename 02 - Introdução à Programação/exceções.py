def mostrar_numero():
    numero_valido = False

    print("Escreva um número menor ou igual a 100")

    while (numero_valido == False):
        try:
            num = int(input())
            if (num > 100):
                print("O número precisa ser menor ou igual a 100")
            else:
                print("Boa! Você escolheu o número" + str(num))
                numero_valido = True
        except:
            print("O valor inserido deve ser um número inteiro")

mostrar_numero()