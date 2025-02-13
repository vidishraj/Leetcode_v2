class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if( grid[0][0]==1){
            return -1;  //path doesn't exist            
        }
        if(grid.size()==1 && grid[0][0]==0){
            return 1;
        }
        int count=0;
        queue<pair<int,int>> points;
        pair<int,int> temp;
        temp.first=0;
        temp.second=0;
        grid[0][0]=1;
        if(grid.size()==2 && grid[1][1]==0){
            return 2;
        }
        points.push(temp);
        count++;
        int count1=0;
        int i,j;
        int distance=1;
        while(!points.empty()){ 
            while(count>0){
                pair<int,int> temp1=points.front();
                points.pop();
                i=temp1.first;
                j=temp1.second;
                if(i-1>=0 && grid[i-1][j]==0 ){//up
                    count1++;
                    temp1.first=i-1;
                    temp1.second=j;
                    points.push(temp1);
                    grid[i-1][j]=1;
                    if(i-1==grid.size()-1 && j==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(j-1>=0 && grid[i][j-1]==0){ //left
                    count1++;
                    temp1.first=i;
                    temp1.second=j-1;
                    points.push(temp1);
                    grid[i][j-1]=1;
                    if(i==grid.size()-1 && j-1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(i+1<grid.size() && grid[i+1][j]==0 ){ //right
                    count1++;
                    temp1.first=i+1;
                    temp1.second=j;
                    points.push(temp1);
                    grid[i+1][j]=1;
                    if(i+1==grid.size()-1 && j==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(j+1<grid.size() && grid[i][j+1]==0 ){//down
                    count1++;
                    temp1.first=i;
                    temp1.second=j+1;
                    points.push(temp1);
                    grid[i][j+1]=1;
                    if(i==grid.size()-1 && j+1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(i-1>=0 && j-1>=0 && grid[i-1][j-1]==0 ){ //top left
                    count1++;
                    temp1.first=i-1;
                    temp1.second=j-1;
                    points.push(temp1);
                    grid[i-1][j-1]=1;
                    if(i-1==grid.size()-1 && j-1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(j+1<grid.size() && i-1>=0 && grid[i-1][j+1]==0){//top right
                    count1++;
                    temp1.first=i-1;
                    temp1.second=j+1;
                    points.push(temp1);
                    grid[i-1][j+1]=1;
                    if(i-1==grid.size()-1 && j+1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(i+1<grid.size() && j-1>=0 && grid[i+1][j-1]==0 ){//bottom left
                    count1++;
                    temp1.first=i+1;
                    temp1.second=j-1;
                    points.push(temp1);
                    grid[i+1][j-1]=1;
                    if(i+1==grid.size()-1 && j-1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                if(i+1<grid.size() && j+1<grid.size() && grid[i+1][j+1]==0 ){ //bottom right
                    count1++;
                    temp1.first=i+1;
                    temp1.second=j+1;
                    points.push(temp1);
                    grid[i+1][j+1]=1;
                    if(i+1==grid.size()-1 && j+1==grid.size()-1){
                        distance++;
                        return distance;
                    }
                }
                count--;     
            }
            count=count1;
            count1=0;
            distance++;
        }
        return -1;
    }
};