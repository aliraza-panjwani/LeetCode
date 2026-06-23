class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return head1