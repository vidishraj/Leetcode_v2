class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> gmap;
        for(int i=0;i<s.size();i++){
            gmap[s[i]]++;
        }
        int sum=0;
        int max=0;
        for(auto it=gmap.begin();it!=gmap.end();it++){
            if(it->second%2==0){
                sum+=it->second;
            }
            else{
                sum+=it->second-1;
                if(max<it->second){
                    max=it->second;
                }
            }
        }
        if(max!=0){
            sum++;
        }
        return sum;
    }
};