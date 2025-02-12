class Solution {
public:
    int digitSum(int num) {
        int sum=0;
        while(num>0){
            sum+=num%10;
            num/=10;
        }
        cout<<sum;
        return sum;
    }
    int addDigits(int num) {
        if(num<10){
            return num;
        }
        return addDigits(digitSum(num));
    }
};