class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        unordered_map<char, string> gmap;
        string two="abc";
        string three="def";
        string four="ghi";
        string five="jkl";
        string six="mno";
        string seven="pqrs";
        string eight="tuv";
        string nine="wxyz";
        gmap['2']= two;
        gmap['3']=three;
        gmap['4']=four;
        gmap['5']=five;
        gmap['6']=six;
        gmap['7']=seven;
        gmap['8']=eight;
        gmap['9']=nine;
        for(int i=0;i<digits.size();i++){
            int x=1;
            for(int j=i+1;j<digits.size();j++){
                string temp=gmap[digits[j]];
                x*=temp.size();
            }
            if( res.empty()){
                //printf("yess");
                string target=gmap[digits[i]];
                for(int k=0;k<target.size();k++){
                    int t=0;
                    while( t<x){
                        string temp;
                        temp.push_back(target[k]);
                        res.push_back(temp);
                        t++;
                    }
                }
            }
            else{
                string target=gmap[digits[i]];
                int t=0;
                int f=0;
                for(int l=0;l<res.size();l++){
                    if(t<x){
                        res[l].push_back(target[f]);
                        t++;
                    }
                    if(t==x){
                        t=0;
                        f++;
                    }
                    if(f==target.size()){
                        f=0;
                    }
                }
            }            
        }
        return res;
    }
};