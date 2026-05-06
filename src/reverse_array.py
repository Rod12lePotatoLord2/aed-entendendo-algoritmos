from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    n = len(array)
    inicio = 0
    fim = n - 1

    while inicio < fim:
        valor_inicio = array[inicio]
        valor_fim = array[fim]

        array[inicio] = valor_fim
        array[fim] = valor_inicio

        inicio += 1
        fim -= 1

    return array
