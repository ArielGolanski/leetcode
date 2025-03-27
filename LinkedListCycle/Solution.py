class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head.next == None or head == None:
            return False
        
        f, s = head.next.next, head.next
        
        while s and f:
            if s == f:
                return True
            else:
                s = s.next
                f = f.next.next
        return False