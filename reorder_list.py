class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None
        second_half = self.reverse_linked_list(second_half)
        self.merge_alternatively(head, second_half)
        
    def find_middle(self, node):
        a = node
        b = node
        while b and b.next:
            a = a.next
            b = b.next.next
        return a
    
    def reverse_linked_list(self, node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def merge_alternatively(self, list1, list2):
        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            
            list1.next = list2
            list1 = temp1
            
            list2.next = list1
            list2 = temp2
