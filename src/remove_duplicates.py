from src.my_node import MyNode

def remove_duplicates(head: MyNode) -> MyNode:
    if head is None:
        return None
    
    valores_vistos = set()
    atual = head
    valores_vistos.add(atual.value)
    
    while atual.next is not None:
        if atual.next.value in valores_vistos:
            atual.next = atual.next.next
        else:
            valores_vistos.add(atual.next.value)
            atual = atual.next
            
    return head
