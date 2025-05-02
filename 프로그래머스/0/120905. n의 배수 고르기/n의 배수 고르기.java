import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] numlist) {
        int num = 0;
        
        for(int i: numlist){
            if(i%n==0){
                num += 1;
            }
        }
        
        int[] answer = new int[num];
        int j = 0;
        for(int i: numlist){
            if(i%n==0){
                answer[j++]=i;
            }
        }
        return answer;
    }
} 