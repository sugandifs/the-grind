class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        HashMap<Character, Integer> sCount = new HashMap<>();
        HashMap<Character, Integer> tCount = new HashMap<>();

        for(char c: sArray){
            if(sCount.containsKey(c)){
                sCount.put(c, sCount.get(c)+1);
            } else {
                sCount.put(c, 1);
            }
        }

        for(char c: tArray){
            if(tCount.containsKey(c)){
                tCount.put(c, tCount.get(c)+1);
            } else {
                tCount.put(c, 1);
            }
        }

        if(sCount.equals(tCount)){
            return true;
        }

        return false;
    }
}
