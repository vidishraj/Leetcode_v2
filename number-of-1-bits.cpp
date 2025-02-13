class Solution {
public:
    int hammingWeight(uint32_t n) {
        string s;
        while(n>0){
            if(n%2==1){
                s.push_back('1');
            }
            else{
                s.push_back('0');
            }
            n=n/2;
        }
        cout<<s;
        return count(s.begin(),s.end(),'1');
    }
};