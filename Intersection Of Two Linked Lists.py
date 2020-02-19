#https://leetcode.com/problems/intersection-of-two-linked-lists
class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        currA = headA
        while currA:
            s.add(currA)
            currA = currA.next
        currB = headB
        while currB:
            if currB in s:
                return currB
            currB = currB.next
        return None