class Solution {
public:
    string convertToTitle(int columnNumber) {
        string res;
        char a ='A';
        while( columnNumber>0){
            --columnNumber;
            int mod=columnNumber%26;
            //printf("%d %d ",mod, columnNumber);
            res.push_back(a+mod);
            columnNumber/=26;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};