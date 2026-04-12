class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> unique = new HashSet<>();
        for(int n: nums){
            if (unique.contains(n)){
                return true;
            } else {
                unique.add(n);
            }
        }
        return false;
    }
}
