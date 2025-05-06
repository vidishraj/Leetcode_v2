class Solution {
public:
    unordered_map<char, int> gmap;
    bool check(string s, string t, string &order){//s is the first word
        int i=0;
        int j=0;
        while(i< s.size() && j<t.size()){
            if(gmap[s[i]]>gmap[t[j]]){ 
                return false;
            }
            if( gmap[s[i]]<gmap[t[j]]){
                return true;
            }
            i++;
            j++;
        }
        if(i<s.size() && j==t.size()){
            //printf("yess");
            return false;
        }
        return true;
    }
    bool isAlienSorted(vector<string>& words, string order) {
        //can we map the order first and then check 
        //we will have to check in pairs
        //use a hash map to attach the letter with the order
        
        for(int i=0;i<order.size();i++){
            gmap[order[i]]=i;
        }
        for(auto it=gmap.begin();it!=gmap.end();++it){
           // printf("%c %d\n", it->first, it->second);
        }
        for(int i=0;i+1<words.size();i++){
            bool x=check(words[i], words[i+1], order);
            if(x==false){
                return false;
            }
        }
        return true;
    }
};