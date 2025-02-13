class Solution {
public:
    void dfs( vector<int> &visited, vector<vector<int>>& grid, int i ){
        for(int j=0;j<grid[i].size();j++){
            if(grid[i][j]==1 && visited[j]==0){
                visited[j]=1;
                dfs(visited, grid, j);
            }
                grid[i][j]=0;
            
        }
        
    }
    
    int findCircleNum(vector<vector<int>>& grid) {
        vector<int> visited(grid[0].size(),0);
        int islands=0;
        for(int i=0;i<grid.size();i++){
            visited.clear();
            for(int j=0;j<grid.size();j++){
                if(grid[i][j]==1 && visited[i]==0){
                    visited[i]=1;
                    dfs(visited,grid, i);
                    islands++;
                }
            }
        }
        return islands;
        
    }
};