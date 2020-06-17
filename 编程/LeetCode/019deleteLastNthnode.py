# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #1th Solution
    def removeNthFromEnd01(self, head: ListNode, n: int) -> ListNode:
        #get list len
        list_num = 0
        pre = curr = ListNode(0)
        curr  = head 
        while curr != None:
            list_num += 1
            curr = curr.next

        #delete node
        d_location = list_num - n + 1
        #if delete head node
        if d_location == 1:
            head = head.next
        else:
            curr = head
            for i in range(d_location-1):
                pre_node = curr
                curr = curr.next
            pre_node.next = curr.next
        #return head
        while head != None:
            print(head.val)
            head = head.next   
    #2nd solution快慢指针

s = Solution()
s1 = ListNode(1)
s2 = ListNode(2)
s3 = ListNode(3)
s4 = ListNode(4)
s5 = ListNode(5)
s1.next = s2
s2.next = s3
s3.next = s4
s4.next = s5
s5.next = None
s.removeNthFromEnd01(s1,5)