class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        for(auto x: strs){
            string sortedSt = x;
            sort(sortedSt.begin(),sortedSt.end());
            mp[sortedSt].push_back(x);
        }
        vector<vector<string>> ans(mp.size());
        int i=0;
        for(auto x:mp){
            for(auto item: x.second){
                ans[i].push_back(item);
            }
            i++;
        }
        return ans;
    }
};
