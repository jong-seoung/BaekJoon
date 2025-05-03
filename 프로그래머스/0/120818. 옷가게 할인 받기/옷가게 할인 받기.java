class Solution {
    public int solution(double price) {
        double discount = 0.00;
        
        if(price>=100000 && price<300000){
            discount = 0.05;
        }
        else if(price<500000 && price>= 300000){
            discount = 0.10;
        }
        else if(price>= 500000){
            discount = 0.20;
        }
        
        
        int answer = (int)(price-(price*discount));
        return answer;
    }
}