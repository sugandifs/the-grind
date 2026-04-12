class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> unique = new HashSet<Integer>();

        for(int n: nums){
            if(unique.contains(n)){
                return true;
            }

            unique.add(n);
        }
        return false;
    }
}
