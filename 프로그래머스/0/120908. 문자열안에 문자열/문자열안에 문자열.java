class Solution {
    public int solution(String str1, String str2) {
        int answer = 2;
        
        for(int i =0; i<=str1.length()-str2.length(); i++){
            System.out.println(str1.substring(i, i+str2.length()));
            if(str1.substring(i, i+str2.length()).equals(str2)){
                return 1;
            }
        }
        return answer;
    }
}