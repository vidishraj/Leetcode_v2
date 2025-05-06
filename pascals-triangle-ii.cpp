class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;
        if( rowIndex==0){
            res.push_back(1);
            return res;
        }
        if( rowIndex==1){
            res.push_back(1);
            res.push_back(1);   
            return res;
        }
        int i=1;
        //always push back 1 in the end
        //always start with index 1
        while(i<=rowIndex){
            int j=1;
            vector<int> temp;
            temp.push_back(1);
            int k=0;
            while( k+1<res.size()){
                temp.push_back(res[k]+res[k+1]);
                k++;
            }
            temp.push_back(1);
            res=temp;
            i++;
        }
        return res;
    }
};