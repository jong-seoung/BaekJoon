import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = String.valueOf(n);
        
        for(String i: s.split("")){
            answer += Integer.parseInt(i);
        }
        return answer;
    }
}