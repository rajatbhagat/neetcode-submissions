# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        res = list3

        while list1 != None and list2 != None:
            if list1.val == list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val < list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list2 = list2.next
            list3 = list3.next

        while list1 != None:
            list3.next = ListNode(list1.val)
            list3 = list3.next
            list1 = list1.next

        while list2 != None:
            list3.next = ListNode(list2.val)
            list3 = list3.next
            list2 = list2.next
        return res.next