class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> maps = new HashMap<>();
        HashMap<Character, Integer> mapt = new HashMap<>();
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        for(char sChar: sArr){
            if(maps.containsKey(sChar)){
                int num = maps.get(sChar);
                num++;
                maps.put(sChar, num);
            } else {
                maps.put(sChar, 1);
            }
        }

        for(char tChar: tArr){
             if(mapt.containsKey(tChar)){
                int num = mapt.get(tChar);
                num++;
                mapt.put(tChar, num);
            } else {
                mapt.put(tChar, 1);
            }
        }

        return mapt.equals(maps);

        

    }
}
