class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(String s: strs){
            int[] count = new int[26];
            for (char c: s.toCharArray()){
                // identifies which position to put in the count array
                count[c-'a']++;
            }

            // converts the array into string form
            String key = Arrays.toString(count);
            // uses the array as the map key, with an arraylist of strings as the value
            map.putIfAbsent(key, new ArrayList<>());
            // adds the string to the arraylist
            map.get(key).add(s);

            // by doing this, all strings that have the same array will have the word added into the string arraylist
        }

        return new ArrayList<>(map.values());
    }
}
