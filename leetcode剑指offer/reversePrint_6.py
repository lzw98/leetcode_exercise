# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        value = []
        node = head

        while True:
            if node != None:
                value.append(node.val)
            else:
                break
            try:
                node = node.next
            except:
                break
        
        return value[::-1]
        
        