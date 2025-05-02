class Solution {
    public int[] solution(int n) {
        int cnt = 0;
        for (int i=1; i<=n;i++){
            if(i%2==1){
                cnt++;
            }
        }
        
        int[] answer = new int[cnt];
        int index = 0;
        
        for (int i=1; i<=n;i++){
            if(i%2==1){
                answer[index++] = i;
            }
        }
        return answer;
    }
}