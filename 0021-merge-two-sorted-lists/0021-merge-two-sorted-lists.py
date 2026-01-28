# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode()
        cur=new
        temp=list1
        temp2=list2
        while temp and temp2:
            if temp.val<=temp2.val:
                cur.next=temp
                temp=temp.next
            else:
                cur.next=temp2
                temp2=temp2.next
            cur=cur.next
        cur.next=temp if temp else temp2
        return new.next
    

            