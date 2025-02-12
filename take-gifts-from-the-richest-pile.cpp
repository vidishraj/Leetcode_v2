
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        //sort the arrays first, travel till k and take the square root, subtract from the total and return it
        sort(gifts.begin(), gifts.end(), greater());
        long long sum=0;
        
        long long max=0;
        for(int i=0;i<k;i++){
            max=*max_element(gifts.begin(), gifts.end());
            int index = find(gifts.begin(),gifts.end(),max)-gifts.begin();
            gifts[index]=floor(sqrt(gifts[index]));
         //    cout<<gifts[i];
        }
        // for(int i=0;i<gifts.size();i++){
        //     cout<<gifts[i]<<"-->";
        // }
        return accumulate(gifts.begin(), gifts.end(),sum);
    }
};