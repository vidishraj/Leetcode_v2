class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
	    vector<vector<int> > result;
	    permuteRecursive(num, 0, result);
        sort(result.begin(), result.end());
        auto it=unique(result.begin(), result.end());
        result.resize(distance(result.begin(), it));
	    return result;
    }
    
    // permute num[begin..end]
    // invariant: num[0..begin-1] have been fixed/permuted
	void permuteRecursive(vector<int> &num, int begin, vector<vector<int> > &result)	{
		if (begin >= num.size()) {
		    // one permutation instance
		    result.push_back(num);
		    return;
		}
		
		for (int i = begin; i < num.size(); i++) {
		    swap(num[begin], num[i]);
		    permuteRecursive(num, begin + 1, result);
		    // reset
              
		    swap(num[begin], num[i]);
		}
    }
};