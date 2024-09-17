# Difficulty level: easy

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            copy1 = list1
            copy2 = list2

            lst = ListNode()
            result = lst

            while copy1 and copy2:
                if copy1.val < copy2.val:
                    result.next = copy1
                    copy1 = copy1.next
                else:
                    result.next = copy2
                    copy2 = copy2.next
                result = result.next
            if copy1:
                result.next = copy1
            else:
                result.next = copy2
            return lst.next                     
