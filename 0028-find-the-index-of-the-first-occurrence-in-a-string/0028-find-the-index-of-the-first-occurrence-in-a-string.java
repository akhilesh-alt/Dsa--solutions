class Solution {
    public int strStr(String haystack, String needle) {
        int id=-1;
        if(haystack.contains(needle)){
            id=haystack.indexOf(needle);
        }
        return id;
    }
}