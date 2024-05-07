class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head.val == 0 and not head.next):
            return head

        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        n = len(result)

        carry = 0
        for i in range(n-1,-1,-1):
            result[i] = result[i] * 2 + carry
            carry = result[i] // 10
            result[i] %= 10
        if carry:
            result.insert(0, carry)

        dummyHead = ListNode()
        current = dummyHead
        for val in result:
            current.next = ListNode(val)
            current = current.next
            
        return dummyHead.next
        
