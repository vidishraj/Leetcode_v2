class Solution {
public:
    
    vector<int> decimal_to_bits(uint32_t n){
        vector<int> temp;
        while( n!=0){
        temp.insert(temp.begin(),n%2);
            n=n/2;
        }
        return temp;
    }
    uint32_t reverseBits(uint32_t n) {
        vector<int>temp=decimal_to_bits(n);
        long res=0;
        while( temp.size()!=32){
            temp.insert(temp.begin(),0);
        }
        reverse(temp.begin(),temp.end());
        for(int i=temp.size()-1;i>=0;i--){
            if(temp[i]==1){
                res+=(pow(2, temp.size()-i-1));
            }
        }
        
        return res;
    }
};