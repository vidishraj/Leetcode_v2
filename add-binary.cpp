class Solution {
public:
    string addBinary(string a, string b) {
        int flag=0;
        int i=a.size()-1;
        int j=b.size()-1;
        string res; 
        while(i>=0 && j>=0){
            if( a[i]=='1' && b[j]=='1'){
                if( flag==1){
                    res.push_back('1');
                }
                else{
                    res.push_back('0');
                    flag=1;
                }
            }
            if( a[i]=='1' && b[j]=='0'){
                if( flag==1){
                    res.push_back('0');
                }
                else{
                    res.push_back('1');
                }
            }
            if(a[i]=='0' && b[j]=='1'){
                if( flag==1){
                    res.push_back('0');
                }
                else{
                    res.push_back('1');
                }
            }
            if( a[i]=='0' && b[j]=='0'){
                if( flag==1){
                    res.push_back('1');
                    flag=0;
                }
                else{
                    res.push_back('0');
                }
                
            }
            i--;
            j--;
            
        }
        while(i>=0){
            if( a[i]=='1'){
                if( flag==1){
                    res.push_back('0');
                }
                else{
                    res.push_back('1');
                }
            }
            if( a[i]=='0'){
                if(flag==1){
                    res.push_back('1');
                    flag=0;
                }
                else{
                    res.push_back('0');
                }
            }
            i--;
        }
        while(j>=0){
            if( b[j]=='1'){
                if( flag==1){
                    res.push_back('0');
                }
                else{
                    res.push_back('1');
                }
            }
            if( b[j]=='0'){
                if(flag==1){
                    res.push_back('1');
                    flag=0;
                }
                else{
                    res.push_back('0');
                }
            }
            j--;
        }
        if( flag==1){
            res.push_back('1');
        }
        reverse(res.begin(), res.end());
        return res;
    }
};