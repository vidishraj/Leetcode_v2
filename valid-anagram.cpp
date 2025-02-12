
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> existMap;
        for(char c:s){
            existMap[c]++;
        }
        for(char c:t){
            if(existMap.find(c)==existMap.end()){
                return false;
            }
            else{
                existMap[c]--;
                if(existMap[c]==0){
                    existMap.erase(c);
                }
            }
        }
        if(existMap.size()>0){
            return false;
        }
        return true;
    }
};