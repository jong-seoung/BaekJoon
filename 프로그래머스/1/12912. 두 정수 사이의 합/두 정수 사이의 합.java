class Solution {
    public long solution(int a, int b) {
        int M = 0;
        int N = 0;
        if (a>b){
            M = a;
            N = b;
        }
        else{
            M = b;
            N = a;
        }
        
        long answer = M;

        
        for(int i=0; i<M-N;i++){
            answer += N+i;
        }
        
        return answer;
    }
}