# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum=0
        arr=[]
        temp = head
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        for i in range(len(arr)//2):
            s=arr[i]+arr[len(arr)-i-1]
            if max_sum<s:
                max_sum=s
        return max_sum
