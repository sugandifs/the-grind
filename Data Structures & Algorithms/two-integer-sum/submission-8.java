class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sol = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(target-nums[i])){
                int sol1 = map.get(target-nums[i]);
                int sol2 = i;
                if(sol1 > sol2){
                    sol[0] = sol2;
                    sol[1] = sol1;
                } else {
                    sol[0]=sol1;
                    sol[1]=sol2;
                }
            } else {
                map.put(nums[i], i);
            }
        }

        return sol;

    }
}
