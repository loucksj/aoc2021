import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = l1.val
    i = 1
    while l1.next != None:
        l1 = l1.next
        a += l1.val * pow(10, i)
        i += 1
    b = l2.val
    i = 1
    while l2.next != None:
        l2 = l2.next
        b += l2.val * pow(10, i)
        i += 1
    
    sum = a + b
    
    if sum == 0:
        return ListNode(0)

    sum_len = int(math.log10(sum))+1
    
    backsum = 0
    i = 0
    while sum != 0:
        backsum = 10 * backsum + (sum % 10)
        sum = sum//10
        i += 1

    backsum_len = int(math.log10(backsum))+1
    
    l = ListNode(backsum % 10)
    while backsum > 9:
        backsum = backsum // 10
        l = ListNode(backsum % 10, l)
    
    for _ in range(sum_len - backsum_len):
        l = ListNode(0, l)

    return l

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = addTwoNumbers(l1, l2)
    assert 7 == l3.val
    assert 0 == l3.next.val
    assert 8 == l3.next.next.val
    
    assert 0 == addTwoNumbers(ListNode(0), ListNode(0)).val

    l1 = ListNode(5, ListNode(6))
    l2 = ListNode(5, ListNode(4, ListNode(9)))
    l3 = addTwoNumbers(l1, l2)
    assert 0 == l3.val
    assert 1 == l3.next.val
    assert 0 == l3.next.next.val
    assert 1 == l3.next.next.next.val