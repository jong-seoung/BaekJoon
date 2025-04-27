class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int num = 0;
        for(int i: numbers){
            answer += i;
            num += 1;
        }
        answer = answer / num;
        return answer;
    }
}