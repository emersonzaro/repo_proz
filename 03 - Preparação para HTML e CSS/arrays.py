def achar_elemento(elem, arr):
    achou = False
    cumprimento = len(arr)

    for i in range(cumprimento):
        if (arr[i] == elem):
            achou = True
    
    if achou:
        print("Achei o nome: " + elem)
    else:
        print("Não achei o nome: " + elem)

nomes = ['Emerson', 'Rafa', 'Adriana']

#achar_elemento('Emerson', nomes)
achar_elemento('Luis', nomes)