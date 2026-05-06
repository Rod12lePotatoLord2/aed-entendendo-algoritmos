from src.my_node import MyNode

def remove_duplicates(head: MyNode) -> MyNode:
    if head is None:
        return None
    
    atual = head
    while atual is not None:
        corredor = atual
        while corredor.next is not None:
            if corredor.next.value == atual.value:
                corredor.next = corredor.next.next
            else:
                corredor = corredor.next
        atual = atual.next
            
    return head
