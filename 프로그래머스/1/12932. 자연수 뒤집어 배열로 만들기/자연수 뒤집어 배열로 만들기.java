class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        int len = s.length();
        int[] answer = new int[len--];
        
        for(String i: s.split("")){
            answer[len--] = Integer.parseInt(i);
        }
        return answer;
    }
}