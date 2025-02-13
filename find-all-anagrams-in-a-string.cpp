class Solution {
public:
    string s="abcdefghijklmnopqrstuvwxyz";
    bool check(unordered_map<char,int> &gmap, unordered_map<char,int> &gmap1){
        
        for(int i=0;i<=26;i++){
            if(gmap[s[i]]!=gmap1[s[i]]){
                return false;
            }
        }
        return true;
    }
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        if(s.size()==0 ||p.size()==0){
            return res;
        }
        unordered_map<char, int> gmap1;
        unordered_map<char, int> gmap2;
        for(int i=0;i<p.size();i++){
            gmap1[s[i]]++;
            gmap2[p[i]]++;
        }
        int i=0;
        int j=p.size();
        while(j<=s.size()){
            if(check(gmap1,gmap2)){
                res.push_back(i);
            }
            gmap1[s[i]]--;//removing first character
            gmap1[s[j]]++;//adding next character;
            i++;
            j++;
        }
        return res;
        
    }
};