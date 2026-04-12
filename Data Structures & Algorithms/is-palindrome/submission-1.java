class Solution {
    public boolean isPalindrome(String s) {
        char[] sArray = s.toCharArray();
        ArrayList<Character> characters = new ArrayList<>();
        ArrayList<Character> reverse = new ArrayList<>();
        for(char c: sArray){
            if(Character.isLetter(c) || Character.isDigit(c)){
                characters.add(Character.toLowerCase(c));
            }
        }
        
        System.out.println(characters);

        for(int i = characters.size()-1; i >= 0; i--){
            reverse.add(characters.get(i));
        }

        System.out.println(reverse);

        for(int i = 0; i < characters.size(); i++){
            if(characters.get(i) != reverse.get(i)){
                return false;
            }
        }

        return true;
    }
}
