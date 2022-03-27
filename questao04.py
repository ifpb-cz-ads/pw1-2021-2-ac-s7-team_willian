expressao = input('Digite a sequência de parênteses: ')
x = 0
pilha = []

while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')

    if expressao[x] == ')':
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(')')
            break
    x = x + 1
if len(pilha) == 0:
    print('Correto!');
else:
    print('Erro de sequencia');