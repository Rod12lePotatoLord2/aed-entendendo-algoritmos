from src.my_node import MyNode


def merge_lists(l1: MyNode, l2: MyNode) -> MyNode:
    dummy = MyNode(0)
    atual = dummy
    
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            atual.next = l1
            l1 = l1.next
        else:
            atual.next = l2
            l2 = l2.next
        atual = atual.next
        
    if l1 is not None:
        atual.next = l1
    else:
        atual.next = l2
        
    return dummy.next
