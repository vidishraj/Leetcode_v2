class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        map<int, float> positionOrderMap; 
        for(int i =0; i<position.size();i++){
            positionOrderMap[position[i]]=float(float(target-position[i])/float(speed[i]));
        }
        int fleets=1;
        float currentRunningSpeed = 0;
        if(!positionOrderMap.empty()){
            currentRunningSpeed =(--positionOrderMap.end())->second;   
        }
        for(auto it = ++positionOrderMap.rbegin(); it!=positionOrderMap.rend();it++){
            if(currentRunningSpeed<it->second){
                currentRunningSpeed=it->second;
                fleets++;
            }
        }
        return fleets;
    }
};