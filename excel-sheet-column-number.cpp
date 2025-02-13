class Solution {
public:
    int add_val(char a){    //will return the addition value
        return a%64;
    }
    int titleToNumber(string columnTitle) {
        int total =add_val(columnTitle[columnTitle.size()-1]);//added last 
        int x=columnTitle.size()-2;
        int i=1;
        while( x>=0){
            //I am going from the back, but i want 26 multiplied 
            //printf("%d\n", total);
            total+=(add_val(columnTitle[x])*pow(26,i));
            i++;
            x--;
        }
        return total;
    }
};