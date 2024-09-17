# Difficulty level: easy

# Given the beginning of a singly linked list head,
# reverse the list, and return the new beginning of the list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        copy = head 
        stack = []
        while(copy):
            stack.append(copy.val)
            copy = copy.next
        copy2 = head
        while(copy2):
            copy2.val = stack.pop()
            copy2 = copy2.next
        return head        