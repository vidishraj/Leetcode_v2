/*class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> temp;
        int ignored=0;
        for(int i=0;i<cost.size();i++){
            if( cost[i]==0 && gas[i]==0){
                ignored++;
            }
            else{
             temp.push_back(gas[i]-cost[i]);}
        }
        for(int i=0;i<temp.size();i++){
            int fuel=0;
            if(temp[i]>=0){//can start from this index
                fuel=temp[i];
                int j=i+1;
                int flag=0;
                while(fuel>=0 && j!=i && flag==0){
                    if(j==temp.size()){
                        j=0;
                    }
                    if(j==i){
                        flag==1;
                    }
                    if( j!=i){
                      fuel+=temp[j];
                      j++;  
                    }
                }
                if( j==i && fuel>=0){
                    return i+ignored;
                }
                i=j+1;
            }
        }
        return -1;
    }
};*/
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int start(0),total(0),tank(0);
        //if car fails at 'start', record the next station
        for(int i=0;i<gas.size();i++) if((tank=tank+gas[i]-cost[i])<0)                      {start=i+1;total+=tank;tank=0;}
        return (total+tank<0)? -1:start;
    }
};