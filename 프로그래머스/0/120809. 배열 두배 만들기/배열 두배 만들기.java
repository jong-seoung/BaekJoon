class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        int index = 0;
        for(int i:numbers){
            answer[index++] = i*2;
        }
        return answer;
    }
}