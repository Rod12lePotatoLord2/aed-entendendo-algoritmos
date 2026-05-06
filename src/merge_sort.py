from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    meio = len(array) // 2

    esquerda = MyArray()
    direita = MyArray()

    for i in range(meio):
        esquerda.insert(i, array.get(i))
    for i in range(meio, len(array)):
        direita.insert(i - meio, array.get(i))

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)


def merge(esquerda: MyArray, direita: MyArray) -> MyArray:
    resultado = MyArray()
    i = j = k = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda.get(i) <= direita.get(j):
            resultado.insert(k, esquerda.get(i))
            i += 1
        else:
            resultado.insert(k, direita.get(j))
            j += 1
        k += 1

    while i < len(esquerda):
        resultado.insert(k, esquerda.get(i))
        i += 1
        k += 1
    while j < len(direita):
        resultado.insert(k, direita.get(j))
        j += 1
        k += 1

    return resultado
