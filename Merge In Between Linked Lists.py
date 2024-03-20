# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        x=list1
        y=list2
        while b:
            x=x.next
            b-=1
        while y.next:
            y=y.next
        y.next=x.next
        x=list1
        while a-1:
            x=x.next
            a-=1
        x.next=list2
        return list1
        
