class Solution {
public:
    vector<string> fizzBuzz(int n) {
        int index=1;
        vector<string> res;
        for(int i=0;i<n;i++){
            if(index%3==0 && index%5==0){
                res.push_back("FizzBuzz");
            }
            else if(index%3==0){
                res.push_back("Fizz");
            }
            else if(index%5==0){
                res.push_back("Buzz");
            }
            else{
                string temp=to_string(index);
                res.push_back(temp);
            }
            index++;
        }
        return res;
    }
};