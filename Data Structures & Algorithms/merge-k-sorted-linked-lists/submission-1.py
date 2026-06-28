# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        return lists[-1]
    
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val < head2.val:
            head = head1
            curr1 = head1.next
            curr2 = head2
        else:
            head = head2
            curr2 = head2.next
            curr1 = head1
        curr = head

        while curr1 and curr2:
            #print(curr1.val, curr2.val)
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        #print(curr1, curr2)
        if curr1:
            while curr1:
                #print(curr1.val, curr.val)
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
        if curr2:
            while curr2:
                #print(curr2.val, curr.val)
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
        return head
        
