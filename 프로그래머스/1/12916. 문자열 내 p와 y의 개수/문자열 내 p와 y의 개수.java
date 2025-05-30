class Solution {
    boolean solution(String s) {
        int answer = 0;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='y'){
                answer += 1;
            }
            else if(c=='Y'){
                answer += 1;
            }
            else if(c=='P'){
                answer -= 1;
            }
            else if(c=='p'){
                answer -= 1;
            }
        }

        return answer == 0;
    }
}