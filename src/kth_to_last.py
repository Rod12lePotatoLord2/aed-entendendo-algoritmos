from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int):
    if head is None or k <= 0:
        return -1
        
    ponteiro_frente = head
    ponteiro_tras = head
    
    for _ in range(k):
        if ponteiro_frente is None:
            return -1
        ponteiro_frente = ponteiro_frente.next
        
    while ponteiro_frente is not None:
        ponteiro_frente = ponteiro_frente.next
        ponteiro_tras = ponteiro_tras.next
        
    return ponteiro_tras.value
