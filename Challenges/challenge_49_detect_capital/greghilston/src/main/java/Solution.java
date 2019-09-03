public class Solution  {
    /**
     * Determines capitalization is correct.
     * @param s to evaluate
     * @return whether we capitalization is correct
     */
    public boolean solve(String s) {
        String subString = s.substring(1, s.length());

        if(Character.isUpperCase(subString.charAt(0))) {
            for(char c : s.toCharArray()) {
                if(!Character.isUpperCase(c)) {
                    return false;
                }
            }
        } else {
            for(char c : s.toCharArray()) {
                if(Character.isUpperCase(c)) {
                    return false;
                }
            }
        }

        return true;
    }
 }