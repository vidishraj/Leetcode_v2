class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> gmap;
        for(int i=0;i<s.size();i++){
            gmap[s[i]]++;
        }
        for(int i=0;i<s.size();i++){
            if(gmap[s[i]]==1){
                return i;
            }
        }
        return -1;
    }   
};