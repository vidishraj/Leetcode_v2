#include<vector>
class Solution {
public:
    //a stack has to be used for this 
    int evalRPN(vector<string>& token) {
        vector<int>s;
        int a;
        int b;
        int res;
        for(int i=0;i<token.size();i++){
            if(token[i]=="+" || token[i]=="-" || token[i]=="/" || token[i]=="*"){
                a=s.back();
                s.pop_back();
                b=s.back();
                s.pop_back();
                if( token[i]=="+"){
                    res=a+b;
                }
                if( token[i]=="-"){
                    res=b-a;
                }
                if( token[i]=="*"){
                    res=a*b;
                }
                if( token[i]=="/"){
                    res=b/a;
                }
               // cout<<res<<a<< b<<" \n";
                s.push_back(res);
            }
            else{
                string x=token[i];
                int operand=stoi(x);
                s.push_back(operand);
            }
        }
        return s.back();
    }
};