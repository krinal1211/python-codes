# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=[]
        y=head
        while y:
            a.append(y.val)
            y=y.next
        print(a) 
        b=list(reversed(a))
        print(b) 
        if a==b:
            return True
        else:
            return False


        
        
