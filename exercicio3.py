#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui


def soma_dos_aninhados(lista):
    soma= 0
    for i in range(len(lista)): #aqui é para percorrer a lista como um todo/ as 3 listas dentro da lista principal 
        for j in range(len(lista[i])): #depois ele vai percorrer as 3 listas formadas
            soma += lista[i][j] #aqui ele vai somar os valores de que foi pegado na lista j/ os 3 valores
    return soma#faz a soma das listas
    # print(sum(lista[i][j]))   




# Teste a sua função aqui (caso ache necessário)











