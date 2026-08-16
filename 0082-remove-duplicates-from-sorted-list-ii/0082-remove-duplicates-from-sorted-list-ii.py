class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if head is None:
            return None
        curr = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy 
        while curr and curr.next:
            temp = curr.next
            if temp and temp.val != curr.val:
                prev = curr
                curr = curr.next
            else: 
                while temp and temp.val == curr.val:
                    temp = temp.next
                prev.next = temp 
                curr = temp 
        return dummy.next 
