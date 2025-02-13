class Solution {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        map<int, int> gmap;
        int k;
        map<int,int>::iterator itr;
        for(int i=0;i<ranges.size();i++){
            if( gmap[ranges[i][0]]==0){
                gmap[ranges[i][0]]=ranges[i][1];
            }
            else{
                k=ranges[i][0];
                while(gmap[k]!=0){
                    k++;
                }
                gmap[k]=ranges[i][1];
            }
        }
        itr=gmap.begin();
        int flag=0;
        while(itr!=gmap.end()){
            if( left>=itr->first && itr->second>=left){
                left=itr->second+1;
                flag=1;
            }
            if( left>right && flag==1){                
                return true;
            }
            ++itr;
        }
        return false;;
    }
};