#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def tem_duplicados(lista): #aqui temos a lista
        for valor in lista: #aqui ele vai percorrer a lista
            cont = 0
            for check in lista:
                if valor == check:
                    cont += 1
            if cont > 1:
                return True
        else:
            return False
                        


# Teste a sua função aqui (caso ache necessário)

print(tem_duplicados([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))








