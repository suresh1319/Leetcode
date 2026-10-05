class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int i = 0;
        while(i<n){
            int corr = nums[i];
            if( corr<n && nums[corr] != nums[i]){
                int temp = nums[corr];
                nums[corr] = nums[i];
                nums[i] = temp;
            }
            else{
                i++;
            }
        }
        for(int j=0;j<n;j++){

            if(nums[j] != j){
                return j;
            }
        }
        return n;
    }
}