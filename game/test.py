
queries = [
    'Iris, ¿cuántos amigos tengo?',
    'Ben, ¿dónde has estado?',
    'Ben, dame un abrazo!',
    'Iris, ¿quiénes son todos mis amigos?'
]

def check_query(query):
    lista1 = []
    for q in query:
        lista1.append(q)

    lista2 = []    
    lista3 = []

    for i in range(len(lista1)):
        lista2 = lista1[i].split(',')
        lista3.append(lista2[1])
        lista2 =[]

    print(lista3)

check_query(queries)
