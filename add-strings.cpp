class Solution {
public:
    string addStrings(string num1, string num2) {
        unordered_map<char,int> gmap;
        unordered_map<int,char> gmap1;
        char c='0';
        for(int i=0;i<10;i++){
            gmap[c]=i;
            gmap1[i]=c;
            c++;
        }
        string ans;
        int carry=0;
        int i=num1.size()-1;
        int j=num2.size()-1;
        while(i>=0 && j>=0){
            int n1=gmap[num1[i]];
            int n2=gmap[num2[j]];
            i--;
            j--;
            int sum=n1+n2;
            if(carry==1){
                sum++;
                carry=0;
            }
            if(sum>=10){
                carry=1;
                sum=sum%10;
            }
            //cout<<sum<<" ";
            char x=gmap1[sum];
           // cout<<x;
            ans.push_back(x);
        }
        while(i>=0){
            char x;
            if(carry==1){
                int sum=gmap[num1[i]]+1;
                carry=0;
                if( sum>=10){
                    carry=1;
                    sum=sum%10;
                }
                x=gmap1[sum];
            }
            else{
                x=num1[i];
            }
            cout<<x;
            ans.push_back(x);
            i--;
        }
        while(j>=0){
            char x;
            if(carry==1){
                int sum=gmap[num2[j]]+1;
                carry=0;
                if( sum>=10){
                    carry=1;
                    sum=sum%10;
                }
                x=gmap1[sum];
            }
            else{
                x=num2[j];
            }
            ans.push_back(x);
            j--;
        }
        if(carry==1){
            ans.push_back('1');
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};