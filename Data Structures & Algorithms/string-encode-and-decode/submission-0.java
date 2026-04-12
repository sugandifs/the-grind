class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoding = new StringBuilder();
        for(String s: strs){
            // add the length of the string and a delimiter before the actual word
            encoding.append(s.length()).append('#').append(s);
        }
        return encoding.toString();
    }

    public List<String> decode(String str) {
        List<String> decode = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            // second, moving pointer
            int j = i;
            // while the delimiter isn't found, keep moving the second pointer
            while(str.charAt(j) != '#'){
                j++;
            }

            // once the delimiter is found, find the length of the substring from the
            // first pointer to the second pointer
            int length = Integer.parseInt(str.substring(i, j));

            // move the first pointer by 1, to get rid of the number
            i = j + 1;

            // move the second pointer by the length of the word from the first pointer
            j = i + length;

            // add the selected substring into the final arraylist
            decode.add(str.substring(i, j));

            // move the first pointer to the end of the added substring
            i = j;
        }
        return decode;
    }
}
