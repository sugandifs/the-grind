class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> sletters = new HashMap<>();
        HashMap<Character, Integer> tletters = new HashMap<>();



        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        for(char c: sArray){
            if(sletters.containsKey(c)){
                sletters.put(c, sletters.get(c) + 1);
            } else {
                sletters.put(c, 1);
            }
        }

        for(char c: tArray){
            if(tletters.containsKey(c)){
                tletters.put(c, tletters.get(c) + 1);
            } else {
                tletters.put(c, 1);
            }
        }

        if(tletters.equals(sletters)){
            return true;
        }

        return false;
        

    }
}
