class Solution:
    def removeZeroSumSublists(self, head):
        
        dictionary={}
        summ=0
        extra_node=ListNode(0,head)
        temp=extra_node
        while(temp!=None):
            summ=summ+temp.val
            dictionary[summ]=temp
            temp=temp.next
        summ=0
        temp=extra_node
        while(temp!=None):
            summ=summ+temp.val
            temp.next=dictionary[summ].next
            temp=temp.next
        return extra_node.next

