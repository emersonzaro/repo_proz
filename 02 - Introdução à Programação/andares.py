
# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)


def andares():
    print("Hotel tem 20 andares")
    andar = 0
    for andar in range(1,21,1):
        if(andar != 13):
            print("O número do andar é:", andar)
andares()

# ordem decrescente

def andares():
    print("Hotel tem 20 andares")
    andar = 20
    while(andar >= 1):
        if(andar != 13):
            print("O número do andar é:", andar)
        andar -= 1    
andares()

def andares():
    print("Hotel tem 20 andares")
    andar = 21
    for andar in range(20,0,-1):
        if(andar != 13):
            print("O número do andar é:", andar)
andares()