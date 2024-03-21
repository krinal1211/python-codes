class Solution(object):
    def reverseList(self, head):
        prev=None
        x=head
        while x:
            next=x.next
            x.next=prev
            prev=x
            x=next
        return prev

        
        
        
