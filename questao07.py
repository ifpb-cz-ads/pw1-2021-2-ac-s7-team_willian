L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a ser procurado(P): "))
v = int(input("Digite o segundo valor a ser procurado(V): "))
achou = ""
posicaoP = False
posicaoV = False
x = 0
while x < len(L):
    if L[x] == p:
        posP = "p"
        break
    elif L[x] == v:
        posV = "v"
        break
    x += 1


if not posicaoV is False and not posicaoP is False:
    print("%d achado na posição %d e %d achado na posição %d" % (p, posicaoP, v, posicaoV))
elif not posicaoV is False:
    print("%d achado na posição %d e %d não encontrado" % (v, posicaoV, p))
elif not posicaoP is False:
    print("%d achado na posição %d e %d não encontrado" % (p, posicaoP, v))
else:
    print("%d e %d não foram encontrados" % (p, v))