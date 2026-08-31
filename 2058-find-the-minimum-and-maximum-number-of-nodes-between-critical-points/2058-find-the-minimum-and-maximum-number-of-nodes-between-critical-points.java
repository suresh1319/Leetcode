/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int[] ans = {-1,-1};
        ArrayList<Integer> criticalPoints = new ArrayList<>();
        if(head == null || head.next == null || head.next.next ==  null){
            return ans;
        }
        int cnt = 1;
        ListNode prev = head;
        ListNode curr = head.next;
        while(curr.next != null){
            if(((prev.val<curr.val)&&(curr.val>curr.next.val)) || ((prev.val>curr.val)&&(curr.val<curr.next.val))){
                criticalPoints.add(cnt);
            }
            prev = curr;
            curr = curr.next;
            cnt++;
        }
        if(criticalPoints.size()<2){
            return ans;
        }

        int n = criticalPoints.size();
        int maxDiff = criticalPoints.get(n-1)-criticalPoints.get(0);
        int minDiff = Integer.MAX_VALUE;
        for(int i=1;i<n;i++){
            minDiff = Math.min(minDiff,criticalPoints.get(i)-criticalPoints.get(i-1));
        }
        ans[0] = minDiff;
        ans[1] = maxDiff;
        return ans;
    }
}