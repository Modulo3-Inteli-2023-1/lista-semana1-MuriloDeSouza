#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def cumulativo(lista):
    lista2 = [lista[0]]
    for i in range(len(lista)-1):
        lista2.append(lista2[i]+lista[i+1])

    return lista2

# Teste a sua função aqui (caso ache necessário)











