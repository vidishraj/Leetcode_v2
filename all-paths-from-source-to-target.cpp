
// all possible paths 
// given in the form of an adjacency list 
//find all paths form 0 to n-1
//keep a visited while exploring each node 
class Solution {
public:
    
    void dfs(vector<vector<int>>& graph, vector<vector<int>>& result, vector<int> path, int src, int dst) {
    path.push_back(src);
    if(src == dst) {
        result.push_back(path);
        return;
    }

    for(int i=0; i< graph[src].size();i++)
        dfs(graph, result, path, graph[src][i], dst);
}
vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
    vector<vector<int>> paths; vector<int> path;
    int nodes = graph.size();
    if(nodes == 0) return paths;
    dfs(graph, paths, path, 0, nodes - 1);
    return paths;
}
};