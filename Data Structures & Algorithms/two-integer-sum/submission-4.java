class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> map = new HashMap<>();
        int i = 0;
        int[] sol = new int[2];

        for(int n: nums){
            map.put(n, i);
            i++;
        }

        for(int n = 0; n < nums.length; n++){
            if(map.containsKey(target - nums[n]) && map.get(target-nums[n]) != n){
                sol[0] = Math.min(n, map.get(target-nums[n]));
                sol[1] = Math.max(n, map.get(target-nums[n]));
                break;
            }
        }

        return sol;
    }
}
