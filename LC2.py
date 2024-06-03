class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1 = [2,4,3]
    l2 = [5,6,4]
    carry=0 #进位
    p=l1
    q=l2
    final=ListNode(0)
    k=final
    while p or q:
        s1=p.val if p else 0
        s2=q.val if q else 0
        n=s1+s2+carry
        carry=n//10
        res=n%10
        node=ListNode(res)
        k.next=node
        k=k.next
        if p:
            p=p.next
        if q:
            q=q.next
    if carry:
        node=ListNode(carry)
        k.next=node
    print(final.next)