class Solution {
    public boolean isPalindrome(int x) {
        String str=Integer.toString(x);
        String str2="";
        for(int i=str.length()-1;i>=0;i--){
              str2=str2+str.charAt(i);
        }
        if(str.equals(str2)){
            return true;
        }
        else{
            return false;
        }
        
    }
}