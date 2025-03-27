class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        if l == None:
            return None
        elif l.next == None:
            return l
        else:
            r = l.next
            while r.next != None:
                temp = r.next
                r.next = l
                l = r
                r = temp
            r.next = l
            head.next = None
            head = r
        return head
                