from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    pivo = array.get(len(array) - 1)
    menores = MyArray()
    maiores = MyArray()

    for i in range(len(array) - 1):
        if array.get(i) < pivo:
            menores.insert(len(menores), array.get(i))
        else:
            maiores.insert(len(maiores), array.get(i))

    ordenados_menores = quick_sort(menores)
    ordenados_maiores = quick_sort(maiores)

    resultado = MyArray()
    idx = 0
    for i in range(len(ordenados_menores)):
        resultado.insert(idx, ordenados_menores.get(i))
        idx += 1

    resultado.insert(idx, pivo)
    idx += 1

    for i in range(len(ordenados_maiores)):
        resultado.insert(idx, ordenados_maiores.get(i))
        idx += 1

    return resultado
