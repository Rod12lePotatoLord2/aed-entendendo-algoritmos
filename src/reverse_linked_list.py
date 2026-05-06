from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    anterior = None
    atual = head
    while atual is not None:
        proximo_no = atual.next
        atual.next = anterior
        anterior = atual
        atual = proximo_no
    return anterior
