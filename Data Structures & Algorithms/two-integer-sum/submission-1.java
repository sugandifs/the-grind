class Solution {
    public int[] twoSum(int[] nums, int target) {
        int sum = 0;
        int[] ans = new int[2];
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                sum = nums[i] + nums[j];
                if(sum == target && i != j){
                    ans[0] = j;
                    ans[1] = i;
                }
            }
        }

        return ans;
    }
}
