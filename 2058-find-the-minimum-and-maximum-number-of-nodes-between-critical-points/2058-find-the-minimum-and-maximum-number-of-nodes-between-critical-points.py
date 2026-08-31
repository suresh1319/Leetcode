# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalPoints = []
        if head is None or head.next is None or head.next.next is None:
            return [-1,-1]
        temp = head.next
        prev = head
        cnt = 1
        while temp.next:
            if prev.val>temp.val<temp.next.val:
                criticalPoints.append(cnt)
            if prev.val<temp.val>temp.next.val:
                criticalPoints.append(cnt)
            prev = temp 
            temp=temp.next 
            cnt += 1
        if len(criticalPoints)<2:
            return [-1,-1]
        minDiff = float('inf')
        for i in range(1,len(criticalPoints)):
            minDiff = min(minDiff,criticalPoints[i]-criticalPoints[i-1])
        maxDiff = criticalPoints[-1]-criticalPoints[0]
        return [minDiff,maxDiff]

