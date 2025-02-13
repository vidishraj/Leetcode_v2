class Solution {
public:
    int check(vector<int> &nums, int &i , int &j){
       int diff=nums[i+1]-nums[i];
        if( diff==nums[j]-nums[i+1]){
            return 1;
        }
        return 0;
    }
    int add(int k){
        if(k==0){return 0;}
        int total=2;
        int add=3;
        int i=1;
        while(i<k){
            total+=add;
            add++;
            i++;
        }
        return total;
    }
    int numberOfArithmeticSlices(vector<int>& nums) {
        //can it also be done through sliding window?
        if( nums.size() <3){//first case
            return 0;
        }
        int i=0;
        int j=2;
        int total=0;
        while(i<j && i<nums.size() && j<nums.size()){
            while(i<nums.size() && j<nums.size() && !check(nums, i , j)){
                i++;
                j++;
            }
            if( i<nums.size() && j<nums.size()){
                total++;
                int diff=nums[i+1]-nums[i];
                int k=j;
                while(k+1<nums.size() && nums[k+1]-nums[k]==diff ){
                    k++;
                }
                
                total+=add(k-j);
                i=k;
                j=i+2;
            }
        }
        return total;
    }
};