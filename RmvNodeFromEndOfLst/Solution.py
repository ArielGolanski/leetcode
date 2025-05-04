class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        counter = 0
        copy = head
        while copy:
            counter+=1
            copy = copy.next
        
        copy = head
        prev = dummy
        for i in range(counter - n):
            copy = copy.next
            prev = prev.next
        prev.next = copy.next
        return dummy.next